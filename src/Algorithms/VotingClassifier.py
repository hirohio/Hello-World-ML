# External Modules
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

# Internal Modules
import PrintHelpers.PrintHelper as phelper
import Algorithms.Utilities.DataframeConverter as dfc

class VotingClass:
    """Voting Class

    """

    @property
    def df(self):
        """Dataframe: Original dataframe to used for learning."""
        return self._df

    def __init__(self,df,algorithms):
        """ Constracter

        Args:
            df (Dataframe): dataframe for learning.
            algorithms (list): list of algorithms.
        """
        self._df = df
        self._algorithms = algorithms
        phelper.PrintHelper.print_title(self.__class__.__name__)


    def learn(self,column,params):
        """

        """
        #predict data
        y = self._df[column]
        self._y = y

        #learning data
        X = self._df.drop([column], axis=1)
        self._X = X

        (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.3, random_state=0)

        eclf = VotingClassifier(estimators=self._algorithms)

        if params == None:
            self._learned_model = eclf
            eclf.fit(X_train, y_train)
            print('...Predicting Test Data...')
            predicted_result = self._learned_model.predict(X_test).astype(int)
        else:
            phelper.PrintHelper.print_title('Params from a file')
            print(params)

            print('...Doing Grid Search...')
            cv = GridSearchCV(eclf, params, cv = 10, scoring = 'neg_mean_squared_error', n_jobs=1, refit = True)
            cv.fit(X_train, y_train)

            self._best_params = cv.best_params_
            self._learned_model = cv.best_estimator_

            phelper.PrintHelper.print_title('Best Params')
            print(cv.best_params_)

            self._learned_model = cv

            # Print accuracy score
            print('...Predicting Test Data...')
            predicted_result = self._learned_model.predict(X_test).astype(int)

        phelper.PrintHelper.print_title('Accuracy Score')
        print(accuracy_score(y_test,predicted_result))

        return True

    def predict(self,test_df):

        return self._learned_model.predict(test_df).astype(int)
