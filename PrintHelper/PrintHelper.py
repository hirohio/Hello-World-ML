class PrintHelper:

    '''
    This method print as follows.

    > PrintHelper.print_title('Best Params')
    > *--------------------------------------------------*
    > |                   Best Params                    |
    > *--------------------------------------------------*
    '''
    @classmethod
    def print_title(cls,message):

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
        print("\n******************** Command Menu ********************")
        for command in commands:
            print(command)
        print("******************************************************\n")
