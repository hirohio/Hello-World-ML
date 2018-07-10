import csv as csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import Algorithms.Utilities.NumChecker as aun
import sys as sys
import traceback

class RandomForestManager:

    def __init__(self,df):
        self._df = df

    def learn(self,column,params):
        if aun.NumChecker.is_df_num(self._df) is False:
            return False

        #predict data
        y = self._df[column]
        self._y = y

        #learning data
        X = self._df.drop([column], axis=1)
        self._X = X

        (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.3, random_state=0)

        model = RandomForestClassifier()

        print('*-----------------------------*')
        print('|        Default Params       |')
        print('*-----------------------------*')
        print(model.get_params())

        print('*-----------------------------*')
        print('|        Read File Params     |')
        print('*-----------------------------*')
        print(params)

        # 評価関数を指定
        #scores = ['accuracy', 'precision', 'recall']
        print('...Doing Grid Search...')
        cv = GridSearchCV(model, params, cv = 10, scoring = 'neg_mean_squared_error', n_jobs=1, refit = True)

        cv.fit(X_train, y_train)

        self._best_params = cv.best_params_
        self._learned_model = cv.best_estimator_
        print('*-----------------------------*')
        print('|          Best Params        |')
        print('*-----------------------------*')
        print(cv.best_params_)

        self._learned_model = cv

        # print importance of features
        print('*-----------------------------*')
        print('|      Feature Importance     |')
        print('*-----------------------------*')
        feature_names = X_train.columns
        importances = cv.best_estimator_.feature_importances_

        for (feature_name, importance) in zip(feature_names, importances):
            print("{0:<20}".format (feature_name), importance)

        # Accuracy Score
        print('...Predicting Test Data...')
        predicted_result = self._learned_model.predict(X_test).astype(int)

        print('*-----------------------------*')
        print('|        Accuracy Score       |')
        print('*-----------------------------*')
        print(accuracy_score(y_test,predicted_result))

        return True

    def predict(self,test_df):
        return self._learned_model.predict(test_df).astype(int)
