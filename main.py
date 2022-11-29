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
    # print("{}".format(time.time() - start))
    puzzleStates = []
    while goal.parent:
        puzzleStates.append(goal.puzzle)
        goal = goal.parent
    puzzleStates.append(firstNode.puzzle)
    vs = NpuzzleVisualizer(parserIstance.shape, puzzleStates[::-1], puzzleStart=firstNode.puzzle, windowDim=720)
    vs.startVisualization()