import Algorithms.RandomForest as randforest
import Algorithms.Deeplearning as deeplearning
import Algorithms.VotingClassifier as votingclassfier
import Algorithms.Utilities.DataFrameChecker as dfc
import IOFiles.IOFileManager as iof
import PrintHelpers.PrintHelper as phelper

_RANDOM_FOREST_PARAMETER_PATH = "/Algorithms/Data/RandomForestParameters_test.yml"
_DEEP_LEARNING_PARAMETER_PATH = "/Algorithms/Data/DeepLearningParameters_test.yml"

_ALGORITHMS_MANAGER_COMMANDS_ = [
    "(r):       RandomForest (ensemble)",
    "(d):       DeepLearning",
    "(v):       VotingClassfier (ensemble)",
    "(c):       Cancel"
]

class AlgorithmsManager:
    """AlgorithmManager Class.
    This class accepts commands and execute machine learning algorithms.

    """

    @property
    def df(self):
        """Dataframe: Original dataframe to used for learning."""
        return self._df

    def __init__(self,df):
        """
        This method is a constracter.

        Args:
            df: Dataframe to execute Machine Learnng.

        """
        self._df = df

    def accept_command(self):
        """
        This method acccepts commands from userself and invoke algorithm classes.

        Examples:
            >>> AlgorithmManager(df).accept_command()
            ******************** Command Menu ********************
            (r):       RandomForest (ensemble)
            (d):       DeepLearning
            (v):       VotingClassfier (ensemble)
            (c):       Cancel
            ******************************************************
        """
        while True:
            phelper.PrintHelper.print_command_menu(_ALGORITHMS_MANAGER_COMMANDS_)

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
        """
        This method invoke random forest.
        It accepts some input for random forest from user.
        """

        # Check object type is existed in data frame
        if dfc.DataFrameChecker.is_df_num(self._df) is False:
            print('Random Forest can not accept these types but int or float')
            return

        print("Following data is referd for training")
        self._df.info()

        self._rf = randforest.RandomForest(self._df)

        while True:
            prediction_column = input("Input column you want to predict: ")
            if(prediction_column in self._df.columns):
                break

        # read parameter from a file.
        io_file = iof.IOFileManager()
        params = io_file.read_from_yaml(_RANDOM_FOREST_PARAMETER_PATH)

        self._rf.learn(prediction_column,params)

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

        output_df = self._rf.predict(test_df)
        if not output_df is None:
            print("Exporting File\n")
            io_file.export_output(test_df,output_df,prediction_column)
        else:
            phelper.PrintHelper.print_error('Prediction data was failed!!')

    def _invoke_deep_learning(self):
        """
        This method invoke deep learning.
        It accepts some input for deep learning from user.
        """

        # Check object type is existed in data frame
        if dfc.DataFrameChecker.is_df_num(self._df) is False:
            print('Deep Learning can not accept these types but int or float')
            return

        print("Following data is referd for training")
        self._df.info()
        self._dl = deeplearning.DeepLearning(self._df)

        while True:
            prediction_column = input("Input column you want to predict: ")
            if(prediction_column in self._df.columns):
                break

        # read parameter from a file.
        io_file = iof.IOFileManager()
        params = io_file.read_from_yaml(_DEEP_LEARNING_PARAMETER_PATH)

        if not slef._dl.learn(prediction_column,params):
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

        output_df = self._dl.predict(test_df)

        print("Exporting File\n")
        io_file.export_output(test_df,output_df,prediction_column)

    def _invoke_voting_classfier(self):
        """This method makes voting classfier learn data.

        """
        print("Following data is referd for training")
        self._df.info()
        vc = votingclassfier.VotingClassifier(self._df)

        while True:
            prediction_column = input("Input column you want to predict: ")
            if(prediction_column in self._df.columns):
                break

        print("Test(Target) file is required.")
        io_file = iof.IOFileManager()
        test_df = io_file.import_from_csv()

        vc.learn(prediction_column)