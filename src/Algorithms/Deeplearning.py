# External Libraries
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier

# Internal Libraries
import Algorithms.Utilities.DataFrameChecker as dfc
import PrintHelpers.PrintHelper as phelper

class DeepLearning:
    """RDeepLearning Class.

    """

    @property
    def df(self):
        """Dataframe: Original dataframe to used for learning."""
        return self._df

    @property
    def model(self):
        """MLPClassifier: MLPClassifier(DeepLearning) Model which has learned original data."""
        return self._learned_model

    def __init__(self,df):
        phelper.PrintHelper.print_title(self.__class__.__name__)
        self._df = df

    def learn(self,column,params):
        if dfc.DataFrameChecker.is_df_num(self._df) is False:
            return False

        #predict data
        y = self._df[column]
        self._y = y

        #learning data
        X = self._df .drop([column], axis=1)
        self._X = X

        (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.3, random_state=0)

        model = MLPClassifier()

        phelper.PrintHelper.print_title('Default Params')
        print(model.get_params())

        phelper.PrintHelper.print_title('Params from a file')
        if params == None:
            print('Settings Params file is None.')
            params = {}
        else:
            print(params)

        print('...Doing Grid Search...')
        cv = GridSearchCV(model, params, cv = 10, scoring = 'neg_mean_squared_error', n_jobs=1, refit = True)

        cv.fit(X_train, y_train)

        self._best_params = cv.best_params_
        self._learned_model = cv.best_estimator_

        phelper.PrintHelper.print_title('Best Params')
        print(cv.best_params_)

        self._learned_model = cv

        # Accuracy Score
        print('...Predicting Test Data...')
        predicted_result = self._learned_model.predict(X_test).astype(int)

        phelper.PrintHelper.print_title('Accuracy Score')
        print(accuracy_score(y_test,predicted_result))

        return True

    def predict(self,test_df):
        #checking matching between test_df.columns and x_df.columns
        if dfc.DataFrameChecker.is_columns_matched(self._X,test_df):
            return self._learned_model.predict(test_df).astype(int)

        phelper.PrintHelper.print_error('columns are not matched !!')
        return None
