from surprise import SVD, KNNBaseline
from collections import defaultdict

class Recommender:
    def __init__(self, trainset, algorithm_type='SVD'):
        self.trainset = trainset
        self.algorithm_type = algorithm_type
        
        if self.algorithm_type == 'SVD':
            self.algorithm = SVD()
        elif self.algorithm_type == 'KNNBaseline':
            self.algorithm = KNNBaseline()
        else:
            raise ValueError("Invalid algorithm type. Choose 'SVD' or 'KNNBaseline'.")
        
        self.predictions = None
        self.top_n_recommendations = None

    def train(self):
        """Train the recommendation model."""
        self.algorithm.fit(self.trainset)

    def predict(self, testset):
        """Make predictions on a testset."""
        self.predictions = self.algorithm.test(testset)
        return self.predictions

    def get_top_n(self, n=10):
        """Get the top N recommendations for each user."""
        top_n = defaultdict(list)
        
        for uid, iid, true_r, est, _ in self.predictions:
            top_n[uid].append((iid, est))
        
        for uid, user_ratings in top_n.items():
            user_ratings.sort(key=lambda x: x[1], reverse=True)
            top_n[uid] = user_ratings[:n]
        
        self.top_n_recommendations = top_n
        return top_n
