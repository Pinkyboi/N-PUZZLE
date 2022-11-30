
from queue import PriorityQueue
from math import sqrt
from puzzle import PuzzleNode

class PuzzleSolver():

    def __init__(self, startState, goalState, heuristic, algorithm):
        self._startState = startState
        self._goalState = goalState
        self._heuristic = heuristic
        self._algorithm = algorithm
        self._priorityQueue = PriorityQueue()
        self._priorityQueue.put(self._startState)
        self._closedList = {}
        self._spaceComplexity = 0
        self._timeCoplexity = 0
        if not self.isSolvable():
            print("The puzzle is not solvable.")
            exit()

    def createChildrenNodes(self, parentPuzzle):
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
            newPuzzleNode = PuzzleNode(newPuzzle, dim, parentPuzzle)
            newPuzzleNode.swap = (axis, 1 if move - index > 0 else -1)
            newPuzzleNode.cost = self._algorithm(newPuzzleNode, self._goalState, self._heuristic)
            newPuzzles.append(newPuzzleNode)
            self._spaceComplexity += 1
        return newPuzzles

    def solve(self):
        while not self._priorityQueue.empty():
            current_item = self._priorityQueue.get()
            if current_item.puzzle == self._goalState.puzzle:
                return current_item
            if current_item.hash in self._closedList.keys()\
                and current_item.cost >= self._closedList[current_item.hash].cost:
                continue
            self._closedList[current_item.hash] = current_item
            childrenNodes = self.createChildrenNodes(current_item)
            for index in range(len(childrenNodes)):
                childKey = childrenNodes[index].hash
                if childKey in self._closedList.keys()\
                    and childrenNodes[index].cost >= self._closedList[childKey].cost:
                        continue
                self._priorityQueue.put(childrenNodes[index])
            self._timeCoplexity += 1

    def isSolvable(self):
        totalPermutation = 0
        initialPermutation = PuzzleSolver.manhatanDistance(self._startState, self._goalState, 0)
        testPuzzle = self._startState.puzzle.copy()
        while testPuzzle != self._goalState.puzzle:
            for sBlock, gBlock  in zip(testPuzzle, self._goalState.puzzle):
                if sBlock != gBlock:
                    currentIndex = testPuzzle.index(sBlock)
                    swapIndex = testPuzzle.index(gBlock)
                    testPuzzle[currentIndex], testPuzzle[swapIndex] = gBlock, sBlock
                    totalPermutation += 1
        return initialPermutation % 2 == totalPermutation % 2

    @staticmethod
    def aStarSearch(currentState, goalState, heuristic):
        return PuzzleSolver.calculateHeuristic(currentState, goalState, heuristic) + currentState.depth

    @staticmethod
    def greedySearch(currentState, goalState, heuristic):
        return PuzzleSolver.calculateHeuristic(currentState, goalState, heuristic)

    @staticmethod
    def uniformSearch(currentState, goalState, heuristic):
        return currentState.depth

    @staticmethod
    def calculateHeuristic(currentState, goalState, heuristic):
        return sum(heuristic(currentState, goalState, block) for block in currentState.puzzle)

    @staticmethod
    def euclideanDistance(startState, goalState, block):
        iIndex = startState.puzzle.index(block)    
        gIndex = goalState .puzzle.index(block)
        pLen = startState.dim
        xDistance = abs(iIndex // pLen - gIndex // pLen)
        yDistance = abs(iIndex % pLen - gIndex % pLen)
        return sqrt(xDistance ** 2 + yDistance ** 2)

    @staticmethod
    def manhatanDistance(startState, goalState , block):
        iIndex = startState.puzzle.index(block)    
        gIndex = goalState .puzzle.index(block)
        pLen = startState.dim
        return abs(iIndex // pLen - gIndex // pLen) + abs(iIndex % pLen - gIndex % pLen)

    @staticmethod
    def misplacedTile(startState, goalState, block):
        return 1 if startState.puzzle.index(block) != goalState.puzzle.index(block) else 0

    @property
    def spaceComplexity(self):
        return self._spaceComplexity

    @property
    def timeComplexity(self):
        return self._timeCoplexity
