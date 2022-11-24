
class PuzzleSolver():

    def __init__(self, startState, goalState):
        self._startState = startState
        self._goalState = goalState
        if not self.isSolvable():
            raise Exception("The puzzle is not solvable")
    
    @staticmethod
    def manhatanDistance(startState, goalState , block):
        iIndex = startState.puzzle.index(block)    
        gIndex = goalState .puzzle.index(block)
        pLen = startState.len
        return abs(iIndex // pLen - gIndex // pLen) + abs(iIndex % pLen - gIndex % pLen)

    def isSolvable(self):
        total_permutation = 0
        initial_permutation = PuzzleSolver.manhatanDistance(self.startState, self.goalState, 0)
        while self.startState.puzzle != self.goalState.puzzle:
            for sBlock, gBlock  in zip(self.startState.puzzle, self.goalState.puzzle):
                if sBlock != gBlock:
                    currentIndex = self.startState.puzzle.index(sBlock)
                    swapIndex = self.startState.puzzle.index(gBlock)
                    self.startState.puzzle[currentIndex], self.startState.puzzle[swapIndex] = gBlock, sBlock
                    total_permutation += 1
        return initial_permutation % 2 == total_permutation % 2
                    

    @property
    def startState(self):
        return self._startState
    
    @property
    def goalState(self):
        return self._goalState
