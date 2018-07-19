import csv as csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys as sys
import traceback

from scipy import stats
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Imputer

class Preprocessing:
    """Preprocessing Class.

    """

    def __init__(self, df):
        self.df = df
        self.datetime_kinds = ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']

    def complement_with_median(self,column):
        """Complete 'NaN' data with median.

        This method completes 'NaN' data with median.

        Args:
            column (str): column name you want to fill.

        Returns:
            Dataframe: dataframe which is filled with median.
        """
        #median = self.df[column].dropna().median()
        #self.df[column] = self.df[column].fillna(median)
        #print("This method is not still tested")
        imr = Imputer(missing_values='NaN', strategy='median', axis=0)
        imr = imr.fit(self.df[[column]])
        self.df[column] = imr.transform(self.df[[column]]).ravel()
        return self.df

    def complement_with_mean(self,column):
        """Complete 'NaN' data with mean.

        This method completes 'NaN' data with mean.

        Args:
            column (str): column name you want to fill.

        Returns:
            Dataframe: dataframe which is filled with mean.
        """
        imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
        imr = imr.fit(self.df[[column]])
        self.df[column] = imr.transform(self.df[[column]]).ravel()
        return self.df

    def complement_with_mostfrequency(self,column):
        """Complete 'NaN' data with most frequency value.

        Args:
            column (str): column name you want to fill.

        Returns:
            Dataframe: dataframe which is filled with most frequency value.
        """
        imr = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
        imr = imr.fit(self.df[[column]])
        self.df[column] = imr.transform(self.df[[column]]).ravel()
        return self.df

    def drop(self, column):
        """Drop column

        Args:
            column(str): column you want to drop

        Returns:
            Dataframe: Dataframe which is dropped column.
        """
        try:
            self.df = self.df.drop(column, axis=1)
        except:
            print("Unexpected Exception")
            traceback.print_exc()
            sys.exit()
        return self.df

    def drop_nan(self):
        """Drop all 'NaN' rows.

        Returns:
            Dataframe: Dataframe which is removed all NaN rows.
        """
        self.df = self.df.dropna(axis=0, how='any')
        return self.df

    # xxxx-xx-xx xx:xx:xx to 0~7
    def convert_time_to_weekdays(self,column):
        """Convert time to weekdays.
        This method covnerts time to weekdays(0,1,2,3,4,5,6).

        Args:
            column(str): column you want to convert.
        Returns:
            Dataframe: dataframe with converted time to weekdays value(0: Monday - 6: Sunday).

        Examples:
            original data : ['2017-11-07 09:30:38']


        """
        try:
            self.df[column + '_weekday'] = pd.to_datetime(self.df[column]).dt.weekday
            self.df.info()
        except:
            print("Unexpected Exception")
            traceback.print_exc()
            sys.exit()
        return self.df

    # xxxx-xx-xx xx:xx:xx to 0~24
    def convert_time_to_datetime(self,column,time_kind):
        """Convert time to date time.

        Args:
            column (str): column you want to convert.

        Returns:
            Dataframe: dataframe with converted time to time.

        Examples:
            original data : ['2017-11-07 09:30:38']

            year: (ex),[2017]
            month:(ex),[11]
            day: (ex),[7]
            hour: (ex),[9]
            minute: (ex),[30]
            second; (ex),[38]
            microsecond (ex),[0]
        """
        if not time_kind in self.datetime_kinds :
            raise(NotSupportedError)

        new_column_name = column + '_' + time_kind
        exec('self.df[new_column_name] = pd.to_datetime(self.df[column_name]).dt.' + time_kind)
        self.df.info()
        return self.df

    def fill_in_NaN(self,column,value):
        """Fill in 'NaN' values in column with value.

        Args:
            column (str): column name.
            value :value you want to fill in NaN with.

        Returns:
            Dataframe: dataframe.

        """
        self.df[column] = self.df[column].fillna(value)
        return self.df

    # It is uede for embarked to Int {S:0 C:1 Q:2}
    def convert_object_to_int(self,column):
        """Convert string(object) to integer in column.

        Args:
            column (str): column name.

        Returns:
            Dataframe: dataframe with converted column.

        Examples:
            S:0
            C:1
            Q:2
        """
        print(self.df[column].value_counts())

        coi_dict = {}
        u = self.df[column].unique()
        for i,j in enumerate(u):
            print("convert " + j + ":" + str(i))
            coi_dict[j] = i
        self.df["converted_" + column] = self.df[column].map(coi_dict).astype(int)

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
