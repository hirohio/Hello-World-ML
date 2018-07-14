class PrintHelper:
    """PrintHelper classs.
    This module prvides with format to print.
    """

    @classmethod
    def print_title(cls,message):
        """print title.
        Args:
            message (str): message you want to print.

        Examples:
            This method print as follows.

            >>> PrintHelper.print_title('Best Params')
            *--------------------------------------------------*
            |                   Best Params                    |
            *--------------------------------------------------*
        """

        MAX_MESSAGE_LENGTH = 50

        front_blank_len = (MAX_MESSAGE_LENGTH-len(message))/2
        back_blank_len = (MAX_MESSAGE_LENGTH-len(message))/2 + (MAX_MESSAGE_LENGTH-len(message))%2

        str_bar = '*'
        for i in range(MAX_MESSAGE_LENGTH):
            str_bar += '-'
        str_bar += '*'

        str_mes = '|'
        for i in range(int(front_blank_len)):
            str_mes += ' '
        str_mes += message
        for i in range(int(back_blank_len)):
            str_mes += ' '
        str_mes += '|'

        print('\n'+str_bar)
        print(str_mes)
        print(str_bar)

    @classmethod
    def print_error(cls,message):
        print('[Error]: ' + message)

    @classmethod
    def print_command_menu(cls, commands):
        """print command menu.
        Args:
            commands (list): message you want to print commands list.

        Examples:
            This method print as follows.

            >>> PrintHelper.print_command_commands(commands_list)
            ******************** Command Menu ********************
            (imf):     Import csv file.
            (exf):     Export csv file.
            (g):       Graphs menu.
            (p):       Preprocessing menu.
            (a):       Algorithms menu.
            (i):       Inforamtion of read data.
            (h):       Header of the data.
            (t):       Tail of the data.
            (d):       Describe the data.
            ******************************************************
        """
        print("\n******************** Command Menu ********************")
        for command in commands:
            print(command)
        print("******************************************************\n")
