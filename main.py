from puzzle import PuzzleNode
from puzzleSolver import PuzzleSolver
from visualizer import NpuzzleVisualizer
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
    firstNode = PuzzleNode(start_puzzle, parserIstance.shape, None)
    endNode = PuzzleNode(execParameters.goal(parserIstance.shape), parserIstance.shape, None)
    solver = PuzzleSolver(firstNode, endNode, execParameters.heuristic, execParameters.algorithm)
    goal = solver.solve()
    print("{}".format(time.time() - start))
    goal.printNode()
    i = 1
    swaps = []
    while goal.parent:
        i += 1
        swaps.append(goal.swap)
        goal.parent.printNode()
        print(goal.parent._swap, "this is the swap and this is goal swa", goal.swap)
        goal = goal.parent
    print(f"Number of moves: {i}")
    print(len(swaps[::-1]))
    vs = NpuzzleVisualizer(parserIstance.shape, swaps, puzzleStart=firstNode.puzzle, windowDim=720)
    vs.startVisualization()