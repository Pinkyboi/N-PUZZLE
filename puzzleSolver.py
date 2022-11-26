
from queue import PriorityQueue
from math import sqrt
from puzzle import PuzzleNode

class PuzzleSolver():

    def __init__(self, startState, goalState, heuristic):
        self._startState = startState
        self._goalState = goalState
        self._heuristic = heuristic
        self._priorityQueue = PriorityQueue()
        self._priorityQueue.put(self._startState)
        self._closedList = {}
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
            g = newPuzzleNode.depth
            h = self.calculateHeuristic(newPuzzleNode, self.goalState)
            newPuzzleNode.cost = g + h
            newPuzzles.append(newPuzzleNode)
        return newPuzzles

    def solve(self):
        while not self._priorityQueue.empty():
            current_item = self._priorityQueue.get()
            if current_item.puzzle == self.goalState.puzzle: # todo: probably slow
                return current_item
            currentItemHash = hash(current_item)
            if currentItemHash in self.closedList.keys()\
                and current_item.cost >= self._closedList[currentItemHash].cost:
                continue
            self.closedList[currentItemHash] = current_item
            childrenNodes = self.createChildrenNodes(current_item)
            for index in range(len(childrenNodes)):
                childHash = hash(childrenNodes[index])
                if childHash in self.closedList.keys()\
                    and childrenNodes[index].cost >= self.closedList[childHash].cost:
                        continue
                self._priorityQueue.put(childrenNodes[index])

    def isSolvable(self):
        totalPermutation = 0
        initialPermutation = PuzzleSolver.manhatanDistance(self.startState, self.goalState, 0)
        testPuzzle = self.startState.puzzle.copy()
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
        pLen = len(startState.puzzle)
        xDistance = abs(iIndex // pLen - gIndex // pLen)
        yDistance = abs(iIndex % pLen - gIndex % pLen)
        return sqrt(xDistance ** 2 + yDistance ** 2)

    @staticmethod
    def manhatanDistance(startState, goalState , block):
        iIndex = startState.puzzle.index(block)    
        gIndex = goalState .puzzle.index(block)
        pLen = len(startState.puzzle)
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

    @property
    def closedList(self):
        return self._closedList


