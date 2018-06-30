import unittest
import sys,os
import pandas as pd
from os import path, pardir

current_dir = path.abspath(path.dirname(__file__))          # 実行箇所のディレクトリを取得
parent_dir = path.abspath(path.join(current_dir, pardir))   # スクリプトの親ディレクトリのPathを作成
deep_learning_dir = path.join(parent_dir,'Deep_Learning')   # DeepLearning用のPathを作成

print("Dir : " + deep_learning_dir)
sys.path.append(deep_learning_dir)

from deep_learning import DeepLearning
from deep_learning_lib.two_layer_net import TwoLayerNet

class TestDeepLearningMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_deep_learning(self):
        df = pd.read_csv('test_data_for_deeplearning.csv',header=0)
        dl = DeepLearning(df,2) # the size of kinds of titnic survived data: 0 or 1
        self.assertTrue(dl.predict)

if __name__ == '__main__':
    unittest.main()
