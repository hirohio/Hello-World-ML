import csv as csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

import threading
import yaml

import sys as sys
import traceback

class IOFile:
    _instance = None
    _lock = threading.Lock()

    # Sigleton Class
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def export_to_csv(self,file_name,output_df):
        print ('file path is ' + file_name)
        output_df.to_csv(file_name)

    def import_from_csv(self,file_name):
        df = pd.read_csv(file_name,header=0)
        if "Unnamed: 0" in df.columns:
            df = df.drop(["Unnamed: 0"],axis=1)
        return df

    def read_from_yaml(self,file_name):
        print ('file path is ' + file_name)
        return yaml.load(open(file_name, "r+"))
