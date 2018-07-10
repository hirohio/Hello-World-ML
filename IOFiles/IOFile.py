import csv as csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from os import path,pardir

import sys as sys
import traceback

class IOFile:
    def export_to_csv(self,file_name,output_df):
        current_dir = path.abspath(path.dirname(__file__))
        parent_dir = path.abspath(path.join(current_dir, pardir))
        target_dir = parent_dir + "/Data/"
        output_df.to_csv(target_dir+file_name)

#        output_file = open(file_name, "w")
#        file_object = csv.writer(output_file)
#        file_object.writerow([id_column, predicted_column])
#        file_object.writerows(zip(ids, output_df))
#        output_file.close()

    def import_from_csv(self,file_name):
        df = pd.read_csv(file_name,header=0)
        if "Unnamed: 0" in df.columns:
            df = df.drop(["Unnamed: 0"],axis=1)
        return df
