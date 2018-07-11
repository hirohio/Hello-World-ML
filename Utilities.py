import csv as csv
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import sys as sys
import traceback

# Our libraries
import Graphs.GraphsManager as grh
import Preprocessing.PreprocessingManager as pp
import Algorithms.AlgorithmsManager as alg
import IOFiles.IOFileManager as iof
import PrintHelper.PrintHelper as phelper

_MAIN_MENU_COMMANDS_ = {
        "(imf):     Import csv file.",
        "(exf):     Export csv file.",
        "(g):       Graphs menu.",
        "(p):       Preprocessing menu.",
        "(a):       Algorithms menu.",
        "(i):       Inforamtion of read data.",
        "(h):       Header of the data.",
        "(t):       Tail of the data.",
        "(d):       Describe the data.",
}

## main function for command line ##
if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)

    if(argc < 2):
        path = input("Please input file name: ")
    else:
        print("Input file is "+ argvs[1])
        path = argvs[1]

    while True:
        try:
            io_file = iof.IOFileManager()
            df = io_file.initial_import_from_csv(path)
            df.info()
            break
        except FileNotFoundError:
            print("Wrong file or File is not exist\n")
            path = input("Please input file name: ")
            continue
        except:
            print("Unexpected Exception")
            traceback.print_exc()
            sys.exit()

    while True:
        phelper.PrintHelper.print_command_menu(_MAIN_MENU_COMMANDS_)

        ans = input("Please input command: ")

        if ans == "g":
            graphsManager = grh.GraphsManager(df)
            graphsManager.accept_command()
        elif ans == "a":
            algorithmsmanager = alg.AlgorithmsManager(df)
            algorithmsmanager.accept_command()
        elif ans == "p":
            prepManager = pp.PreprocessingManager(df)
            df = prepManager.accept_command()
        elif ans == "i":
            df.info()
        elif ans == "h":
            print(df.head())
        elif ans == "t":
            print(df.tail())
        elif ans == "d":
            print(df.describe())
        elif ans == "imf":
            io_file = iof.IOFileManager()
            df = io_file.import_from_csv()
        elif ans == "exf":
            io_file = iof.IOFileManager()
            io_file.export_to_csv(df)
        elif ans == "":
            continue
        else:
            print(ans + " is not supported command!!\n")
