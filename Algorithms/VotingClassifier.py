import csv as csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import VotingClassifier

import sys as sys
import traceback


class VotingClassifierManager:

    def __init__(self,df):
        self._df = df

    @property
    def df(self):
        return self._df

    def learn(self,column):
        return False

    def predict(self,test_df):
        return self._learned_model.predict(test_df).astype(int)
