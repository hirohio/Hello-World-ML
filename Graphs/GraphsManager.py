import csv as csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import sys as sys
import traceback
import Graphs as gph

class GraphsManager:
    def __init__(self,df):
        self.df = df
        self.graphs = gph.Graphs(self.df)

    def accept_command(self):
        while True:
            print("\n******** Command Menu ************")
            print("(h):Histgram Plot.")
            print("(c):Count Plot.")
            print("(p):Point Plot.")
            print("(s):Scatter Plot.")
            print("(b):Box Plot.")
            print("(pair):Pair Plot.")
            print("(cancel):Cancel.")
            print("**********************************\n")
            ans = input("Please input command: ")
            if ans == "h":
                self._invoke_hist_plot()
                break
            elif ans == "c":
                self._invoke_count_plot()
                break
            elif ans == "p":
                self._invoke_point_plot()
                break
            elif ans == "s":
                self._invoke_sctter_plot()
                break
            elif ans == "b":
                self._invoke_box_plot()
                break
            elif ans == "pair":
                self._invoke_pair_plot()
                break
            elif ans == "cancel":
                break
            elif ans == "":
                continue
            else:
                print(ans + " is not supported")
                break

    def _invoke_hist_plot(self):
        while True:
            column = input("Please input coulmn name: ")
            if not column in self.df.columns:
                print(column + " is not exist!!")
                continue
            else:
                self.graphs.hist_plot(column)
                break
    def _invoke_count_plot(self):
        while True:
            column = input("Please input coulmn name: ")
            if not column in self.df.columns:
                print(column + " is not exist!!")
                continue
            else:
                self.graphs.count_plot(column)
                break
    def _invoke_point_plot(self):
        while True:
            column_x = input("Please input column X name: ")
            if not column_x in self.df.columns:
                print(column_x + " is not exist!!")
                continue
            else:
                break

        while True:
            column_y = input("Please input column Y name: ")
            if not column_y in self.df.columns:
                print(column_y + " is not exist!!")
                continue
            else:
                break

        self.graphs.point_plot(column_x,column_y)
    def _invoke_sctter_plot(self):
        while True:
            column_x = input("Please input column X name: ")
            if not column_x in self.df.columns:
                print(column_x + " is not exist!!")
                continue
            else:
                break

        while True:
            column_y = input("Please input column Y name: ")
            if not column_y in self.df.columns:
                print(column_y + " is not exist!!")
                continue
            else:
                break

            self.graphs.scatter_plot(column_x,column_y)
    def _invoke_pair_plot(self):
        self.graphs.pair_plot()

    def _invoke_box_plot(self):
        self.graphs.box_plot()
