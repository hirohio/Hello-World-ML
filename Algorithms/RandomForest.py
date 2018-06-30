import csv as csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

import sys as sys
import traceback


class RandomForestManager:

    def __init__(self,df):
        self._df = df

    def learn(self,column):
        #predict data
        y = self._df[column]
        self._y = y
        #learning data
        X = self._df.drop([column], axis=1)
        self._X = X

        (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.3, random_state=0)

        model = RandomForestClassifier()
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
        params = {  'n_jobs':[-1],
                    'bootstrap': [True],
                    'max_depth': [40],
                    'max_features': ['auto'],
                    'min_samples_leaf': [2],
                    'min_samples_split': [10],
                    'n_estimators': [400]}

        # 評価関数を指定
        #scores = ['accuracy', 'precision', 'recall']
        cv = GridSearchCV(model, params, cv = 10, scoring = 'neg_mean_squared_error', n_jobs=1, refit = True)

        #cv.fit(X_train, y_train)
        cv.fit(X, y)

        self._best_params = cv.best_params_
        self._learned_model = cv.best_estimator_
        print('*----------------*')
        print('|   Best Params  |')
        print('*----------------*')
        print(cv.best_params_)

        self._learned_model = cv


        # print importance of features
        print('*---------------------*')
        print('|  Feature Importance |')
        print('*---------------------*')

        feature_names = X.columns
        importances = cv.best_estimator_.feature_importances_

        for (feature_name, importance) in zip(feature_names, importances):
            print("{0:<20}".format (feature_name), importance)

    def predictII(self,test_df):
        return self._learned_model.predict(test_df).astype(int)

    def predict(self,column,test_df):
        self._y_column = column
        #predict data
        y_df = self._df[self.y_column]

        #learning data
        x_df = self._df.drop([self.y_column], axis=1)
        print("[train data]: \n")
        x_df.info()

        #test Data
        #original_test_df = test_df

        #preprocessing test Data
        #Matching between train_df and test_df
        print("\n" + "preprocesing data")
        for val in test_df.columns:
            if not val in x_df.columns:
                test_df = test_df.drop(val, axis=1)
                print("dropped " + val + " from test data")

        for val in x_df.columns:
            if not val in test_df.columns:
                x_df = x_df.drop(val, axis=1)
                print("dropped " + val + " from train data")

        print("[test data]: \n")
        test_df.info()

        print("Random Forest is learning\n")
        # create 100 Decision Treess(Random Forest)
        model = RandomForestClassifier(n_estimators=100)
        output = model.fit(x_df, y_df).predict(test_df).astype(int)

        return output
