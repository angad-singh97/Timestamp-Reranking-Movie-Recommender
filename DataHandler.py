from surprise import Dataset, Reader
import pandas as pd

class DataHandler:
    def __init__(self, data_path, movie_path, rating_path):
        self.reader = Reader(line_format='user item rating timestamp', sep=',', rating_scale=(1, 5), skip_lines=1)
        self.data_path = data_path
        self.movie_path = movie_path
        self.rating_path = rating_path
        self.data = None
        self.trainset = None
        self.testset = None
        self.Movies_fixed = None
        self.Ratings_fixed = None

    def load_data(self):
        """Load the data from file."""
        self.data = Dataset.load_from_file(self.data_path, reader=self.reader)

    def build_trainset(self):
        """Construct the full trainset."""
        if not self.data:
            self.load_data()
        self.trainset = self.data.build_full_trainset()
        return self.trainset

    def build_testset(self):
        """Construct the testset."""
        if not self.trainset:
            self.build_trainset()
        self.testset = self.trainset.build_anti_testset()
        return self.testset

    def update_movies(self, df=None):
        """Update the Movies_fixed dataframe."""
        if df:
            self.Movies_fixed = df
        else:
            self.Movies_fixed = pd.read_csv(self.movie_path, encoding="ISO-8859-1")
        return self.Movies_fixed

    def update_ratings(self, df=None):
        """Update the Ratings_fixed dataframe."""
        if df:
            self.Ratings_fixed = df
        else:
            self.Ratings_fixed = pd.read_csv(self.rating_path, encoding="ISO-8859-1")
        return self.Ratings_fixed
# -*- coding: utf-8 -*-

