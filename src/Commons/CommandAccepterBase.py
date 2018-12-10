import sys

class CommandAccepterBase:
    def accept_command(self):
        try:
            return self._extend_accept_command()
        except EOFError:
            print("Program is ended.")
            sys.exit()

    def _extend_accept_command(self):
        raise NotImplementedError
