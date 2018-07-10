import unittest
import pandas as pd

import sys,os
sys.path.append(os.pardir)
import Utilities.NumChecker as nc

class TestNumChecker(unittest.TestCase):
    def test_is_df_num(self):
        df = pd.read_csv('numeric.csv',header=0)
        self.assertTrue(nc.NumChecker.is_df_num(df))
        self.assertRaises(ValueError, lambda:nc.NumChecker.is_df_num('test'))

        df = pd.read_csv('numeric_with_text.csv',header=0)
        self.assertFalse(nc.NumChecker.is_df_num(df))

if __name__ == "__main__":
    unittest.main()
