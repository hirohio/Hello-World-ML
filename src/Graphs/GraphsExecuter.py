import matplotlib.pyplot as plt
import seaborn as sns
import sys as sys
import traceback

"""
Graph Class is a class for graphss.
(e.g, histogram)
"""
class Graphs:

    def __init__(self,df):
        """Constracter

        Args:
            df: dataframe to draw graphs
        """
        self.df = df

    def hist_plot(self, column):
        """Draw histogram.

        Args:
            column: column in dataframe to draw graphs
        """
        try:
            sns.distplot(self.df[column], label = column)
            plt.show()
            #self.df.plot(kind='hist',subplots=True)
            plt.show()
        except TypeError:
            print("Unsupported Operand Type. You have to convert following vlaues to integer.\n")
            print(self.df[column].value_counts())
        except:
            print("Unexpected Exception")
            traceback.print_exc()
            sys.exit()

    def box_plot(self):
        """Draw box plot.

        """
        self.df.plot(kind='box',subplots=True)
        plt.show()

    def count_plot(self,column):
        """Draw count plot

        """
        try:
            sns.countplot(x=column, data=self.df, label=column)
            plt.show()
        except TypeError:
            print("Unsupported Operand Type. You have to convert following vlaues to integer.\n")
            print(df[column].value_counts())
        except:
            print("Unexpected Exception")
            traceback.print_exc()
            sys.exit()

    def point_plot(self,column_x,column_y):
        try:
            sns.set(style="whitegrid")
            g = sns.PairGrid(data=self.df, x_vars=column_x, y_vars=column_y)
            g.map(sns.pointplot, color=sns.xkcd_rgb["blue"])
            plt.show()
        except TypeError:
            print("Unsupported Operand Type. You have to convert following vlaues to integer.\n")
            print(df[column].value_counts())
        except:
            print("Unexpected Exception")
            traceback.print_exc()
            sys.exit()

    def scatter_plot(self, column_x, column_y):
        try:
            plt.scatter(self.df[column_x], self.df[column_y])
            plt.show()
        except TypeError:
            print("Unsupported Operand Type. You have to convert following vlaues to integer.\n")
            print(df[column_x].value_counts())
            print(df[column_y].value_counts())
        except:
            print("Unexpected Exception")
            traceback.print_exc()
            sys.exit()

    def pair_plot(self):
        try:
            sns.pairplot(self.df)
            plt.show()
        except:
            print("Unexpected Exception")
            traceback.print_exc()
            sys.exit()
