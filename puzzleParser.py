
import re
import sys

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
            sys.exit("Error: File not found.")
        except OSError:
            sys.exit("Error: OS Error.")
        except Exception as e:
            sys.exit(f"Error: Unexpected error {repr(e)}")

    def printRawPuzzle(self):
        for line in self._lines:
            print(line, end="")

    def removeComments(self):
        commentPatten = re.compile("(#.*)|[\s]*[\n]")
        newLines = []
        for line in self._lines:
            newLine = re.sub(commentPatten, '', line)
            if newLine:
                newLines.append(newLine.strip())
        return newLines

    def getShape(self, newLines):
        self.shape = int(newLines[0].split()[0])
        if self._shape <= 2:
            sys.exit("Error: Shape cannot be lower than or equal to 2.")

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

    def flattenPuzzle(self, puzzleLines):
        if len(puzzleLines) != self.shape:
            sys.exit("Error: Wrong row shape.")
        for line in puzzleLines:
            try:
                row = [int(x) for x in line.split()]
            except ValueError:
                sys.exit("Error: Non numeric characters in puzzle.")
            if len(row) != self.shape:
                sys.exit("Error: Wrong column shape.")
            self.flattenedPuzzle += row
        for i in range(pow(self.shape, 2)):
            if i not in self.flattenedPuzzle:
                sys.exit("Error: Wrong numbers in puzzle.")

    def cleanPuzzle(self):
        newLines = self.removeComments()
        if len(newLines[0].split()) != 1:
            sys.exit("Error: Wrong format.")
        self.getShape(newLines)
        self.flattenPuzzle(newLines[1:])
