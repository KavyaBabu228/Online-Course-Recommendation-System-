from fastapi import FastAPI
import joblib
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_distances

app = FastAPI(title="Online Course Recommender System")

# Load saved models and data
pipeline = joblib.load("content_pipeline.pkl")
X_sparse = joblib.load("X_sparse.pkl")
user_item_matrix = joblib.load("user_item_matrix.pkl")
user_item_sparse = joblib.load("user_item_sparse.pkl")
df = pd.read_excel("online_course_recommendation_v2.xlsx")  # Make sure this file is in the same directory

@app.get("/")
def home():
    return {"message": "Online Course Recommender System is running!"}

@app.get("/recommend")
def recommend(course_name: str, alpha: float = 0.5, n_recs: int = 5):
    if course_name not in user_item_matrix.columns:
        return {"error": "Course not found!"}
    
    idx = user_item_matrix.columns.get_loc(course_name)

    content_distances = cosine_distances(X_sparse[idx], X_sparse).flatten()
    cf_distances = cosine_distances(user_item_sparse.T[idx], user_item_sparse.T).flatten()

    hybrid_score = alpha * cf_distances + (1 - alpha) * content_distances
    recommended_indices = hybrid_score.argsort()[1:n_recs+1]

    recommended_courses = df.iloc[recommended_indices][['course_name', 'difficulty_level', 'certification_offered']]

    return recommended_courses.to_dict(orient="records")
