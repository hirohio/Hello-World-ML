# External Modules
import pandas as pd
import sys as sys
import traceback

# Internal Modules
import IOFiles.IOFile as iof
import PrintHelpers.PrintHelper as phelper

from os import path,pardir
ROOT_DIR = path.abspath(path.join(path.abspath(path.dirname(__file__)),pardir))

class IOFileManager:
    def __init__(self):
        self.io_file = iof.IOFile()

    def import_from_csv(self):
        while True:
            try:
                file_name = input("Please input file. : ")

                if file_name[:1] is not '/':
                    file_name = '/' + file_name
                print ('file path is ' + ROOT_DIR + file_name)
                df = self.io_file.import_from_csv(ROOT_DIR + file_name)
                return df
            except FileNotFoundError:
                print(ROOT_DIR + file_name + " is not exist.")
                continue
            except:
                print("Unexpected Exception")
                traceback.print_exc()
                sys.exit()

    #for command line arguments
    def initial_import_from_csv(self, file_name):
        try:
            if file_name[:1] is not '/':
                file_name = '/' + file_name
            print ('file path is ' + ROOT_DIR + file_name)

            df = self.io_file.import_from_csv(ROOT_DIR + file_name)
        except FileNotFoundError:
            df = self.import_from_csv()
        return df

    def read_from_yaml(self, file_name):
        try:
            if file_name[:1] is not '/':
                file_name = '/' + file_name
            print ('file path is ' + ROOT_DIR + file_name)
            data = self.io_file.read_from_yaml(ROOT_DIR + file_name)
        except FileNotFoundError:
            data = None
        return data

    def export_to_csv(self,df):
        while True:
            try:
                file_name = input("Please input output file name. : ")
                if file_name[:1] is not '/':
                    file_name = '/' + file_name
                print ('file path is ' + ROOT_DIR + file_name)
                self.io_file.export_to_csv(ROOT_DIR + file_name,df)
                return df
            except:
                print("Unexpected Exception")
                traceback.print_exc()
                sys.exit()

    def export_output(self,original_test_df,output_df,predicted_column):

        columns = ['temp']
        tmp_df = pd.DataFrame(output_df,columns=columns)
        original_test_df[predicted_column] = tmp_df['temp']
        print(original_test_df.head())
        self.export_to_csv(original_test_df)
