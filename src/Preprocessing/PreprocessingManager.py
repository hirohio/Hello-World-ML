# External Modules
import pandas as pd
import sys as sys
import traceback
import re

# Internal Modules
import Preprocessing.PreprocessingExecuter as prep
import Helpers.PrintHelpers.PrintHelper as phelper
import Helpers.DataFrameHelpers.DataFrameChecker as dfc
import Commons.CommandAccepterBase as CAB

_PROCESSING_MANAGER_COMMANDS_ = [
    "(add id)           Add id to each rows.",
    "(dc):              Drop columns.",
    "(dr):              Delete rows which meets terms",
    "(median):          Complete with median.",
    "(mean):            Complete with mean.",
    "(most frequent):   Complerte with most frequent",
    "(tw):              Time to weekday.",
    "(td):              Time to datetime.",
    "(n):               Nomilize data",
    "(f):               Fill in NaN data with value",
    "(coi):             Convert objects to int",
    "(cib):             Covnert int to boolean",
    "(s):               Sum two columns",
    "(sample):           Sampling rows from data.",
    "(deloutlier):      Delete outlier",
    "(cancel):          Cancel."
]

class PreprocessingManager(CAB.CommandAccepterBase):
    """Preprocessing Manager
    This modules accepts commadn to prepreocessing data.

    """
    def __init__(self, df):
        self._df = df
        self._pp = prep.Preprocessing(self._df)

    def _extend_accept_command(self):
        while True:
            phelper.PrintHelper.print_command_menu(_PROCESSING_MANAGER_COMMANDS_)

            ans = input("Please input command: ")
            if ans == "add id":
                return self._invoke_add_id()
            elif ans == "dc":
                return self._invoke_drop_colum()
            elif ans == "dr":
                return self._invoke_drop_rows()
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
            elif ans == "sample":
                return self._invoke_sample()
            elif ans == "cib":
                return self._invoke_convert_columns_to_boolean()
            elif ans == "deloutlier":
                return self._invoke_delete_outlier()
            elif ans == "cancel":
                return self._df
            elif ans == "":
                continue
            else:
                print(ans + " is not a supported command!\n")
                continue
    def _invoke_add_id(self):
        return self._pp.add_id()

    def _invoke_complement_with_median(self):
        while True:
            column = input("Plese input column name: ")
            if not column in self._df.columns:
                print(column + " is not exist!!")
                continue
            else:
                return self._pp.complement_with_median(column)
    def _invoke_complement_with_mean(self):
        while True:
            column = input("Plese input column name: ")
            if not column in self._df.columns:
                print(column + " is not exist!!")
                continue
            else:
                return self._pp.complement_with_mean(column)

    def _invoke_complement_with_mostfrequency(self):
        while True:
            column = input("Plese input column name: ")
            if not column in self._df.columns:
                print(column + " is not exist!!")
                continue
            else:
                return self._pp.complement_with_mostfrequency(column)

    def _invoke_drop_colum(self):
        """dorp columns from dataframe.

        """
        while True:
            ans = input("Please input coulmn name or NaN: ")
            if ans == "NaN":
                return self._pp.drop_nan()
            elif ans == "":
                continue
            elif ans not in self._df.columns:
                print(ans + " is not exist!!")
                continue
            else:
                return self._pp.drop_colum(ans)
    def _invoke_drop_rows(self):
        """drop rows which meets term.

        """
        while True:
            command = input("Please input a term value. (e.g, column_name = 1  column_name < 1, column_name > 1 ): ")
            words = re.split(" ", command)
            column = words[0]
            term = words[1]
            try:
                threshold = int(words[2])
            except TypeError:
                phelper.PrintHelper.print_error("invalid value error: Is " + words[2] + " numeric?")
                return self._df
            except ValueError:
                phelper.PrintHelper.print_error("invalid value error: Is " + words[2] + " numeric?")
                return self._df

            if column not in self._df.columns:
                print(column + " is not existed!!")
                continue

            if self._check_value_of_invoke_drop_rows(words) is False:
                return self._df
            else:
                return self._pp.drop_rows(column,term,threshold)

    def _check_value_of_invoke_drop_rows(self,words):
        if (len(words) != 3):
            print(words + " is not supported!")
            return False
        elif words[1] == ">" or words[1] == "<" or words[1] == "=":
            return True
        else:
            print(words + " is not supported!")
            return False


    def _invoke_convert_time_to_weekdays(self):
        """Convert time to weekdays.
        This method covnerts time to weekdays(0,1,2,3,4,5,6,7).

        Returns:
            Dataframe: dataframe with converted time to weekdays value.

        Examples:
            original data : ['2017-11-07 09:30:38']

        """
        while True:
            ans = input("Please input column name you want to convert to weekday: ")
            if ans not in self._df.columns:
                print(ans + "is not exist!!")
                continue
            else:
                return self._pp.convert_time_to_weekdays(ans)


    def _invoke_convert_time_to_datetime(self):
        """Convert time to date time as follows
        This method convert time to date time as follows


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
        while True:
            ans = input("Please input column name you want to convert to datetime: ")
            if ans not in self._df.columns:
                print(ans + " is not exist!!")
                continue
            else:
                #show example with 1 line.
                tmp_df = self._df.iloc[:1,]

                commands = [
                'original data: '   + str(tmp_df[ans].values),
                'year: (ex),'       + str(pd.to_datetime(tmp_df[ans]).dt.year.values),
                'month:(ex),'       + str(pd.to_datetime(tmp_df[ans]).dt.month.values),
                'day: (ex),'        + str(pd.to_datetime(tmp_df[ans]).dt.day.values),
                'hour: (ex),'       + str(pd.to_datetime(tmp_df[ans]).dt.hour.values),
                'minute: (ex),'     + str(pd.to_datetime(tmp_df[ans]).dt.minute.values),
                'second; (ex),'     + str(pd.to_datetime(tmp_df[ans]).dt.second.values),
                'microsecond (ex),' + str(pd.to_datetime(tmp_df[ans]).dt.microsecond.values)
                ]
                phelper.PrintHelper.print_command_menu(commands)
                break

        while True:
            try:
                print("Please input one of following instructions.")
                ans_time = input("year, month, day, hour, minute, second, microsecond, (c):Cancel :")
                if ans_time == "c":
                    return self._df
                else:
                    return  self._pp.convert_time_to_datetime(ans,ans_time)
            except prep.NotSupportedError:
                print(ans + " is not supported!!")
                continue

    def _invoke_convert_nomalize(self):
        while True:
            ans = input("Please input column name you want to convert to datetime: ")
            if ans not in self._df.columns:
                print(ans + " is not exist!!")
                continue
            else:
                return self.pp.convert_data_to_nomalized(ans)

    def _invoke_fill_in_NaN(self):
        while True:
            ans = input("Please input column name you want to fill in: ")
            if ans not in self._df.columns:
                print(ans + " is not exist!!")
                continue
            else:
                break
        while True:
            print(self._df[ans].value_counts())
            ans_value = input("Please input value name you want to fill in NaN: ")
            if not ans_value in self._df[ans].unique():
                print(ans_value + " is not exist!!")
                continue
            else:
                return self._pp.fill_in_NaN(ans,ans_value)

    def _invoke_convert_object_to_int(self):
        while True:
            ans = input("Please input column name you want to convert type object to int: ")
            if ans not in self._df.columns:
                print(ans + " is not exist!!")
                continue
            else:
                return self._pp.convert_object_to_int(ans)

    def _invoke_sum_columns(self):
        while True:
            print(self._df.columns)
            column_name = input("Please input 1st column name you want to Add: ")
            if not column_name in self._df.columns:
                print(column_name + " is not existed!!")
                continue

            column_name2 = input("Please input 2nd column name you want to Add: ")
            if not column_name2 in self._df.columns:
                print(column_name2 + " is not existed!!")
                continue

            new_column_name = input("Please input new column name you want to create: ")
            if new_column_name in self._df.columns:
                print(new_column_name + " is existed!!")
                continue
            return self._pp.sum_columns(column_name,column_name2,new_column_name)
    def _invoke_sample(self):
        while True:
            n = input("Please input number of rows.")
            if not n.isdigit():
                phelper.PrintHelpers.print_error("Your input is not numeric.")
                continue
            else:
                return self._pp.sample(n)

    def _invoke_convert_columns_to_boolean(self):
        while True:
            print(self._df.columns)
            column_name = input("Please input column name you want to convert: ")
            if not column_name in self._df.columns:
                print(column_name + " is not exist!!")
                continue
            new_column_name = input("Please input new column name you want to create: ")
            if new_column_name in self._df.columns:
                print(new_column_name + " is existed!!")
                continue
            threshold = input("Please input threshold value: ")
            return self._pp.convert_columns_to_boolean(column_name,new_column_name,int(threshold))

    def _invoke_delete_outlier(self):
        while True:
            self._df.info()
            column_name = input("Please input column name you want to delete when it is ourlierself. If you did not column name, system tries to delete outlier from all columns: ")
            if column_name == "":
                if not dfc.DataFrameChecker.is_df_num(self._df):
                    print("[Warning!]Some data are NOT numeric. You have to convert the data type to integer or float before")
                    return self._df
                break;
            elif not column_name in self._df.columns:
                print(column_name + " is not existed!!")
                continue
            elif column_name in self._df.columns:
                 if not dfc.DataFrameChecker.is_df_num(self._df[column_name]):
                     print("[Warning!]" + column_name + " is NOT numeric. You have to convert the data type to integer or float before!")
            else:
                break


        while True:
            bias = input("Please input bias(e.g, 1.5). Default value is 1.5: ")
            if bias == "":
                print("bias is default value(1.5)")
                bias = 1.5
                break
            else:
                break
        # delete out lier from all columns
        if column_name == "":
            for i in self._df.columns:
                print("Delete outlier in " + i)
                self._pp.df.info()
                self._pp.df = self._pp.delete_outlier(i,float(bias))
            return self._pp.df
        # delete out lier from one column
        else:
            return self._pp.delete_outlier(column_name,float(bias))
