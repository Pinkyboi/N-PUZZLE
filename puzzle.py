
class PuzzleNode():
    
    def __init__(self, puzzle, dim, parent=None):
        self._puzzle = puzzle
        self._hash = ''.join(str(x) for x in puzzle)
        self._dim = dim
        self._swap = 0
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
        return self._parent

    @property
    def depth(self):
        return self._depth

    @cost.setter
    def cost(self, value):
        self._cost = value

    def __lt__(self, other):
        return self.cost < other.cost

    @staticmethod
    def printPuzzle(puzzle, dim):
        for block in puzzle:
            print(f"|{block:>3}", end="{}".format('|\n' if (puzzle.index(block) + 1) % dim == 0 else ''))
        print()

    @property
    def hash(self):
        return self._hash

    @property
    def swap(self):
        return self._swap

    @swap.setter
    def swap(self, swap):
        self._swap = swap
