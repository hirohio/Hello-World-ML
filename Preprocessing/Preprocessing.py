import csv as csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Imputer
import sys as sys
import traceback

class Preprocessing:
    def __init__(self, df):
        self.df = df
        self.datetime_kinds = ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']
    def is_column_exist(self, column):
        return column in self.df.columns

    def complement_with_median(self,column):
        #median = self.df[column].dropna().median()
        #self.df[column] = self.df[column].fillna(median)
        #print("This method is not still tested")
        imr = Imputer(missing_values='NaN', strategy='median', axis=0)
        imr = imr.fit(self.df[[column]])
        self.df[column] = imr.transform(self.df[[column]]).ravel()
        return self.df

    def complement_with_mean(self,column):
        imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
        imr = imr.fit(self.df[[column]])
        self.df[column] = imr.transform(self.df[[column]]).ravel()
        return self.df

    def complement_with_mostfrequency(self,column):
        imr = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
        imr = imr.fit(self.df[[column]])
        self.df[column] = imr.transform(self.df[[column]]).ravel()
        return self.df

    def drop(self, column_name):
        try:
            self.df = self.df.drop(column_name, axis=1)
            return self.df
        except:
            print("Unexpected Exception")
            traceback.print_exc()
            sys.exit()

    def drop_nan(self):
        self.df = self.df.dropna(axis=0, how='any')
        return self.df

    # xxxx-xx-xx xx:xx:xx to 0~7
    def convert_time_to_weekdays(self,column_name):
        try:
            self.df[column_name + '_weekday'] = pd.to_datetime(self.df[column_name]).dt.weekday
            self.df.info()
            return self.df
        except:
            print("Unexpected Exception")
            traceback.print_exc()
            sys.exit()

    # xxxx-xx-xx xx:xx:xx to 0~24
    def convert_time_to_datetime(self,column_name,time_name):
        if not time_name in self.datetime_kinds :
            raise(NotSupportedError)

        new_column_name = column_name + '_' + time_name
        exec('self.df[new_column_name] = pd.to_datetime(self.df[column_name]).dt.' + time_name)
        self.df.info()
        return self.df

    def fill_in_NaN(self,column_name,value_name):
        self.df[column_name] = self.df[column_name].fillna(value_name)
        return self.df

    # It is uede for embarked to Int {S:0 C:1 Q:2}
    def convert_object_to_int(self,column_name):
        print(self.df[column_name].value_counts())

        coi_dict = {}
        u = self.df[column_name].unique()
        for i,j in enumerate(u):
            print("convert " + j + ":" + str(i))
            coi_dict[j] = i
        self.df["converted_" + column_name] = self.df[column_name].map(coi_dict).astype(int)

        return self.df

    #正規化するメソッド
    def convert_data_to_nomalized(self,column_name):
        if type(column_name) is not str:
            return False
        mms = MinMaxScaler()
        self.df[column_name] = mms.fit_transform(self.df[column_name])
        return self.df

    #Add two columns
    def sum_columns(self,column_name,column_name2,new_column_name):
        self.df[new_column_name] = self.df[column_name] + self.df[column_name2]
        return self.df

    #convert value to boolean
    def convert_columns_to_boolean(self,column_name,new_column_name,sleshhold):
        self.df[new_column_name] = self.df[column_name].apply(lambda x: 1 if x < sleshhold else 0)
        return self.df

    def delete_outlier(self,column_name,bias):
        q1 = self.df[column_name].quantile(.25)
        q3 = self.df[column_name].quantile(.75)
        iqr = q3 - q1

        outlier_min = q1 - (iqr) * bias
        outlier_max = q3 + (iqr) * bias

        deleted_df = self.df[(outlier_min < self.df[column_name]) & (self.df[column_name] < outlier_max)]
        return deleted_df

class NotSupportedError(Exception):
    pass
