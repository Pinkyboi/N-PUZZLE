
import re

class Parser():

    def __init__(self, path):
        self._path = path
        self._flattenedPuzzle = []
        self._shape = -1

    def loadData(self):
        try:
            with open(self._path, "r") as f:
                self._lines = f.readlines()
        except FileNotFoundError:
            print("File not found.")
            exit()
        except OSError:
            print("OS Error.")
            exit()
        except Exception as e:
            print(f"Unexpected error {repr(e)}")
            exit()

    def printRawPuzzle(self):
        for line in self._lines:
            print(line, end="")

    def removeComments(self):
        commentPatten = re.compile("(#.+)|[\n]")
        newLines = []
        for line in self._lines:
            newLine = re.sub(commentPatten, '', line)
            if newLine:
                newLines.append(newLine.strip())
        return newLines

    def getShape(self, newLines):
        self.shape = int(newLines[0].split()[0])
        if self._shape <= 2:
            print("Error: Shape cannot be lower than 2.")
            exit()

    @property
    def shape(self):
        return self._shape

    @property
    def flattenedPuzzle(self):
        return self._flattenedPuzzle

    @flattenedPuzzle.setter
    def flattenedPuzzle(self, flattendPuzzle):
        self._flattenedPuzzle = flattendPuzzle

    @shape.setter
    def shape(self, shape):
        self._shape = shape

    @staticmethod
    def manageError(error):
        print(f"Error: {error}.")
        exit()

    def flattenPuzzle(self, puzzleLines):
        if len(puzzleLines) != self.shape:
            self.manageError("Wrong row shape")
        for line in puzzleLines:
            try:
                row = [int(x) for x in line.split()]
            except ValueError:
                self.manageError("Non numeric characters in puzzle")
            if len(row) != self.shape:
                self.manageError("Wrong column shape")
            self.flattenedPuzzle += row
        for i in range(pow(self.shape, 2)):
            if i not in self.flattenedPuzzle:
                self.manageError("Wrong numbers in puzzle")

    def cleanPuzzle(self):
        newLines = self.removeComments()
        if len(newLines[0].split()) != 1:
            self.manageError("Wrong format")
        self.getShape(newLines)
        self.flattenPuzzle(newLines[1:])

        
if __name__ == "__main__":
    p = Parser("puzzle.txt")
    p.loadData()
    # p.printRawPuzzle()
    p.cleanPuzzle()
    print(p.flattenedPuzzle)