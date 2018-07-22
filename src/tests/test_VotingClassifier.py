# External Modules
import unittest
import pandas as pd
import sys,os
sys.path.append(os.pardir)

# Internal Modules
import Algorithms.RandomForest as randomforest
import Algorithms.Deeplearning as deeplearning
import Algorithms.VotingClassifier as votingclassifier

class TestVotingClassifier(unittest.TestCase):

    def test_learn(self):
        df = pd.read_csv('Data/train_data_for_ML.csv',header=0)
        rf = randomforest.RandomForest(df)
        rf.learn('Survived',None)
        learned_rf = rf.model

        dl = deeplearning.DeepLearning(df)
        dl.learn('Survived',None)
        learned_dl = dl.model
        algorithms = []
        algorithms.append(('rf',learned_rf))
        algorithms.append(('dl',learned_dl))

        vc = votingclassifier.VotingClass(df,algorithms)
        vc.learn('Survived',None)

if __name__ == "__main__":
    unittest.main()
