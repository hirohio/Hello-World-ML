# External Libraries
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Internal Libraries
import Helpers.DataFrameHelpers.DataFrameChecker as dfc
import Helpers.PrintHelpers.PrintHelper as phelper

class RandomForest:
    """RandomFroest Class.

    """

    @property
    def df(self):
        """Dataframe: Original dataframe to used for learning."""
        return self._df

    @property
    def model(self):
        """RandomForestClassifier: RanfromForest Model which has learned original data."""
        return self._learned_model

    def __init__(self,df):
        """
        Constracter.

        Args:
            df (Dataframe): Dataframe to learn.
        """
        self._df = df
        phelper.PrintHelper.print_title(self.__class__.__name__)

    def learn(self,column,params):
        """Randomforest learns data in dataframe.

        Args:
            column (str): data you want to prdict.
            params (list): parameter for Searching.

        Returns:
            bool: Suecceded or Failed.

        Examples:


        """
        if dfc.DataFrameChecker.is_df_num(self._df) is False:
            return False

        #predict data
        y = self._df[column]
        self._y = y

        #learning data
        X = self._df.drop([column], axis=1)
        self._X = X

        (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.3, random_state=0)

        model = RandomForestClassifier()

        if params == None:
            phelper.PrintHelper.print_title('Default Params')
            params = self._convert_params_to_list(model.get_params())
            print(params)
        else:
            phelper.PrintHelper.print_title('Params from a file')
            #params = self._convert_params_to_list(params)
            print(params)

        print('...Doing Grid Search...')
        cv = GridSearchCV(model, params, cv = 10, scoring = 'neg_mean_squared_error', n_jobs=1, refit = True)

        cv.fit(X_train, y_train)

        self._best_params = cv.best_params_
        self._learned_model = cv.best_estimator_

        phelper.PrintHelper.print_title('Best Params')
        print(cv.best_params_)

        self._learned_model = cv

        phelper.PrintHelper.print_title('Feature Importance')
        feature_names = X_train.columns
        importances = cv.best_estimator_.feature_importances_

        for (feature_name, importance) in zip(feature_names, importances):
            print("{0:<20}".format (feature_name), importance)

        # Accuracy Score
        print('...Predicting Test Data...')
        predicted_result = self._learned_model.predict(X_test).astype(int)

        phelper.PrintHelper.print_title('Accuracy Score')
        print(accuracy_score(y_test,predicted_result))

        return True

    def predict(self,test_df):
        """
        Randomforest predict data.

        Args:
            test_df (str): data you want to prdict.

        Returns:
            Dataframe: Dataframe with predict data or None.

        """
        #checking matching between test_df.columns and x_df.columns
        if dfc.DataFrameChecker.is_columns_matched(self._X,test_df):
            return self._learned_model.predict(test_df).astype(int)

        phelper.PrintHelper.print_error('columns are not matched !!')
        return None

    def _convert_params_to_list(self,params):
        """Convert parameters for estimator to list.
        GridSearch can not receive object but list.
        This method convert parameters to list.

        Args:
            params (map): parameters for estimater.

        Returns:
            list: list of parameters
        """
        result = {}
        for i in params:
            result_list = []
            result_list.append(params[i])
            result[i] = result_list
        return result
