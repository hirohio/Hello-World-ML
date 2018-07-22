import pandas as pd
import sys as sys
import threading
import traceback
import yaml

class IOFile:
    """IOFille Class.
    This class manages file input/output.
    This class is a singleton class to prevent to forget closing file.
    """

    _instance = None
    _lock = threading.Lock()

    # Sigleton Class
    def __new__(cls):
        """This class is a singleton class.
        This method is defined to generates only one instance.
        """
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def export_to_csv(self,file_name,output_df):
        """This method export dataframe file as csv.

        Args:
            df: Dataframe to execute Machine Learnng.

        Returns:
            bool: True or False.
        """
        print ('File path is ' + file_name)
        output_df.to_csv(file_name)

        return True

    def import_from_csv(self,file_name):
        """This method imports csv file as dataframe.
        Then, this method removes 'Unnamed: 0' from dataframe automatically.

        Args:
            file_name: File name of csv you want to import.

        Returns:
            bool: True or False.
        """
        df = pd.read_csv(file_name,header=0)
        if "Unnamed: 0" in df.columns:
            df = df.drop(["Unnamed: 0"],axis=1)
        return df

    def read_from_yaml(self,file_name):
        """This method read yaml file.

        Args:
            file_name: File name of YAML file you want to import.

        Returns:
            list data.
        """
        print ('file path is ' + file_name)

        with open(file_name, "r+") as file:
            parameters = yaml.load(file)
        return parameters
