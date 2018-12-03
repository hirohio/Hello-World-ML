# External Modules
import sys as sys
import traceback

# Internal Modules
import Graphs.GraphsManager as grh
import Preprocessing.PreprocessingManager as pp
import Algorithms.AlgorithmsManager as alg
import IOFiles.IOFileManager as iof
import Helpers.PrintHelpers.PrintHelper as phelper

_MAIN_MENU_COMMANDS_ = [
        "(file):    Import/Export Files menu.",
        "(g):       Graphs menu.",
        "(p):       Preprocessing menu.",
        "(a):       Algorithms menu.",
        "(i):       Inforamtion of read data.",
        "(h):       Header of the data.",
        "(t):       Tail of the data.",
        "(d):       Describe the data.",
]


def main():
    """Entry point of this modules.

    1, If user inputs csv file name in command-line arguments, this function tries to read the file.

    2, If reading the file was failed, this method requires csv file name to user.

    3, If this function succeeded in reading file, this method reqires commands.

    4, This method navigates other command accepters as commands user input.
    """
    try:
        argvs = sys.argv
        argc = len(argvs)

        if(argc < 2):
            path = input("Please input file name: ")
        else:
            print("Input file is "+ argvs[1])
            path = argvs[1]

        # Initialzie Properties.
        _algorithmsmanager = None


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
                if _algorithmsmanager is None:
                    _algorithmsmanager = alg.AlgorithmsManager(df)
                else:
                    _algorithmsmanager._df = df
                _algorithmsmanager.accept_command()
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
            elif ans == "file":
                io_file = iof.IOFileManager()
                result= io_file.accept_command()
                if result is not None:
                    result = df
            elif ans == "":
                continue
            else:
                print(ans + " is not supported command!!\n")
    except EOFError:
        print("Program is ended.")
        sys.exit()
## main function for command line ##
if __name__ == '__main__':
    main()
