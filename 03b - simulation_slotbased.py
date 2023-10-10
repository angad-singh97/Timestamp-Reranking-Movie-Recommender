# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 00:50:00 2020

@author: Angad


this is the custom simulator


"""

import random
from random import sample
import json

from datetime import datetime
from datetime import timedelta

with open('metadata.txt','r') as json_file:
    json_data = json.load(json_file)
    
datetime_object = datetime.strptime(json_data["lastRatedDate"], '%Y-%m-%d')

my_timestamp = datetime.timestamp(datetime_object)
my_timestamp2 = datetime.timestamp(datetime_object + timedelta(days=7))
my_timestamp3 = datetime.timestamp(datetime_object + timedelta(days=14))
my_timestamp4 = datetime.timestamp(datetime_object + timedelta(days=21))




users_list = [x for x in range(1,611)]

sample_range = [x for x in range(45,71)]

sample_perc = random.sample(sample_range,1)

#print("RANDOM USER PERC",sample_perc)

sample_count = int((sample_perc[0]/100)*len(users_list))

sample_users_list = random.sample(users_list,sample_count)

sample_ratings = [x*0.1 for x in range(10,51,1)]

for i in range(0,len(sample_ratings)):
    sample_ratings[i] = round(sample_ratings[i],1)
    
sample_users_list = [i for i in range(1,201)]

userId_list = []
movieId_list = []
rating_list = []
timestamp_list = []


for user in sample_users_list:
    curr_recom_list = top_n_a[str(user)]
    #now select random movies from this
    #but from where? top 10% - 30%
    sample_range = [x for x in range(5,11)]
    sample_perc = random.sample(sample_range,1)
    #print("RANDOM SAMPLE PERC",sample_perc)
    sample_count = int((sample_perc[0]/100)*len(curr_recom_list))  
    sample_recom_list = random.sample(curr_recom_list,sample_count)
    sample_recom_list = curr_recom_list[0:10]
    #print("USER",user)
    for recom in sample_recom_list:
        
        push_user_id = int(user)
        push_movie_id = int(recom[0])
        push_rating = float(round(recom[1],1))
        push_timestamp = int(my_timestamp)
        
        userId_list.append(push_user_id)
        movieId_list.append(push_movie_id)
        rating_list.append(push_rating)
        timestamp_list.append(push_timestamp)
        curr_rating=round(recom[1],1)
        
        #we also need to update this movie's last rated date
        
        mv_row_id = push_movie_id-1
        Movies_fixed.at[mv_row_id,3] = datetime.strftime(datetime.fromtimestamp(push_timestamp),"%Y-%m-%d")
        
        curr_rating = random.sample(sample_ratings,1)[0]
        print("Movie ID ",recom[0]," Rating ",recom[1]," Rated ",curr_rating)
    print(" ")

for user in sample_users_list:
    curr_recom_list = top_n_b[str(user)]
    #now select random movies from this
    #but from where? top 10% - 30%
    sample_range = [x for x in range(5,11)]
    sample_perc = random.sample(sample_range,1)
    #print("RANDOM SAMPLE PERC",sample_perc)
    sample_count = int((sample_perc[0]/100)*len(curr_recom_list))  
    sample_recom_list = random.sample(curr_recom_list,sample_count)
    sample_recom_list = curr_recom_list[0:10]
    #print("USER",user)
    for recom in sample_recom_list:
        
        push_user_id = int(user)
        push_movie_id = int(recom[0])
        push_rating = float(round(recom[1],1))
        push_timestamp = int(my_timestamp2)
        
        userId_list.append(push_user_id)
        movieId_list.append(push_movie_id)
        rating_list.append(push_rating)
        timestamp_list.append(push_timestamp)
        curr_rating=round(recom[1],1)
        mv_row_id = push_movie_id-1
        Movies_fixed.at[mv_row_id,3] = push_timestamp
        print("Movie ID ",recom[0]," Rating ",recom[1]," Rated ",curr_rating)
    print(" ")

for user in sample_users_list:
    curr_recom_list = top_n_c[str(user)]
    #now select random movies from this
    #but from where? top 10% - 30%
    sample_range = [x for x in range(5,11)]
    sample_perc = random.sample(sample_range,1)
    #print("RANDOM SAMPLE PERC",sample_perc)
    sample_count = int((sample_perc[0]/100)*len(curr_recom_list))  
    sample_recom_list = random.sample(curr_recom_list,sample_count)
    sample_recom_list = curr_recom_list[0:10]
    #print("USER",user)
    for recom in sample_recom_list:
        
        push_user_id = int(user)
        push_movie_id = int(recom[0])
        push_rating = float(round(recom[1],1))
        push_timestamp = int(my_timestamp3)
        
        userId_list.append(push_user_id)
        movieId_list.append(push_movie_id)
        rating_list.append(push_rating)
        timestamp_list.append(push_timestamp)
        curr_rating=round(recom[1],1)
        mv_row_id = push_movie_id-1
        Movies_fixed.at[mv_row_id,3] = push_timestamp
        print("Movie ID ",recom[0]," Rating ",recom[1]," Rated ",curr_rating)
    print(" ")

for user in sample_users_list:
    curr_recom_list = top_n_d[str(user)]
    #now select random movies from this
    #but from where? top 10% - 30%
    sample_range = [x for x in range(5,11)]
    sample_perc = random.sample(sample_range,1)
    #print("RANDOM SAMPLE PERC",sample_perc)
    sample_count = int((sample_perc[0]/100)*len(curr_recom_list))  
    sample_recom_list = random.sample(curr_recom_list,sample_count)
    sample_recom_list = curr_recom_list[0:10]
    #print("USER",user)
    for recom in sample_recom_list:
        
        push_user_id = int(user)
        push_movie_id = int(recom[0])
        push_rating = float(round(recom[1],1))
        push_timestamp = int(my_timestamp4)
        
        userId_list.append(push_user_id)
        movieId_list.append(push_movie_id)
        rating_list.append(push_rating)
        timestamp_list.append(push_timestamp)
        curr_rating=round(recom[1],1)
        mv_row_id = push_movie_id-1
        Movies_fixed.at[mv_row_id,3] = push_timestamp
        print("Movie ID ",recom[0]," Rating ",recom[1]," Rated ",curr_rating)
    print(" ")


        
ratingDict2 = {}

ratingDict2["userId_list"] = userId_list
ratingDict2["movieId_list"] = movieId_list
ratingDict2["rating_list"] = rating_list
ratingDict2["timestamp_list"] = timestamp_list

appended_ratings2 = pd.DataFrame.from_dict(ratingDict2)

#Ratings_fixed=pd.read_csv("ml-latest-small/ratings_fixed_main.csv",encoding="ISO-8859-1")
appended_ratings2.columns = ['userId','movieId','rating','timestamp']
Ratings_fixed = Ratings_fixed.append(appended_ratings2,ignore_index=True,sort=False) 

Ratings_fixed.to_csv("ml-latest-small/ratings_fixed_main.csv",index=None,header=True)
Movies_fixed.to_csv("ml-latest-small/movies_fixed_main.csv")



datetime_object_write_out = datetime.fromtimestamp(my_timestamp4)

dtobj = datetime_object_write_out.strftime('%Y-%m-%d')

json_data['lastRatedDate'] = dtobj

with open('metadata.txt','w') as json_file:
    json.dump(json_data, json_file)