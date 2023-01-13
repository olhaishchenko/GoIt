from OutputHandler import *


class ConsoleOutputHandler(OutputHandler):
    def out(self, result):
        print(result)