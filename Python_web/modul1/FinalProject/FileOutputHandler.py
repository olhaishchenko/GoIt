from OutputHandler import *


class FileOutputHandler(OutputHandler):
    def out(self, result):
        # implement writing to file
        with open('output.txt', 'a') as file:
            file.write(f'{result}\n')