

#this is a class representing one node of n puzzle

class PuzzleNode():
    
    def __init__(self, puzzle, dim, parent=None):
        self._puzzle = puzzle
        self._dim = dim
        self._parent = parent
        self._depth = parent.depth + 1 if parent != None else 0
        self._cost = 0

    @property
    def cost(self):
        return self._cost
    
    @property
    def dim(self):
        return self._dim

    @property
    def puzzle(self):
        return self._puzzle

    @property
    def parent(self):
        return self.parent

    @property
    def depth(self):
        return self._depth

    @cost.setter
    def cost(self, value):
        self._cost = value

    def _lt_(self, other):
        return self.cost < other.cost

    def printNode(self):
        for block in self.puzzle:
            print(f"|{block:>3}", end="{}".format('|\n' if (self.puzzle.index(block) + 1) % self.dim == 0 else ''))
        print()
