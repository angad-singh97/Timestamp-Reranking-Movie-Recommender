# utility.py
from collections import defaultdict
import json
import random
from random import sample
from datetime import datetime
from datetime import timedelta
import pandas as pd

def get_top_n(predictions, n=10):

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

def single_prec(recom_list,threshold):
    count = 0
    short_list = recom_list[0:12]
 
    for rl in short_list:
        #print(rl[1])
        if rl[1]>=threshold:
            count = count + 1

    recom_list_size = len(short_list)

    return count/recom_list_size

def single_prec_hybrid(recom_list,threshold):
    count = 0
    short_list = recom_list[0:25]
 
    for rl in short_list:
        #print(rl[1])
        if rl[1]>=threshold:
            count = count + 1

    recom_list_size = len(short_list)

    return count/recom_list_size


def global_prec(user_count,func, top_n):
    
    global_res = 0
    for i in range(1,user_count+1):
        i2 = str(i)
        curr = top_n[i2]
        curr_prec = func(curr,3.5)
        #print(curr_prec)
        global_res = global_res + curr_prec*100
    
    return global_res/user_count

def global_prec2(user_count,func, top_n2):
    
    global_res = 0
    for i in range(1,user_count+1):
        i2 = str(i)
        curr = top_n2[i2]
        curr_prec = func(curr,4)
        #print(curr_prec)
        global_res = global_res + curr_prec*100
    
    return global_res/user_count
#
def global_prec_hybrid(user_count,func, top_n_hybrid):
    
    global_res = 0
    for i in range(1,user_count+1):
        i2 = str(i)
        curr = top_n_hybrid[i2]
        curr_prec = func(curr,3.5)
        #print(curr_prec)
        global_res = global_res + curr_prec*100
    
    return global_res/user_count

def diversity_in_top_n(user_count, top_n):
	global_res = set()
	for i in range(1,user_count+1):
		i2 = str(i)
		curr = top_n[i2]
		for mv in curr[0:5]:
			global_res.add(mv[0])
	return len(global_res)

def diversity_in_top_n2(user_count,top_n2):
	global_res = set()
	for i in range(1,user_count+1):
		i2 = str(i)
		curr = top_n2[i2]
		for mv in curr[0:5]:
			global_res.add(mv[0])
	return len(global_res)
    
#
def diversity_in_top_n_hybrid(user_count, top_n_hybrid):
	global_res = set()
	for i in range(1,user_count+1):
		i2 = str(i)
		curr = top_n_hybrid[i2]
		for mv in curr[0:5]:
			global_res.add(mv[0])
	return len(global_res)



def combine_and_adjust_recommendations(list1, list2, svd_algo):
    """
    Combines two recommendation lists (SVD and KNN), tags them with their origin, 
    and adjusts the KNN recommendations using the SVD model.
    
    Args:
    - list1 (dict): Recommendations from SVD.
    - list2 (dict): Recommendations from KNN.
    - svd_algo (surprise.prediction_algorithms): The SVD algorithm used for predictions.

    Returns:
    - top_n_hybrid (dict): The combined and adjusted recommendations.
    """

    top_n_hybrid = {}

    # Splice the two lists for each user
    for i in range(1, len(list1) + 1):
        user_recommendations = [list(elem) for elem in zip(list1[str(i)], list2[str(i)])]
        top_n_hybrid[str(i)] = user_recommendations

    # Tag each recommendation with its origin: 1 for SVD and 2 for KNN
    for user_id, recommendations in top_n_hybrid.items():
        for idx, recommendation in enumerate(recommendations):
            tag = 1 if idx % 2 == 0 else 2
            recommendation.append(tag)

    # Adjust the KNN predictions using the SVD algorithm
    for user_id, recommendations in top_n_hybrid.items():
        for recommendation in recommendations:
            if recommendation[2] == 2:  # If it's from KNN
                new_pred_val = svd_algo.predict(user_id, recommendation[0], 3.4)
                recommendation[1] = new_pred_val.est
                recommendation[2] = 1  # Adjusting the tag to indicate it's now an SVD prediction

    return top_n_hybrid





def spliceList(lst1, lst2): 
    return [sub[item] for item in range(len(lst2)) 
                      for sub in [lst1, lst2]] 


def display_metrics(model_name, recommendations):
    """
    Prints out precision and diversity metrics for given recommendations.
    Args:
    - model_name (str): Name of the recommendation model (e.g., 'SVD', 'KNN', 'Hybrid').
    - recommendations (dict): Recommendations from the model.
    """
    print(f"Precision of {model_name} Model:", global_prec(len(recommendations)))
    print(f"Diversity in {model_name} Top N:", diversity_in_top_n2(len(recommendations)), "unique items found.")


def sort_list(list1, list2): 
  
    zipped_pairs = zip(list2, list1) 
  
    z = [x for _, x in sorted(zipped_pairs)] 
      
    return z 

'''fix this one's usage - broke while refactoring''' 
def sortByLastRatedDate(recom_list, Movies_fixed):
    
    for i in range(1,611):
        curr_user = str(i)
        
        
        curr_list = recom_list[curr_user]
        
        datesList = []
        for movie in curr_list:
            curr_mv_id = int(movie[0])
            curr_mv_date = Movies_fixed.at[curr_mv_id-1,'LastRated']
            datesList.append(curr_mv_date)
        
        z_list = sort_list(curr_list,datesList)
        
        recom_list[curr_user] = z_list
        
        
def getUserSampleSet():
    users_list = [x for x in range(1,611)]

    sample_range = [x for x in range(45,71)]

    sample_perc = random.sample(sample_range,1)

    sample_count = int((sample_perc[0]/100)*len(users_list))

    sample_users_list = random.sample(users_list,sample_count)
    
    return sample_users_list


def getRatingsRange():
    sample_ratings = [x*0.1 for x in range(10,51,1)]
    
    for i in range(0,len(sample_ratings)):
        sample_ratings[i] = round(sample_ratings[i],1)

def simulateUsageSimple(sample_users_list, top_n_hybrid, my_timestamp):
    userId_list = []
    movieId_list = []
    rating_list = []
    timestamp_list = []
    
    for user in sample_users_list:
        # Retrieve the first 25 recommendations for the given user
        user_recommendations = top_n_hybrid[str(user)][:25]
        
        # Determine a random percentage between 10% and 30%
        percentage_options = list(range(10, 31))
        selected_percentage = random.choice(percentage_options)
        
        # Calculate the number of recommendations to sample based on the selected percentage
        num_to_sample = int((selected_percentage / 100) * len(user_recommendations))
        
        # Randomly sample the determined number of recommendations
        random_recommendation_subset = random.sample(user_recommendations, num_to_sample)

    
        for recommendation in random_recommendation_subset:
            user_id = int(user)
            movie_id = int(recommendation[0])
            rating = float(round(recommendation[1], 1))
        
            userId_list.append(user_id)
            movieId_list.append(movie_id)
            rating_list.append(rating)
            timestamp_list.append(my_timestamp)
                   
    rating_data = {
        "userId_list": userId_list,
        "movieId_list": movieId_list,
        "rating_list": rating_list,
        "timestamp_list": timestamp_list
    }
    return rating_data



def split_list(input_list):
    list_length = len(input_list)
    result_list = []
    quarter_length = int(0.25 * list_length)
    start_pos = 0
    end_pos = quarter_length
    
    for _ in range(4):
        sublist = input_list[start_pos:end_pos]
        result_list.append(sublist)
        start_pos += quarter_length
        end_pos += quarter_length

    return result_list

def simulateUsageSlotBased(sample_users_list, top_n_hybrid, my_timestamp, Movies_fixed):

    timestamps = []
    
    for days in range(0, 28, 7):
        new_datetime = my_timestamp + timedelta(days=days)
        timestamp = datetime.timestamp(new_datetime)
        timestamps.append(timestamp)
        
    top_n_a = {}
    top_n_b = {}
    top_n_c = {}
    top_n_d = {}

    for i in range(1,611):
        curr_user = str(i)
        curr_list = top_n_hybrid[curr_user]
        #I need to sort this by date before the split up
            
        curr_list_split = splitList(curr_list)
            
        top_n_a[curr_user] = curr_list_split[0]
        top_n_b[curr_user] = curr_list_split[1]
        top_n_c[curr_user] = curr_list_split[2]
        top_n_d[curr_user] = curr_list_split[3]
        
    # User IDs from 1 to 610
    user_ids = [x for x in range(1, 611)]
    
    # Random sample percentage (45-70%)
    sample_percentage = random.sample(range(45, 71), 1)[0]
    
    # Calculate sample size based on percentage
    sample_user_count = int((sample_percentage / 100) * len(user_ids))
    
    # Randomly select users
    sampled_users = random.sample(user_ids, sample_user_count)
    
    # Ratings from 1.0 to 5.0 in steps of 0.1
    sample_ratings = [round(x * 0.1, 1) for x in range(10, 51)]
    
    # User IDs from 1 to 200
    sample_users_list = [i for i in range(1, 201)]
        
    userId_list = []
    movieId_list = []
    rating_list = []
    timestamp_list = []
    

    for timestamp in timestamps:
        for user_id in sample_users_list:
            recommended_movies = top_n_d[str(user_id)]#need to loop over a,b,c,d
            
            # Randomly select a sample percentage from 5% to 10%
            sample_percentage = random.sample(range(5, 11), 1)
            sample_count = int((sample_percentage[0] / 100) * len(recommended_movies))
            
            # Randomly sample movies from the recommendations
            sampled_movies = random.sample(recommended_movies, sample_count)
            
            # Limit the number of recommendations to 10
            sampled_movies = recommended_movies[:10]
            
            for movie in sampled_movies:
                push_user_id = int(user_id)
                push_movie_id = int(movie[0])
                push_rating = float(round(movie[1], 1))
                push_timestamp = int(timestamp)
                
                # Append data to lists
                userId_list.append(push_user_id)
                movieId_list.append(push_movie_id)
                rating_list.append(push_rating)
                timestamp_list.append(push_timestamp)
                
                # Update the movie timestamp in Movies_fixed DataFrame
                movie_row_id = push_movie_id - 1
                Movies_fixed.at[movie_row_id, 'timestamp'] = push_timestamp
                
                # Print movie information
                current_rating = round(movie[1], 1)
                print("Movie ID:", movie[0], "Rating:", movie[1], "Rated:", current_rating)
            print(" ")

    
    for user in sample_users_list:
        # Retrieve the first 25 recommendations for the given user
        user_recommendations = top_n_hybrid[str(user)][:25]
        
        # Determine a random percentage between 10% and 30%
        percentage_options = list(range(10, 31))
        selected_percentage = random.choice(percentage_options)
        
        # Calculate the number of recommendations to sample based on the selected percentage
        num_to_sample = int((selected_percentage / 100) * len(user_recommendations))
        
        # Randomly sample the determined number of recommendations
        random_recommendation_subset = random.sample(user_recommendations, num_to_sample)

    
        for recommendation in random_recommendation_subset:
            user_id = int(user)
            movie_id = int(recommendation[0])
            rating = float(round(recommendation[1], 1))
        
            userId_list.append(user_id)
            movieId_list.append(movie_id)
            rating_list.append(rating)
            timestamp_list.append(my_timestamp)
                   
    rating_data = {
        "userId_list": userId_list,
        "movieId_list": movieId_list,
        "rating_list": rating_list,
        "timestamp_list": timestamp_list
    }
    return rating_data


def appendRatings(new_rating_data, existing_ratings):
    appended_ratings = pd.DataFrame.from_dict(new_rating_data)
    appended_ratings.columns = ['userId','movieId','rating','timestamp']
    existing_ratings = existing_ratings.append(appended_ratings,ignore_index=True,sort=False) 
    existing_ratings.to_csv("ratings_fixed_main.csv",index=None,header=True)
    return existing_ratings

def updateExternalTimestamp(my_timestamp):
    datetime_object_write_out = datetime.fromtimestamp(my_timestamp)

    dtobj = datetime_object_write_out.strftime('%Y-%m-%d')
    with open('metadata.txt','r') as json_file:
        json_data = json.load(json_file)

    json_data['lastRatedDate'] = dtobj

    with open('metadata.txt','w') as json_file:
        json.dump(json_data, json_file)

def getLastRatedTimestamp():
    with open('config/metadata.txt','r') as json_file:
        json_data = json.load(json_file)
    datetime_object = datetime.strptime(json_data["lastRatedDate"], '%Y-%m-%d')
    my_timestamp = int(datetime.timestamp(datetime_object))
    return my_timestamp
        
def generate_user_sample(users_list, sample_range):
        sample_perc = random.sample(sample_range, 1)
        sample_count = int((sample_perc[0]/100)*len(users_list))
        return random.sample(users_list, sample_count)
    

def generate_recommendations(user_sample, top_n_hybrid, my_timestamp):
    userId_list = []
    movieId_list = []
    rating_list = []
    timestamp_list = []

    for user in user_sample:
        curr_recom_list = top_n_hybrid[str(user)][0:25]
        sample_range = [x for x in range(10,31)]
        sample_perc = random.sample(sample_range, 1)
        sample_count = int((sample_perc[0]/100)*len(curr_recom_list))  
        sample_recom_list = random.sample(curr_recom_list, sample_count)
        for recom in sample_recom_list:
            userId_list.append(int(user))
            movieId_list.append(int(recom[0]))
            rating_list.append(float(round(recom[1], 1)))
            timestamp_list.append(my_timestamp)

    return userId_list, movieId_list, rating_list, timestamp_list

def create_ratings_dataframe(uid_list, mid_list, r_list, ts_list):
    rating_dict = {
        "userId_list": uid_list,
        "movieId_list": mid_list,
        "rating_list": r_list,
        "timestamp_list": ts_list
    }
    return pd.DataFrame.from_dict(rating_dict)