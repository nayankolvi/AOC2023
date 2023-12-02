class Read:
    def __init__(self, file = 'None'):
        self.file = file
        pass

    # read lines
    def readLines(self, file):
        with open(file, "r") as f:
            lines = f.readlines()

        revisedLines = [line.replace('\n', '') for line in lines]
        return revisedLines


rd = Read()