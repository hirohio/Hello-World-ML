import Algorithms.RandomForest as randforest
import Algorithms.Deeplearning as deeplearning
import Algorithms.VotingClassifier as votingclassfier
import IOFiles.IOFileManager as iof
import Algorithms.Utilities.DataFrameChecker as dfc

RANDOM_FOREST_PARAMETER_PATH = "/Algorithms/Data/RandomForestParameters_test.yml"
DEEP_LEARNING_PARAMETER_PATH = "/Algorithms/Data/DeepLearningParameters_test.yml"

class AlgorithmsManager:

    def __init__(self,df):
        self._df = df

    @property
    def df(self):
        return self._df

    def accept_command(self):
        while True:
            print("\n******** Command Menu ************")
            print("(r):RandomForest (ensemble)")
            print("(d):DeepLearning")
            print("(v):VotingClassfier (ensemble)")
            print("(c):Cancel")
            print("**********************************\n")
            ans = input("Please input command: ")
            if ans == "r":
                self._invoke_random_forest()
                break
            elif ans == "d":
                self._invoke_deep_learning()
                break
            elif ans == "v":
                self._invoke_voting_classfier()
            elif ans == "cancel":
                break
            elif ans == "":
                continue

    def _invoke_random_forest(self):
        # Check object type is existed in data frame
        if dfc.DataFrameChecker.is_df_num(self._df) is False:
            print('Random Forest can not accept these types but int or float')
            return

        print("Following data is referd for training")
        self._df.info()

        rf = randforest.RandomForestManager(self._df)

        while True:
            prediction_column = input("Input column you want to predict: ")
            if(prediction_column in self._df.columns):
                break

        # read parameter from a file.
        io_file = iof.IOFileManager()
        params = io_file.read_from_yaml(RANDOM_FOREST_PARAMETER_PATH)

        rf.learn(prediction_column,params)

        while True:
            ans = input("Do you predict test csv file? ( y / n ) :")
            if 'y' ==  ans:
                print("Test file is required.")
                io_file = iof.IOFileManager()
                test_df = io_file.import_from_csv()
                break
            elif 'n' == ans:
                return
            else:
                continue

        output_df = rf.predict(test_df)
        if not output_df is None:
            print("Exporting File\n")
            io_file.export_output(test_df,output_df,prediction_column)
        else:
            phelper.PrintHelper.print_error('Prediction data was failed!!')

    def _invoke_deep_learning(self):
        # Check object type is existed in data frame
        if dfc.DataFrameChecker.is_df_num(self._df) is False:
            print('Deep Learning can not accept these types but int or float')
            return

        print("Following data is referd for training")
        self._df.info()
        dl = deeplearning.DeepLearningManager(self._df)

        while True:
            prediction_column = input("Input column you want to predict: ")
            if(prediction_column in self._df.columns):
                break

        # read parameter from a file.
        io_file = iof.IOFileManager()
        params = io_file.read_from_yaml(DEEP_LEARNING_PARAMETER_PATH)

        if not dl.learn(prediction_column,params):
            print('Deep Learning was failed')
            return

        while True:
            ans = input("Do you predict test csv file? ( y / n ) :")
            if 'y' ==  ans:
                print("Test file is required.")
                io_file = iof.IOFileManager()
                test_df = io_file.import_from_csv()
                break
            elif 'n' == ans:
                return
            else:
                continue

        output_df = dl.predict(test_df)

        print("Exporting File\n")
        io_file.export_output(test_df,output_df,prediction_column)

    def _invoke_voting_classfier(self):
        print("Following data is referd for training")
        self._df.info()
        vc = votingclassfier.VotingClassifierManager(self._df)

        while True:
            prediction_column = input("Input column you want to predict: ")
            if(prediction_column in self._df.columns):
                break

        print("Test(Target) file is required.")
        io_file = iof.IOFileManager()
        test_df = io_file.import_from_csv()

        vc.learn(prediction_column)
