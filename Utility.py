# utility.py
from collections import defaultdict
import json
import random
from random import sample
from datetime import datetime
from datetime import timedelta

"""Return the top N recommendations for each user from a set of predictions."""
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