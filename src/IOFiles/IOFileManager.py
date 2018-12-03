# External Modules
import pandas as pd
import sys as sys
import traceback

# Internal Modules
import IOFiles.IOFile as iof
import Helpers.PrintHelpers.PrintHelper as phelper
import Commons.CommandAccepterBase as CAB

from os import path,pardir
ROOT_DIR = path.abspath(path.join(path.abspath(path.dirname(__file__)),pardir))

_IOFILE_MENU_COMMANDS_ = [
        "(imf):     Import csv file.",
        "(exf):     Export csv file.",
]

class IOFileManager(CAB.CommandAccepterBase):
    """Manager of input/output files.
    This class requires user input to input/output files.

    """
    def __init__(self):
        self.io_file = iof.IOFile()

    def _extend_accept_command(self):
        while True:
            phelper.PrintHelper.print_command_menu(_IOFILE_MENU_COMMANDS_)
            ans = input("Please input command: ")

            if ans == "imf":
                return self.import_from_csv()
            elif ans == "exf":
                self.export_to_csv(df)
                break
            elif ans == "cancel":
                break
            elif ans == "":
                continue
            else:
                print(ans + " is not supported")
                break
    def import_from_csv(self):
        """This method exports dataframe file as csv.

        Returns:
            Dataframe: Dataframe which read csv file.
        """
        df = None
        while True:
            try:
                file_name = input("Please input file. : ")

                if file_name[:1] is not '/':
                    file_name = '/' + file_name
                print ('file path is ' + ROOT_DIR + file_name)
                df = self.io_file.import_from_csv(ROOT_DIR + file_name)
                break
            except FileNotFoundError:
                print(ROOT_DIR + file_name + " is not exist.")
                return
            except:
                print("Unexpected Exception")
                traceback.print_exc()
                sys.exit()
        return df

    #for command line arguments
    def initial_import_from_csv(self, file_name):
        """This method imports csv file as dataframe.

        Arges:
            file_name: File name of csv you want to import

        Returns:
            Dataframe: Dataframe which read csv file.
        """
        try:
            if file_name[:1] is not '/':
                file_name = '/' + file_name
            print ('file path is ' + ROOT_DIR + file_name)

            df = self.io_file.import_from_csv(ROOT_DIR + file_name)
        except FileNotFoundError:
            df = self.import_from_csv()
        return df

    def read_from_yaml(self, file_name):
        """This method read YAML file.

        Arges:
            file_name: File name of YAML you want to import

        Returns:
            Dataframe: Dataframe which read csv file.
        """
        try:
            if file_name[:1] is not '/':
                file_name = '/' + file_name
            print ('file path is ' + ROOT_DIR + file_name)
            data = self.io_file.read_from_yaml(ROOT_DIR + file_name)
        except FileNotFoundError:
            data = None
        return data

    def export_to_csv(self,df):
        """This method exports csv file.

        Arges:
            df: File name of YAML you want to import.

        Returns:
            bool: True or False.
        """
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
        return True

    def export_output(self,original_test_df,output_df,predicted_column):
        """

        """
        columns = ['temp']
        tmp_df = pd.DataFrame(output_df,columns=columns)
        original_test_df[predicted_column] = tmp_df['temp']
        print(original_test_df.head())
        self.export_to_csv(original_test_df)
