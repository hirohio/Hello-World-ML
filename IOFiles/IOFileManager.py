import csv as csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

import sys as sys
import traceback
import IOFiles.IOFile as iof

class IOFileManager:
    def __init__(self):
        self.io_file = iof.IOFile()

    def import_from_csv(self):
        while True:
            try:
                file_name = input("Please input file. : ")
                df = self.io_file.import_from_csv(file_name)
                return df
            except FileNotFoundError:
                print(file_name + " is not exist.")
                continue
            except:
                print("Unexpected Exception")
                traceback.print_exc()
                sys.exit()

    #for command line arguments
    def initial_import_from_csv(self, file_name):
        try:
            df = self.io_file.import_from_csv(file_name)
        except FileNotFoundError:
            df = self.import_from_csv()
        return df

    def read_from_yaml(self, file_name):
        try:
            data = self.io_file.read_from_yaml(file_name)
        except FileNotFoundError:
            data = None
        return data

    def export_to_csv(self,df):
        while True:
            try:
                file_name = input("Please input output file name. : ")
                self.io_file.export_to_csv('/Data/' + file_name,df)
                return df
            except:
                print("Unexpected Exception")
                traceback.print_exc()
                sys.exit()


    def export_output(self,original_test_df,output_df,predicted_column):
        print('*-----------------------------*')
        print('|     Original Test Data      |')
        print('*-----------------------------*')
        original_test_df.info()
        ans = input("(w):Write output to file, (cancel) Not write output to file: ")
        while True:
            if ans == "w":
                while True:
                    try:
                        id_column = input("Input id column for output: ")
                        ids = original_test_df[id_column]
                        break
                    except KeyError:
                        print("Wrong column name or the column is not exist")
                        continue
                    except:
                        print("Unexpected Exception")
                        traceback.print_exc()
                        sys.exit()

                file_name = input("Please write output file name: ")
                output_file = open(file_name, "w")
                file_object = csv.writer(output_file)
                file_object.writerow([id_column, predicted_column])
                file_object.writerows(zip(ids, output_df))
                output_file.close()
                break

            elif ans == "cancel":
                break
