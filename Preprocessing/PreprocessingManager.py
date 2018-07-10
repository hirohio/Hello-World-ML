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

import Preprocessing as prep

class PreprocessingManager:

    def __init__(self, df):
        self.df = df
        self.pp = prep.Preprocessing(self.df)

    def accept_command(self):
        while True:
            print("\n******** Command Menu ************")
            print("(d):Drop columns.")
            print("(median):Complete with median.")
            print("(mean):Complete with mean.")
            print("(most frequent);Complerte with most frequent")
            print("(tw): Time to weekday.")
            print("(td): Time to datetime.")
            print("(n): Nomilize data")
            print("(f): fill in NaN data with value")
            print("(coi): convert objects to int")
            print("(cib): covnert int to boolean")
            print("(s): sum two columns")
            print("(del outlier): delete outlier")
            print("(cancel): Cancel.")
            print("**********************************\n")
            ans = input("Please input command: ")
            if ans == "d":
                return self._invoke_drop()
            elif ans == "median":
                return self._invoke_complement_with_median()
            elif ans == "mean":
                return self._invoke_complement_with_mean()
            elif ans == "most frequent":
                return self._invoke_complement_with_mostfrequency()
            elif ans == "tw":
                return self._invoke_convert_time_to_weekdays()
            elif ans == "td":
                return self._invoke_convert_time_to_datetime()
            elif ans == "n":
                return self._invoke_convert_nomalize()
            elif ans == "f":
                return self._invoke_fill_in_NaN()
            elif ans == "coi":
                return self._invoke_convert_object_to_int()
            elif ans == "s":
                return self._invoke_sum_columns()
            elif ans == "cib":
                return self._invoke_convert_columns_to_boolean()
            elif ans == "del outlier":
                return self._invoke_delete_outlier()
            elif ans == "cancel":
                return self.df
            elif ans == "":
                continue
            else:
                print(ans + " is not a supported command!\n")
                continue
    def _invoke_complement_with_median(self):
        while True:
            column = input("Plese input column name: ")
            if not column in self.df.columns:
                print(column + " is not exist!!")
                continue
            else:
                return self.pp.complement_with_median(column)
    def _invoke_complement_with_mean(self):
        while True:
            column = input("Plese input column name: ")
            if not column in self.df.columns:
                print(column + " is not exist!!")
                continue
            else:
                return self.pp.complement_with_mean(column)
    def _invoke_complement_with_mostfrequency(self):
        while True:
            column = input("Plese input column name: ")
            if not column in self.df.columns:
                print(column + " is not exist!!")
                continue
            else:
                return self.pp.complement_with_mostfrequency(column)

    def _invoke_drop(self):
        while True:
            ans = input("Please input coulmn name or NaN: ")
            if ans == "NaN":
                return self.pp.drop_nan()
            elif ans == "":
                continue
            elif not self.pp.is_column_exist(ans):
                print(ans + " is not exist!!")
                continue
            else:
                return self.pp.drop(ans)

    def _invoke_convert_time_to_weekdays(self):
        while True:
            ans = input("Please input column name you want to convert to weekday: ")
            if not self.pp.is_column_exist(ans):
                print(ans + "is not exist!!")
                continue
            else:
                return self.pp.convert_time_to_weekdays(ans)


    def _invoke_convert_time_to_datetime(self):
        while True:
            ans = input("Please input column name you want to convert to datetime: ")
            if not self.pp.is_column_exist(ans):
                print(ans + " is not exist!!")
                continue
            else:
                #show list options of 1 line.
                tmp_df = self.df.iloc[:1,]
                print("\n******** Command Menu ************")
                print("original data: ", tmp_df[ans].values)
                print("year: (ex),",pd.to_datetime(tmp_df[ans]).dt.year.values)
                print("month:(ex),",pd.to_datetime(tmp_df[ans]).dt.month.values)
                print("day: (ex),",pd.to_datetime(tmp_df[ans]).dt.day.values)
                print("hour: (ex),",pd.to_datetime(tmp_df[ans]).dt.hour.values)
                print("minute: (ex),",pd.to_datetime(tmp_df[ans]).dt.minute.values)
                print("second; (ex),",pd.to_datetime(tmp_df[ans]).dt.second.values)
                print("microsecond (ex),",pd.to_datetime(tmp_df[ans]).dt.microsecond.values)
                print("**********************************\n")
                break

        while True:
            try:
                print("Please input one of following instructions.")
                ans_time = input("year, month, day, hour, minute, second, microsecond, (c):Cancel :")
                if ans_time == "c":
                    return self.df
                else:
                    return  self.pp.convert_time_to_datetime(ans,ans_time)
            except prep.NotSupportedError:
                print(ans + " is not supported!!")
                continue

    def _invoke_convert_nomalize(self):
        while True:
            ans = input("Please input column name you want to convert to datetime: ")
            if not self.pp.is_column_exist(ans):
                print(ans + " is not exist!!")
                continue
            else:
                return self.pp.convert_data_to_nomalized(ans)

    def _invoke_fill_in_NaN(self):
        while True:
            ans = input("Please input column name you want to fill in: ")
            if not self.pp.is_column_exist(ans):
                print(ans + " is not exist!!")
                continue
            else:
                break
        while True:
            print(self.df[ans].value_counts())
            ans_value = input("Please input value name you want to fill in NaN: ")
            if not ans_value in self.df[ans].unique():
                print(ans_value + " is not exist!!")
                continue
            else:
                return self.pp.fill_in_NaN(ans,ans_value)

    def _invoke_convert_object_to_int(self):
        while True:
            ans = input("Please input column name you want to convert to string from object: ")
            if not self.pp.is_column_exist(ans):
                print(ans + " is not exist!!")
                continue
            else:
                return self.pp.convert_object_to_int(ans)

    def _invoke_sum_columns(self):
        while True:
            print(self.df.columns)
            column_name = input("Please input 1st column name you want to Add: ")
            if not column_name in self.df.columns:
                print(column_name + " is not existed!!")
                continue

            column_name2 = input("Please input 2nd column name you want to Add: ")
            if not column_name2 in self.df.columns:
                print(column_name2 + " is not existed!!")
                continue

            new_column_name = input("Please input new column name you want to create: ")
            if new_column_name in self.df.columns:
                print(new_column_name + " is existed!!")
                continue
            return self.pp.sum_columns(column_name,column_name2,new_column_name)

    def _invoke_convert_columns_to_boolean(self):
        while True:
            print(self.df.columns)
            column_name = input("Please input column name you want to convert: ")
            if not column_name in self.df.columns:
                print(column_name + " is not exist!!")
                continue
            new_column_name = input("Please input new column name you want to create: ")
            if new_column_name in self.df.columns:
                print(new_column_name + " is existed!!")
                continue
            sleshhold = input("Please input sleshhold value: ")
            return self.pp.convert_columns_to_boolean(column_name,new_column_name,int(sleshhold))

    def _invoke_delete_outlier(self):
        while True:
            self.df.info()
            column_name = input("Please input column name you want to delete when it is ourlier: ")
            if not column_name in self.df.columns:
                print(column_name + " is not existed!!")
                continue
            else:
                break
        while True:
            bias = input("Please input bias(e.g, 1.5). Default value is 1.5: ")
            if bias is "":
                print("bias is default value(1.5)")
                bias = 1.5
                break
            else:
                break

        return self.pp.delete_outlier(column_name,float(bias))
