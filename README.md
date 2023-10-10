# temporal-reranking-movie-recommender

Movie Recommender System 🎬✨
Overview:
An advanced movie recommendation system built using collaborative filtering techniques. Through this project, we harness the power of both matrix factorization (SVD) and memory-based (KNNBaseline) algorithms, and even introduce a hybrid approach. We simulate user interactions over time, enriching our data, and continuously retrain our models for more accurate and timely recommendations.

Features:
Dual Recommender Engines: Employs both SVD and KNNBaseline recommendation algorithms from the surprise library.

Hybrid Recommendation: Merges the strength of both algorithms for enhanced user recommendations.

Dynamic User Simulation: Simulates user behavior to generate ratings, enabling a feedback loop for continuous model improvement.

Timestamped Recommendations: Recommendations are mindful of the last rated date, keeping them fresh and relevant.

Evaluation Metrics: Implements precision and diversity metrics to gauge recommendation quality.

How It Works:
Initialization: Load the movie ratings dataset and train the recommendation models.

Recommendation Generation: Based on trained models, generate top-N recommendations for each user.

User Interaction Simulation: Users "rate" recommended movies. These interactions are timestamped and appended back to the dataset, simulating real-world behavior.

Model Retraining: Periodically retrain models on the enriched dataset, incorporating recent simulated user interactions.

Metadata Management: A metadata file tracks simulated dates ensuring logical continuity.