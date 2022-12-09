
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

    def normalSearch(self):
        while not self._priorityQueue.empty():
            self._timeCoplexity += 1
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

    def idaStarSearch(self):
        minimumDepth = self._heuristic(self._startState, self._goalState)        
        while True:
            bound = minimumDepth
            minimumDepth = -1
            self._priorityQueue.put(self._startState)
            self._closedList = {}
            while not self._priorityQueue.empty():
                self._timeCoplexity += 1
                current_item = self._priorityQueue.get()
                if current_item.puzzle == self._goalState.puzzle:
                    return current_item
                if current_item.hash in self._closedList.keys()\
                    and current_item.cost >= self._closedList[current_item.hash].cost:
                    continue
                if current_item.cost > bound:
                    if current_item.cost < minimumDepth or minimumDepth == -1:
                        minimumDepth = current_item.cost
                    continue
                self._closedList[current_item.hash] = current_item
                childrenNodes = self.createChildrenNodes(current_item)
                for index in range(len(childrenNodes)):
                    childKey = childrenNodes[index].hash
                    if childKey in self._closedList.keys()\
                        and childrenNodes[index].cost >= self._closedList[childKey].cost:
                            continue
                    self._priorityQueue.put(childrenNodes[index])

    def solve(self):
        if self._algorithm == PuzzleSolver.idaStarSearchCost:
            return self.idaStarSearch()
        return self.normalSearch()

    def isSolvable(self):
        totalPermutation = 0
        gZeroIndex, sZeroIndex = self._goalState.puzzle.index(0), self._startState.puzzle.index(0)
        initialPermutation = PuzzleSolver.calculateManhatan(sZeroIndex, gZeroIndex, self._startState.dim)
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
    def aStarSearchCost(currentState, goalState, heuristic):
        return heuristic(currentState, goalState) + currentState.depth
    
    @staticmethod
    def idaStarSearchCost(currentState, goalState, heuristic):
        return heuristic(currentState, goalState) + currentState.depth

    @staticmethod
    def greedySearchCost(currentState, goalState, heuristic):
        return heuristic(currentState, goalState)

    @staticmethod
    def uniformSearchCost(currentState, goalState, heuristic):
        return currentState.depth

    @staticmethod
    def euclideanDistance(startState, goalState):  
        pDim = startState.dim
        for sIndex in range(len(startState.puzzle)):
            if startState[sIndex] != goalState[sIndex]:
                gIndex = goalState.puzzle.index(startState.puzzle[sIndex])
                xDistance = abs(sIndex // pDim - gIndex // pDim)
                yDistance = abs(sIndex % pDim - gIndex % pDim)
                score += sqrt(xDistance ** 2 + yDistance ** 2)
        return score

    @staticmethod
    def calculateManhatan(startIndex, goalIndex, dim):
        xDistance = abs(startIndex // dim - goalIndex // dim)
        yDistance = abs(startIndex % dim - goalIndex % dim)
        return xDistance + yDistance

    @staticmethod
    def manhatanDistance(startState, goalState):  
        pDim = startState.dim
        score = 0
        for sIndex in range(len(startState.puzzle)):
            if startState.puzzle[sIndex] != goalState.puzzle[sIndex]:
                gIndex = goalState.puzzle.index(startState.puzzle[sIndex])
                score += PuzzleSolver.calculateManhatan(sIndex, gIndex, pDim)
        return score

    @staticmethod
    def misplacedTile(startState, goalState):
        score = 0
        for i in range(len(startState.puzzle)):
            if startState.puzzle[i] != goalState.puzzle[i]:
                score += 1
        return score

    @staticmethod
    def gaschnig(startState, goalState):
        score = 0
        gaschnigPuzzle = startState.puzzle.copy()
        while gaschnigPuzzle != goalState.puzzle:
            sZeroIndex = gaschnigPuzzle.index(0)
            gZeroIndex = goalState.puzzle.index(0)
            if sZeroIndex != gZeroIndex:
                swapIndex = gaschnigPuzzle.index(goalState.puzzle[sZeroIndex])
                gaschnigPuzzle[sZeroIndex], gaschnigPuzzle[swapIndex] = gaschnigPuzzle[swapIndex], 0
            else:
                swapIndex = 0
                for i in range(len(gaschnigPuzzle)):
                    if gaschnigPuzzle[i] != goalState.puzzle[i]:
                        swapIndex = i
                        break
                gaschnigPuzzle[sZeroIndex], gaschnigPuzzle[swapIndex] = gaschnigPuzzle[swapIndex], 0
            score += 1
        return score

    @staticmethod
    def linearConflict(startState, goalState):
        score = 0
        for i in range(startState.dim):
            currentRow = startState.puzzle[i * startState.dim: i * startState.dim + startState.dim]
            goalRow = goalState.puzzle[i * startState.dim: i * startState.dim + startState.dim]
            currentColumn = startState.puzzle[i::startState.dim]
            goalColumn = goalState.puzzle[i::startState.dim]
            for j in range(startState.dim):
                if currentRow[j] in goalRow or currentColumn[j] in goalColumn:
                    for k in range(j, startState.dim):
                        if currentRow[k] in goalRow and goalRow[k] in currentRow[:j]:
                            score += 2
                        if currentColumn[k] in goalColumn and goalColumn[k] in currentColumn[:j]:
                            score += 2
        return score + PuzzleSolver.manhatanDistance(startState, goalState)

    @property
    def spaceComplexity(self):
        return self._spaceComplexity

    @property
    def timeComplexity(self):
        return self._timeCoplexity
