# controller.py
from config import CONFIG
from datahandler import DataHandler
from recommender import Recommender
from utility import *

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
    
    
    combined_recommendations = combine_and_adjust_recommendations(svd_top_recommendations, knn_top_recommendations, svd_recommender)
    
    #get initial metric data
    display_metrics("Early SVD", svd_recommendations)
    display_metrics("Early KNN", knn_recommendations)
    display_metrics("Early Hybrid", hybrid_recommendations)

    
    sortByLastRatedDate(svd_top_recommendations)
    sortByLastRatedDate(knn_top_recommendations)
    sortByLastRatedDate(combined_recommendations)
    
    #simulation of users, recompute model, then re-run metrics
    lastRatedTimestamp = getLastRatedTimestamp()
    
    next_timestamp = int(datetime.timestamp(lastRatedTimestamp + timedelta(days=7)))
    
    sampleUserSet = getUserSampleSet()
    
    ratingsRange = getRatingsRange()
    
    
    
    

    
    
    
    #repeat n-times
    
    
    
    top_n_hybrid_sorted = {}
    #todo - likely need to pass to datahandler
    Movies_fixed=pd.read_csv("ml-latest-small/movies_fixed.csv",encoding="ISO-8859-1")
    Ratings_fixed=pd.read_csv("ml-latest-small/ratings_fixed.csv",encoding="ISO-8859-1")
        

