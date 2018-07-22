import pandas as pd

class DataFrameChecker:

    @classmethod
    def is_columns_matched(cls,a_df,b_df):
        for val in a_df.columns:
            if not val in b_df.columns:
                return False

        for val in a_df.columns:
            if not val in b_df.columns:
                return False
        return True

    @classmethod
    def is_df_num(cls,df):

        if type(df) is not pd.DataFrame:
            raise ValueError('Value type is not DataFrame')

        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        newdf = df.select_dtypes(include=numerics)
        if newdf.shape[1] == df.shape[1]:
            return True
        else:
            return False

    @classmethod
    def is_num(s):
        return s.replace(',', '').replace('.', '').replace('-', '').isnumeric()
