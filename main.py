{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "95af9339-5afc-4498-95ec-b29f49972ed9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Saved fitted pipeline!\n",
      "✅ Saved X_sparse.pkl!\n"
     ]
    }
   ],
   "source": [
    "# 1. Import required libraries\n",
    "import pandas as pd\n",
    "import joblib\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.preprocessing import OneHotEncoder, StandardScaler\n",
    "from sklearn.pipeline import Pipeline\n",
    "from scipy.sparse import csr_matrix\n",
    "\n",
    "# 2. Load your dataset\n",
    "df = pd.read_excel(r\"C:\\Users\\kavya\\Downloads\\online_course_recommendation_v2.xlsx\")\n",
    "\n",
    "# 3. Define your preprocessing pipeline (example structure)\n",
    "numeric_features = ['rating', 'course_duration_hours', 'enrollment_numbers', 'course_price', 'feedback_score', 'time_spent_hours', 'previous_courses_taken']\n",
    "categorical_features = ['difficulty_level', 'certification_offered', 'study_material_available']\n",
    "\n",
    "preprocessor = ColumnTransformer(\n",
    "    transformers=[\n",
    "        ('num', StandardScaler(), numeric_features),\n",
    "        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)\n",
    "    ]\n",
    ")\n",
    "\n",
    "# 4. Create pipeline (if needed you can add models too)\n",
    "pipeline = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor)\n",
    "])\n",
    "\n",
    "# 5. Fit the pipeline on your dataframe\n",
    "pipeline.fit(df)\n",
    "\n",
    "# 6. Save the fitted pipeline\n",
    "joblib.dump(pipeline, r\"C:\\Users\\kavya\\Desktop\\OCR\\content_pipeline.pkl\")\n",
    "print(\"✅ Saved fitted pipeline!\")\n",
    "\n",
    "# 7. Now transform the data\n",
    "X = pipeline.transform(df)\n",
    "X_sparse = csr_matrix(X)\n",
    "\n",
    "# 8. Save the sparse matrix\n",
    "joblib.dump(X_sparse, r\"C:\\Users\\kavya\\Desktop\\OCR\\X_sparse.pkl\")\n",
    "print(\"✅ Saved X_sparse.pkl!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33e12ce9-53c2-48cf-9298-bc786b4ecb50",
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
