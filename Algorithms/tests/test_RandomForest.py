import unittest
import pandas as pd

import sys,os
sys.path.append(os.pardir)
import Algorithms as al

class TestRandomForest(unittest.TestCase):
    def test_learn(self):
        df = pd.read_csv('numeric.csv',header=0)
        self.assertTrue(nc.NumChecker.is_df_num(df))
        self.assertRaises(ValueError, lambda:nc.NumChecker.is_df_num('test'))

        df = pd.read_csv('numeric_with_text.csv',header=0)
        self.assertFalse(nc.NumChecker.is_df_num(df))
        
    def test_predict(slef):



if __name__ == "__main__":
    unittest.main()
