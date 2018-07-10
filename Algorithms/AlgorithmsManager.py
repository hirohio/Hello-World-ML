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

import sys as sys
import traceback
import Algorithms.RandomForest as randforest
import Algorithms.Deeplearning as deeplearning
import Algorithms.VotingClassifier as votingclassfier
import IOFiles.IOFileManager as iof

class AlgorithmsManager:

    def __init__(self,df):
        self._df = df

    @property
    def df(self):
        return self._df

    def accept_command(self):
        while True:
            print("\n******** Command Menu ************")
            print("(r):RandomForest (ensemble)")
            print("(d):DeepLearning")
            print("(v):VotingClassfier (ensemble)")
            print("(c):Cancel")
            print("**********************************\n")
            ans = input("Please input command: ")
            if ans == "r":
                self._invoke_random_forest()
                break
            elif ans == "d":
                self._invoke_deep_learning()
                break
            elif ans == "v":
                self._invoke_voting_classfier()
            elif ans == "cancel":
                break
            elif ans == "":
                continue

    def _invoke_random_forest(self):
        print("Following data is referd for training")
        self._df.info()
        rf = randforest.RandomForestManager(self._df)

        while True:
            prediction_column = input("Input column you want to predict: ")
            if(prediction_column in self._df.columns):
                break

        print("Test file is required.")
        io_file = iof.IOFileManager()
        test_df = io_file.import_from_csv()

        rf.learn(prediction_column)
        output_df = rf.predictII(test_df)
        #output_df = rf.predict(prediction_column,test_df)

        print("Exporting File\n")
        io_file.export_output(test_df,output_df,prediction_column)

    def _invoke_deep_learning(self):
        print("Following data is referd for training")
        self._df.info()
        dl = deeplearning.DeepLearningManager(self._df)

        while True:
            prediction_column = input("Input column you want to predict: ")
            if(prediction_column in self._df.columns):
                break

        while True:
            #最適化手法
            solver = input("Input solver you want to use:('lbfgs', 'sgd', 'adam'): ")
            break

            if solver == "lbfgs":
                break
            elif solver == "sgd":
                break
            elif solver == "adam":
                break
            elif solver == "":
                continue
            else:
                print(solver + " is not existed.")
                continue

        while True:
            #活性化関数
            activation = input("Input activation you want to use:(‘identity’, ‘logistic’, ‘tanh’, ‘relu’): ")
            if activation == "identity":
                break
            elif activation == "logistic":
                break
            elif activation == "tanh":
                break
            elif activation == "relu":
                break
            elif activation == "":
                continue
            else:
                print(activation + " is not existed.")
                continue

        print("Test file is required.")
        io_file = iof.IOFileManager()
        test_df = io_file.import_from_csv()
        output_df = dl.predict(prediction_column,test_df, solver, activation)

        print("Exporting File\n")
        io_file.export_output(test_df,output_df,prediction_column)

    def _invoke_voting_classfier(self):
        print("Following data is referd for training")
        self._df.info()
        vc = votingclassfier.VotingClassifierManager(self._df)

        while True:
            prediction_column = input("Input column you want to predict: ")
            if(prediction_column in self._df.columns):
                break

        print("Test(Target) file is required.")
        io_file = iof.IOFileManager()
        test_df = io_file.import_from_csv()

        vc.learn(prediction_column)
