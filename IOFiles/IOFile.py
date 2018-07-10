import csv as csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from os import path,pardir
import threading

import yaml

import sys as sys
import traceback

ROOT_DIR = path.abspath(path.join(path.abspath(path.dirname(__file__)),pardir))

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
        print ('file path is ' + ROOT_DIR + file_name)
        output_df.to_csv(ROOT_DIR + file_name)

    def import_from_csv(self,file_name):
        print ('file path is ' + ROOT_DIR + file_name)
        df = pd.read_csv(ROOT_DIR + file_name,header=0)
        if "Unnamed: 0" in df.columns:
            df = df.drop(["Unnamed: 0"],axis=1)
        return df

    def read_from_yaml(self,file_name):
        print ('file path is ' + ROOT_DIR + file_name)
        return yaml.load(open(ROOT_DIR + file_name, "r+"))
