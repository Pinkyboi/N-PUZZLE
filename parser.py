
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
        self._shape = int(newLines[0].split()[0])
        if self._shape <= 2:
            print("Error: Shape cannot be lower than 2.")
            exit()

    @property
    def shape(self):
        return self._shape

    @property
    def flattenedPuzzle(self):
        return self._flattenedPuzzle

    def flattenPuzzle(self, puzzleLines):
        for line in puzzleLines:
            row = [int(x) for x in line.split()]
            if len(row) != self._shape:
                print("Error: Wrong format.1")
                exit()
            self._flattenedPuzzle += row
        for i in range(pow(self._shape, 2)):
            if i not in self._flattenedPuzzle:
                print("Error: Wrong numbers in puzzle.")
                exit()

    def cleanPuzzle(self):
        newLines = self.removeComments()
        if len(newLines[0].split()) != 1:
            print("Error: Wrong format.")
            exit()
        self.getShape(newLines)
        self.flattenPuzzle(newLines[1:])

        
if __name__ == "__main__":
    p = Parser("puzzle.txt")
    p.loadData()
    # p.printRawPuzzle()
    p.cleanPuzzle()
    print(p._flattenedPuzzle)