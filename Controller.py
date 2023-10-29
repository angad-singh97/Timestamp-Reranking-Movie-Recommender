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
    
    run_simulation()

    
    def run_simulation(self, sample_users_list, top_n_hybrid, iterations):
        choice = input("Choose simulation type: \n1. Simple Usage Simulation \n2. Slot-based Usage Simulation\n")
        
        if choice == "1":
            self.simple_usage_simulation(sample_users_list, top_n_hybrid, iterations)
        elif choice == "2":
            self.slot_based_simulation(sample_users_list, top_n_hybrid, iterations)
        else:
            print("Invalid choice! Please select 1 or 2.")
    
    def simple_usage_simulation(self,sample_users_list, top_n_hybrid, iterations):
        for i in range(iterations):
            # Your logic or code to run during each iteration
            print(f"Iteration number {i + 1}")
            
            #simulation of users, recompute model, then re-run metrics
            lastRatedTimestamp = getLastRatedTimestamp()
            
            next_timestamp = int(datetime.timestamp(lastRatedTimestamp + timedelta(days=7)))
            
            sampleUserSet = getUserSampleSet()
            
            ratingsRange = getRatingsRange()
            
            simulateUsageSimple(sample_users_list, top_n_hybrid, next_timestamp)
            
            display_metrics("SVD, Iteration {i+1}", svd_recommendations)
            display_metrics("KNN, Iteration {i+1}", knn_recommendations)
            display_metrics("Hybrid, Iteration {i+1}", hybrid_recommendations)


    
    def slot_based_simulation(self, sample_users_list, top_n_hybrid, iterations):
        for i in range(iterations):
            # Your logic or code to run during each iteration
            print(f"Iteration number {i + 1}")
            
            #simulation of users, recompute model, then re-run metrics
            lastRatedTimestamp = getLastRatedTimestamp()
            
            next_timestamp = int(datetime.timestamp(lastRatedTimestamp + timedelta(days=7)))
            
            sampleUserSet = getUserSampleSet()
            
            ratingsRange = getRatingsRange()
            
            simulateUsageSlotBased(sample_users_list, top_n_hybrid, next_timestamp)
            
            display_metrics("SVD, Iteration {i+1}", svd_recommendations)
            display_metrics("KNN, Iteration {i+1}", knn_recommendations)
            display_metrics("Hybrid, Iteration {i+1}", hybrid_recommendations)
            

