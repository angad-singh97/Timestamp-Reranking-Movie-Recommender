# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:42:52 2020

@author: Angad
"""

data = Dataset.load_from_file('ml-latest-small/ratings_fixed_main.csv', reader=reader)

#data = Dataset.load_builtin('ml-100k')     USE INBUILT DATASET WITH THIS LINE 
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

#
top_n = get_top_n(predictions, n=50)

print("MET 3")

top_n2 = get_top_n(predictions_2, n=50)

#Movies_fixed = pd.read_csv("ml-latest-small/movies_fixed_main.csv",encoding="ISO-8859-1")
#Ratings_fixed = pd.read_csv("ml-latest-small/ratings_fixed_main.csv",encoding="ISO-8859-1")