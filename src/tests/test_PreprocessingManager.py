# External Libraries
import unittest
import pandas as pd
import sys,os
sys.path.append(os.pardir)

import re

# Internal Libraries
import Preprocessing.PreprocessingManager as pp


class TestprocessingManager(unittest.TestCase):
    def test_check_value_drop_rows(self):
        df = pd.read_csv('Data/wine_train.csv',header=0)
        pManager = pp.PreprocessingManager(df)
        words = re.split(" ", "a > 0")
        self.assertTrue(pManager._check_value_of_invoke_drop_rows(words))

if __name__ == "__main__":
    unittest.main()
