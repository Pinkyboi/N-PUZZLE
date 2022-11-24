
from math import sqrt
class PuzzleSolver():

    def __init__(self, startState, goalState):
        self._startState = startState
        self._goalState = goalState
        if not self.isSolvable():
            raise Exception("The puzzle is not solvable")

    def isSolvable(self):
        totalPermutation = 0
        initialPermutation = PuzzleSolver.manhatanDistance(self.startState, self.goalState, 0)
        puzzle = self.startState.puzzle
        while puzzle != self.goalState.puzzle:
            for sBlock, gBlock  in zip(puzzle, self.goalState.puzzle):
                if sBlock != gBlock:
                    currentIndex = puzzle.index(sBlock)
                    swapIndex = puzzle.index(gBlock)
                    puzzle[currentIndex], puzzle[swapIndex] = gBlock, sBlock
                    totalPermutation += 1
        return initialPermutation % 2 == totalPermutation % 2
                    
    @staticmethod
    def euclideanDistance(startState, goalState, block):
        iIndex = startState.puzzle.index(block)    
        gIndex = goalState .puzzle.index(block)
        pLen = startState.len
        xDistance = abs(iIndex // pLen - gIndex // pLen)
        yDistance = abs(iIndex % pLen - gIndex % pLen)
        return sqrt(xDistance ** 2 + yDistance ** 2)

    @staticmethod
    def manhatanDistance(startState, goalState , block):
        iIndex = startState.puzzle.index(block)    
        gIndex = goalState .puzzle.index(block)
        pLen = startState.len
        return abs(iIndex // pLen - gIndex // pLen) + abs(iIndex % pLen - gIndex % pLen)

    @property
    def startState(self):
        return self._startState
    
    @property
    def goalState(self):
        return self._goalState
