import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import VotingClassifier

class VotingClassifier:

    def __init__(self,df):
        self._df = df

    @property
    def df(self):
        return self._df

    def learn(self,column):
        return False

    def predict(self,test_df):
        return self._learned_model.predict(test_df).astype(int)
