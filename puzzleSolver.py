
from queue import PriorityQueue
from math import sqrt
from puzzle import PuzzleNode
class PuzzleSolver():

    def __init__(self, startState, goalState, heuristic):
        self._startState = startState
        self._goalState = goalState
        self._heuristic = heuristic
        self._priorityQueue = PriorityQueue()
        if not self.isSolvable():
            raise Exception("The puzzle is not solvable")


    def createChildrenStates(self, parentPuzzle):
        dim = parentPuzzle.dim
        index = parentPuzzle.puzzle.index(0)
        moves = [('x', index + 1), ('x', index - 1), ('y', index + dim), ('y', index - dim)]
        newPuzzles = []
        for axis, move in moves:
            if axis == 'x' and move // dim != index // dim:
                continue
            if move < 0 or move >= dim * dim:
                continue
            newPuzzle = parentPuzzle.puzzle.copy()
            newPuzzle[index], newPuzzle[move] = newPuzzle[move], newPuzzle[index]
            newPuzzles.append(PuzzleNode(newPuzzle, dim, parentPuzzle))
        return newPuzzles

    def isSolvable(self):
        totalPermutation = 0
        initialPermutation = PuzzleSolver.manhatanDistance(self.startState, self.goalState, 0)
        testPuzzle = self.startState.puzzle
        while testPuzzle != self.goalState.puzzle:
            for sBlock, gBlock  in zip(testPuzzle, self.goalState.puzzle):
                if sBlock != gBlock:
                    currentIndex = testPuzzle.index(sBlock)
                    swapIndex = testPuzzle.index(gBlock)
                    testPuzzle[currentIndex], testPuzzle[swapIndex] = gBlock, sBlock
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

    @staticmethod
    def misplacedTile(startState, goalState, block):
        return 1 if startState.puzzle.index(block) != goalState.puzzle.index(block) else 0

    def calculateHeuristic(self, currentState, goalState):
        return sum(self.heuristic(currentState, goalState, block) for block in currentState.puzzle)

    @property
    def startState(self):
        return self._startState
    
    @property
    def goalState(self):
        return self._goalState

    @property
    def currentState(self):
        return self._currentState

    @property
    def heuristic(self):
        return self._heuristic
