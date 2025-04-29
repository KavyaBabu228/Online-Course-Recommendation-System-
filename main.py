{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "33e12ce9-53c2-48cf-9298-bc786b4ecb50",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI\n",
    "import joblib\n",
    "import pandas as pd\n",
    "from scipy.sparse import csr_matrix\n",
    "from sklearn.metrics.pairwise import cosine_distances\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "# Load saved files\n",
    "pipeline = joblib.load('content_pipeline.pkl')\n",
    "X_sparse = joblib.load('X_sparse.pkl')\n",
    "user_item_matrix = joblib.load('user_item_matrix.pkl')\n",
    "user_item_sparse = joblib.load('user_item_sparse.pkl')\n",
    "\n",
    "# Load course dataset\n",
    "df = pd.read_excel(r\"C:\\Users\\kavya\\Downloads\\online_course_recommendation_v2.xlsx\")\n",
    "\n",
    "@app.get(\"/\")\n",
    "def home():\n",
    "    return {\"message\": \"Online Course Recommender System is running!\"}\n",
    "\n",
    "@app.get(\"/recommend\")\n",
    "def recommend(course_name: str, alpha: float = 0.5, n_recs: int = 5):\n",
    "    if course_name not in user_item_matrix.columns:\n",
    "        return {\"error\": \"Course not found!\"}\n",
    "    \n",
    "    idx = user_item_matrix.columns.get_loc(course_name)\n",
    "\n",
    "    # Calculate content similarity\n",
    "    content_distances = cosine_distances(X_sparse[idx], X_sparse).flatten()\n",
    "\n",
    "    # Calculate CF similarity\n",
    "    cf_distances = cosine_distances(user_item_sparse.T[idx], user_item_sparse.T).flatten()\n",
    "\n",
    "    # Hybrid\n",
    "    hybrid_score = alpha * cf_distances + (1 - alpha) * content_distances\n",
    "    recommended_indices = hybrid_score.argsort()[1:n_recs+1]\n",
    "\n",
    "    recommended_courses = df.iloc[recommended_indices][['course_name', 'difficulty_level', 'certification_offered']]\n",
    "\n",
    "    return recommended_courses.to_dict(orient=\"records\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42bd6553-9988-45f5-96ab-78faf8392a78",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
