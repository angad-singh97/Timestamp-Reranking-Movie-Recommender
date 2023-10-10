# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:42:06 2019

@author: Angad
"""

import pandas as pd
from datetime import datetime
import time


temp_movies = pd.read_csv('ml-latest-small/movies_fixed.csv')

for u in range(0,9742):
    curr_mv_date = temp_movies.iloc[u,3]
    if(curr_mv_date == "1970-01-01"):
        curr_mv_date = "1970-10-01"
    print(type(curr_mv_date))
    print(curr_mv_date)
    datetime_object = datetime.strptime(curr_mv_date, '%Y-%m-%d')
    print(datetime_object)
    my_timestamp = datetime.timestamp(datetime_object)
    print(my_timestamp)
    temp_movies.at[u,'LastRated'] = int(my_timestamp)

temp_movies.to_csv("ml-latest-small/movies_fixed.csv",index=None,header=True)
    