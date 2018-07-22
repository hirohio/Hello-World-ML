import pandas as pd

class DataframeConverter:
    @classmethod
    def convert_params_to_list(self,params):
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

    @classmethod
    def drop_empty_param(self,params):
        """

        """
        for i in params:
            if len(params[i]) == 0:
                params.pop(i)

        return params
