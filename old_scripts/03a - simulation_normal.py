# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:49:31 2020

@author: Angad
"""

"""
THIS IS MY REGULAR SIMULATOR


"""
import random
from random import sample
from datetime import datetime
from datetime import timedelta
import json

with open('metadata.txt','r') as json_file:
    json_data = json.load(json_file)
    
datetime_object = datetime.strptime(json_data["lastRatedDate"], '%Y-%m-%d')

my_timestamp = int(datetime.timestamp(datetime_object + timedelta(days=7)))





    

users_list = [x for x in range(1,611)]

sample_range = [x for x in range(45,71)]

sample_perc = random.sample(sample_range,1)

sample_count = int((sample_perc[0]/100)*len(users_list))

sample_users_list = random.sample(users_list,sample_count)

sample_ratings = [x*0.1 for x in range(10,51,1)]

sample_users_list = [i for i in range(1,201)]

for i in range(0,len(sample_ratings)):
    sample_ratings[i] = round(sample_ratings[i],1)

userId_list = []
movieId_list = []
rating_list = []
timestamp_list = []

for user in sample_users_list:
    curr_recom_list = top_n_hybrid[str(user)][0:25]
    #now select random movies from this
    #but from where? top 10% - 30%
    sample_range = [x for x in range(10,31)]
    sample_perc = random.sample(sample_range,1)
    sample_count = int((sample_perc[0]/100)*len(curr_recom_list))  
    sample_recom_list = random.sample(curr_recom_list,sample_count)
    sample_recom_list = curr_recom_list[0:10]
    print(user)
    for recom in sample_recom_list:
        
        push_user_id = int(user)
        push_movie_id = int(recom[0])
        push_rating = float(round(recom[1],1))
        push_timestamp = my_timestamp
        
        userId_list.append(push_user_id)
        movieId_list.append(push_movie_id)
        rating_list.append(push_rating)
        timestamp_list.append(push_timestamp)
        curr_rating=round(recom[1],1)
        #curr_rating = random.sample(sample_ratings,1)[0]
        print("Movie ID ",recom[0]," Rating ",recom[1]," Rated ",curr_rating)
    print(" ")
        
ratingDict = {}

ratingDict["userId_list"] = userId_list
ratingDict["movieId_list"] = movieId_list
ratingDict["rating_list"] = rating_list
ratingDict["timestamp_list"] = timestamp_list

appended_ratings = pd.DataFrame.from_dict(ratingDict)
appended_ratings.columns = ['userId','movieId','rating','timestamp']
Ratings_fixed = Ratings_fixed.append(appended_ratings,ignore_index=True,sort=False) 

Ratings_fixed.to_csv("ratings_fixed_main.csv",index=None,header=True)



datetime_object_write_out = datetime.fromtimestamp(my_timestamp)

dtobj = datetime_object_write_out.strftime('%Y-%m-%d')

json_data['lastRatedDate'] = dtobj

with open('metadata.txt','w') as json_file:
    json.dump(json_data, json_file)