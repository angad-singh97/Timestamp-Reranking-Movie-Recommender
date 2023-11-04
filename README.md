Temporal Re-Ranking Based Movie Recommender System 🎬✨

**Overview:**
This project is a movie recommender engine written using Python and the Scikit-Surprise libraries to generate better movie recommendations by utilizing temporal user interaction data. The project also includes a configurable simulator that demonstrates system usage in multiple Collaborative Filtering techniques (Matrix Factorization and K-Nearest Neighbours).We simulate user interactions over time, enriching our data, and continuously retrain our models for more accurate and timely recommendations.

**How It Works:**

Initialization: Load the movie ratings dataset and train the recommendation models.

Recommendation Generation: Based on trained models, generate top-N recommendations for each user.

User Interaction Simulation: Users "rate" recommended movies. These interactions are timestamped and appended back to the dataset, simulating real-world behavior.

Model Retraining: Periodically retrain models on the enriched dataset, incorporating recent simulated user interactions.

Metadata Management: A metadata file tracks simulated dates ensuring logical continuity.

