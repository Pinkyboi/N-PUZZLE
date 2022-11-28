from puzzle import PuzzleNode

from puzzleSolver import PuzzleSolver
from parser import Parser
from argumentHandler import getExectionParameters

if __name__ == "__main__":
    import time 
    
    start = time.time()
    execParameters  = getExectionParameters()
    parserIstance = Parser(execParameters.path)
    parserIstance.loadData()
    parserIstance.cleanPuzzle()
    start_puzzle = parserIstance.flattenedPuzzle
    # end_puzzle = [1, 2, 3, 4, 5, 16, 17, 18, 19, 6, 15, 24, 0, 20, 7, 14, 23, 22, 21, 8, 13, 12, 11, 10, 9]
    # end_puzzle = [1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7]
    end_puzzle = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    firstNode = PuzzleNode(start_puzzle, parserIstance.shape, None)
    endNode = PuzzleNode(end_puzzle, parserIstance.shape, None)
    # pes = PuzzleEndStates(firstNode.dim, snail)
    solver = PuzzleSolver(firstNode, endNode, execParameters.heuristic, execParameters.algorithm)
    goal = solver.solve()
    print("{}".format(time.time() - start))
    goal.printNode()
    i = 1
    while goal.parent:
        i += 1
        goal.parent.printNode()
        goal = goal.parent
    print(f"Number of moves: {i}")