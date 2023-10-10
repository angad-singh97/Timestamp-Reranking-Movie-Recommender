# controller.py
from config import CONFIG
from datahandler import DataHandler
from recommender import Recommender
from utility import get_top_n

class Controller:
    def __init__(self):
        self.datahandler = DataHandler(
            CONFIG['DATA_PATH'], 
            CONFIG['MOVIE_PATH'], 
            CONFIG['RATING_PATH']
        )
        self.recommender = None

    # Initialize data handler
    data_handler = DataHandler('ml-latest-small/ratings_fixed_main.csv', 
                               'ml-latest-small/movies_fixed_main.csv', 
                               'ml-latest-small/ratings_fixed_main.csv')
    
    # Load datasets
    data_handler.load_data()
    
    # Build training and test sets
    training_set = data_handler.build_trainset()
    testing_set = data_handler.build_testset()
    
    # Define both algorithms and fit them to the training set
    
    svd_recommender = Recommender(training_set, algorithm_type='SVD')
    svd_recommender.train()

    knn_recommender = Recommender(training_set, algorithm_type='KNNBaseline')
    knn_recommender.train()

    # Test algorithms
    svd_predictions = svd_recommender.predict(testing_set)
    knn_predictions = knn_recommender.predict(testing_set)

    
    # Retrieve top N predictions
    svd_top_recommendations = get_top_n(svd_predictions, n=50)
    knn_top_recommendations = get_top_n(knn_predictions, n=50)
    
    # Update movie and ratings dataframes
    updated_movies_df = data_handler.update_movies()
    updated_ratings_df = data_handler.update_ratings()

