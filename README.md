#Course Recommendation System


A hybrid course recommendation system combining Content-Based Filtering and Collaborative Filtering to recommend courses based on course features (like course name, difficulty, certification offered) and user ratings.

Overview

This project implements a Hybrid Course Recommendation System using:

Content-Based Filtering: Recommends courses based on content features like course name, difficulty level, certification, etc.

Collaborative Filtering: Recommends courses based on user ratings and interactions.

Hybrid System: Combines both content-based and collaborative recommendations, controlled by an adjustable alpha parameter.


Features

Content-Based Filtering using K-Nearest Neighbors (KNN).

Collaborative Filtering using a user-item matrix.

Hybrid Recommendation System blending both methods.

Tuning Parameters for alpha (blend ratio), n_neighbors (KNN), and distance metric (cosine, euclidean).

API built using FastAPI for recommending courses based on user input.
