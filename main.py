{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ba7ae582-b907-4642-be93-ed074a1f6338",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI\n",
    "import joblib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "369d840a-43e7-4c35-bee6-e9066275d733",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = FastAPI()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f617b53-563e-4c65-9b39-14491f37e68f",
   "metadata": {},
   "source": [
    "#### Load models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a39deb98-75c9-41a7-b5f9-f63de405a775",
   "metadata": {},
   "outputs": [],
   "source": [
    "pipeline = joblib.load('content_pipeline.pkl')\n",
    "knn_model = joblib.load('content_knn_model.pkl')\n",
    "\n",
    "@app.get(\"/recommend\")\n",
    "def recommend(course_name: str, alpha: float = 0.5, n_recs: int = 5):\n",
    "    # Recommendation logic here\n",
    "    return {\"message\": \"Recommendations for \" + course_name}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da28435d-ba27-439b-ba01-0aebd354e3a2",
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
