#scikit-learnから必要な関数をインポート
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix

class DeepLearningManager:
    def __init__(self,df):
        self._df = df

    def predict(self,column,test_df,solver,activation):
        self._y_column = column
        #predict data
        y_df = self._df[self.y_column]

        #learning data
        x_df = self._df.drop([self.y_column], axis=1)
        print("[train data]: \n")
        x_df.info()

        #test Data
        original_test_df = test_df

        #preprocessing test Data
        #Matching between train_df and test_df
        print("\n" + "preprocesing data")
        for val in test_df.columns:
            if not val in x_df.columns:
                test_df = test_df.drop(val, axis=1)
                print("dropped " + val + " from test data")

        for val in x_df.columns:
            if not val in test_df.columns:
                x_df = x_df.drop(val, axis=1)
                print("dropped " + val + " from train data")

        print("[test data]: \n")
        test_df.info()

        print("Deep Learning is learning\n")

        clf = MLPClassifier(solver=solver,activation=activation)

        #fit(説明変数, 目的変数).predict(トレーニングデータ)
        output = clf.fit(x_df,y_df).predict(test_df).astype(int)
        return output
