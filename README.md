# 🎓 Online Course Recommendation System

This project aims to build a hybrid recommendation system that suggests online courses based on user preferences, past ratings, and course content. By combining collaborative filtering and content-based filtering techniques, the system helps users discover relevant and personalized learning opportunities.

---

## 📌 Objective

The goal is to develop a robust recommender system that:

- Performs exploratory data analysis to understand user behavior and course features  
- Builds a content-based recommender using course metadata  
- Implements collaborative filtering using user feedback and ratings  
- Combines both methods into a hybrid recommendation model  
- (Optional) Deploys the system for real-time interaction

---

## 🔍 Exploratory Data Analysis (EDA)

A detailed EDA was carried out to understand the dataset structure and extract insights:

- Analyzed course rating distributions, price trends, feedback patterns  
- Explored relationships between duration, difficulty level, and certification  
- Checked for missing values and data inconsistencies  
- Used correlation heatmaps and distribution plots for visual analysis  

---

## 🧠 Model Development

Two recommendation strategies were implemented and combined:

### 🔹 Content-Based Filtering
- Extracted features such as course title, description, duration, price, certification, etc.  
- Used cosine similarity to recommend courses similar to a selected course  
- Prioritized attributes based on their influence on user preferences  

### 🔹 Collaborative Filtering
- Applied matrix factorization techniques using the `Surprise` library (SVD, KNNBasic)  
- Predicted user ratings based on similar users’ behaviors  
- Evaluated performance using RMSE and cross-validation  

### 🔹 Hybrid Model
- Combined scores from both methods to balance personalization and popularity  
- Tuned weights to maximize relevance and accuracy of recommendations  

---

## 🔧 Optimization & Evaluation

- Evaluated models using RMSE, precision@k, and user satisfaction  
- Tuned similarity thresholds and content filters for better output diversity  
- Performed cold-start handling for new users and unrated courses  

---

## 🚀 Deployment

The system can be deployed using **Streamlit** .
Deployment - http://localhost:8501/
### Key Features:
- Simple UI to enter course preferences or select past rated courses  
- Backend logic to process input and generate top N course recommendations  
- Ready for local or cloud deployment (Heroku, Streamlit Cloud)

---

## ✅ Project Outcomes

- Built a scalable, hybrid recommendation system for online courses  
- Successfully integrated both content-based and collaborative filtering  
- Delivered accurate and relevant recommendations based on real user behavior  
- Demonstrated strong data preprocessing and model building skills in a practical project  

---

## 🧰 Technologies & Tools

- **Programming**: Python  
- **Libraries**: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `Surprise`  
- **Deployment**: Streamlit / Flask *(optional)*  
- **Environment**: Jupyter Notebook, Git  

---

## 📈 Future Enhancements

- Integrate deep learning approaches (e.g., Neural Collaborative Filtering)  
- Add user profiles and login system for personalized dashboards  
- Support multi-modal inputs (e.g., video duration, instructor rating, reviews)  
- Deploy via Docker and implement CI/CD for production readiness  

---

## 🙋‍♀️ Author

**Kavya Babu**  
[LinkedIn](https://www.linkedin.com/in/kavya-babu-15a36a2b5/)
