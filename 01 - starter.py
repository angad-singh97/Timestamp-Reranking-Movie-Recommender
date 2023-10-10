from __future__ import (absolute_import, division, print_function,unicode_literals)
import surprise
from surprise import Dataset
from surprise import Reader
from surprise import KNNBaseline
from surprise import accuracy
from collections import defaultdict
from surprise import SVD
import pandas as pd
import numpy as np
import math
from surprise.model_selection import train_test_split
from datetime import datetime
from datetime import *


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




reader = Reader(line_format='user item rating timestamp', sep=',', rating_scale=(1, 5), skip_lines=1)
data = Dataset.load_from_file('ml-latest-small/ratings_fixed.csv', reader=reader)

#data = Dataset.load_builtin('ml-100k')     #USE INBUILT DATASET WITH THIS LINE 
trainset = data.build_full_trainset()
algo = SVD()
algo.fit(trainset)

algo_2 = KNNBaseline()
algo_2.fit(trainset)


print("MET 1")

# Than predict ratings for all pairs (u, i) that are NOT in the training set.
testset = trainset.build_anti_testset()
predictions = algo.test(testset)
predictions_2 = algo_2.test(testset)

print("MET 2")


top_n = get_top_n(predictions, n=50)

print("MET 3")

top_n2 = get_top_n(predictions_2, n=50)



