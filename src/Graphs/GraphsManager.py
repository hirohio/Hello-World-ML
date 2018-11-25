# External Modules
import sys as sys
import traceback

# Internal Modules
import Graphs.GraphsExecuter as gph
import Helpers.PrintHelpers.PrintHelper as phelper

_GRAPHS_MANAGER_COMMANDS_ = [
    '(h):           Histgram Plot.',
    '(c):           Count Plot.',
    '(p):           Point Plot.',
    '(s):           Scatter Plot.',
    '(b):           Box Plot.',
    '(pair):        Pair Plot.',
    '(heat):        Heat Map.',
    '(cancel):      Cancel.'
]

class GraphsManager:
    def __init__(self,df):
        self.df = df
        self.graphs = gph.Graphs(self.df)

    def accept_command(self):
        while True:
            phelper.PrintHelper.print_command_menu(_GRAPHS_MANAGER_COMMANDS_)
            ans = input("Please input command: ")
            if ans == "h":
                self._invoke_hist_plot()
                break
            elif ans == "c":
                self._invoke_count_plot()
                break
            elif ans == "p":
                self._invoke_point_plot()
                break
            elif ans == "s":
                self._invoke_sctter_plot()
                break
            elif ans == "b":
                self._invoke_box_plot()
                break
            elif ans == "pair":
                self._invoke_pair_plot()
                break
            elif ans == "heat":
                self._inboke_heatmap()
                break
            elif ans == "cancel":
                break
            elif ans == "":
                continue
            else:
                print(ans + " is not supported")
                break

    def _invoke_hist_plot(self):
        while True:
            column = input("Please input coulmn name: ")
            if not column in self.df.columns:
                print(column + " is not exist!!")
                continue
            else:
                self.graphs.hist_plot(column)
                break
    def _invoke_count_plot(self):
        while True:
            column = input("Please input coulmn name: ")
            if not column in self.df.columns:
                print(column + " is not exist!!")
                continue
            else:
                self.graphs.count_plot(column)
                break
    def _invoke_point_plot(self):
        while True:
            column_x = input("Please input column X name: ")
            if not column_x in self.df.columns:
                print(column_x + " is not exist!!")
                continue
            else:
                break

        while True:
            column_y = input("Please input column Y name: ")
            if not column_y in self.df.columns:
                print(column_y + " is not exist!!")
                continue
            else:
                break

        self.graphs.point_plot(column_x,column_y)

    def _invoke_sctter_plot(self):
        while True:
            column_x = input("Please input column X name: ")
            if not column_x in self.df.columns:
                print(column_x + " is not exist!!")
                continue
            else:
                break

        while True:
            column_y = input("Please input column Y name: ")
            if not column_y in self.df.columns:
                print(column_y + " is not exist!!")
                continue
            else:
                break

            self.graphs.scatter_plot(column_x,column_y)
    def _invoke_pair_plot(self):
        self.graphs.pair_plot()

    def _invoke_box_plot(self):
        self.graphs.box_plot()

    def _inboke_heatmap(self):
        self.graphs.heat_map()
