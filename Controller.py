# controller.py
from config import CONFIG
from datahandler import DataHandler
from recommender import Recommender
from utility import get_top_n

class Controller:
    def __init__(self):
        self.datahandler = DataHandler(
            CONFIG['DATA_PATH'], 
            CONFIG['MOVIE_PATH'], 
            CONFIG['RATING_PATH']
        )
        self.recommender = None

    def load_data(self):
        self.datahandler.load_data()

    def train_model(self, algorithm_type=None):
        if not algorithm_type:
            algorithm_type = CONFIG['DEFAULT_ALGORITHM']
        
        trainset = self.datahandler.build_trainset()
        self.recommender = Recommender(trainset, algorithm_type)
        self.recommender.train()

    def get_recommendations(self, n=None):
        if not n:
            n = CONFIG['TOP_N']
        
        testset = self.datahandler.build_testset()
        predictions = self.recommender.predict(testset)
        return get_top_n(predictions, n)

    # more methods - saving model, updating dataset
