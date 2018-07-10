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
        #predict data
        y = self._df[column]
        self._y = y
        #learning data
        X = self._df.drop([column], axis=1)
        self._X = X

        (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.3, random_state=0)

        model = VotingClassifier()
        #model.fit(X_train, y_train)
        print('*----------------*')
        print('| Default Params |')
        print('*----------------*')
        print(model.get_params())
        #parameterの指定
        '''
        params = {  'n_jobs':[-1],
                    'bootstrap': [True, False],
                    'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],
                    'max_features': ['auto', 'sqrt'],
                    'min_samples_leaf': [1, 2, 4],
                    'min_samples_split': [2, 5, 10],
                    'n_estimators': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]}
        '''
        '''
        params = {  'n_jobs':[-1],
                    'bootstrap': [True],
                    'max_depth': [40],
                    'max_features': ['auto'],
                    'min_samples_leaf': [2],
                    'min_samples_split': [10],
                    'n_estimators': [400],
                    'criterion':['gini','entropy'],
                    'max_leaf_nodes':[10,100],
                    'oob_score':[True, False],
                    'min_weight_leaf':[1,50,100],
                    'min_weight_fraction_leaf':[1,50,100],
                    'min_impurity_decrease':[1,50,100],
                    'random_state':[1,50,100],
                    'verbose',
                    'warm_start':[True, False],
                    'class_weight'
                    }
        '''
        '''
        params = {  'n_jobs':[-1],
                    'bootstrap': [True],
                    'max_depth': [40],
                    'max_features': ['auto'],
                    'min_samples_leaf': [2],
                    'min_samples_split': [10],
                    'n_estimators': [400]}
        '''
        # 評価関数を指定
        #scores = ['accuracy', 'precision', 'recall']
        #cv = GridSearchCV(model, params, cv = 10, scoring = 'neg_mean_squared_error', n_jobs=1, refit = True)

        #cv.fit(X, y)
        #self._best_params = cv.best_params_
        #self._learned_model = cv.best_estimator_
        print('*----------------*')
        print('|   Best Params  |')
        print('*----------------*')
        #print(cv.best_params_)

        #self._learned_model = cv


        # print importance of features
        print('*---------------------*')
        print('|  Feature Importance |')
        print('*---------------------*')

        feature_names = X.columns
        #importances = cv.best_estimator_.feature_importances_

        #for (feature_name, importance) in zip(feature_names, importances):
        #    print("{0:<20}".format (feature_name), importance)

    def predict(self,test_df):
        return self._learned_model.predict(test_df).astype(int)
