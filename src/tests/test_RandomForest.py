# External Modules
from sklearn.ensemble import RandomForestClassifier
import unittest
import pandas as pd
import sys,os
sys.path.append(os.pardir)

# Internal Libraries
import Algorithms.Utilities.DataFrameChecker as dc
import Algorithms.RandomForest as randomforest
import IOFiles.IOFileManager as iof

_RANDOM_FOREST_PARAMETER_PATH = "/Algorithms/Data/RandomForestParameters_test.yml"

class TestRandomForest(unittest.TestCase):
    def test_convert_params_to_lits(self):
        model = RandomForestClassifier()
        params = model.get_params()

        df = pd.read_csv('Data/train_data_for_ML.csv',header=0)
        rf = randomforest.RandomForest(df)
        rf._convert_params_to_list(params)

        io_file = iof.IOFileManager()
        params = io_file.read_from_yaml(_RANDOM_FOREST_PARAMETER_PATH)
        rf._convert_params_to_list(params)

    def test_learn(self):
        df = pd.read_csv('Data/train_data_for_ML.csv',header=0)
        rf = randomforest.RandomForest(df)
        rf.learn('Survived',None)
        learned_rf = rf.model

    def test_learn_yaml_param(self):
        df = pd.read_csv('Data/train_data_for_ML.csv',header=0)
        rf = randomforest.RandomForest(df)
        io_file = iof.IOFileManager()
        params = io_file.read_from_yaml(_RANDOM_FOREST_PARAMETER_PATH)

        rf.learn('Survived',params)
        learned_rf = rf.model

if __name__ == "__main__":
    unittest.main()
