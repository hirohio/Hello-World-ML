import pandas as pd

class NumChecker:

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
