# External Libraries
import unittest
import pandas as pd
import sys,os
sys.path.append(os.pardir)

# Internal Libraries
import Algorithms.Utilities.DataFrameChecker as dc

class TestDataFrameChecker(unittest.TestCase):
    def test_is_df_num(self):
        df = pd.read_csv('Data/numeric.csv',header=0)
        self.assertTrue(dc.DataFrameChecker.is_df_num(df))
        self.assertRaises(ValueError, lambda:dc.DataFrameChecker.is_df_num('test'))

        df = pd.read_csv('Data/numeric_with_text.csv',header=0)
        self.assertFalse(dc.DataFrameChecker.is_df_num(df))

if __name__ == "__main__":
    unittest.main()
