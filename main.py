from puzzle import PuzzleNode
from puzzleSolver import PuzzleSolver
from visualizer import NpuzzleVisualizer
from parser import Parser
from argumentHandler import getExectionParameters
import time


if __name__ == "__main__":
    execParameters  = getExectionParameters()
    parserIstance = Parser(execParameters.path)
    parserIstance.loadData()
    parserIstance.cleanPuzzle()
    start_puzzle = parserIstance.flattenedPuzzle
    firstNode = PuzzleNode(start_puzzle, parserIstance.shape, None)
    endNode = PuzzleNode(execParameters.goal(parserIstance.shape), parserIstance.shape, None)
    solver = PuzzleSolver(firstNode, endNode, execParameters.heuristic, execParameters.algorithm)
    start = time.time()
    goal = solver.solve()
    puzzleStates = []
    while goal:
        puzzleStates.append(goal.puzzle)
        goal = goal.parent
    puzzleStates.reverse()
    if execParameters.v:
        vs = NpuzzleVisualizer(parserIstance.shape, puzzleStates, 1000)
        vs.startVisualization()
    else:
        for puzzle in puzzleStates:
            if puzzle == puzzleStates[-1]:
                PuzzleNode.printPuzzle(puzzle, parserIstance.shape)
                print("--------------------------------------------")
                print("Goal State !")
                print("--------------------------------------------")
                print(f"-Time taken: {time.time() - start}")
                print(f"-Number of moves: {len(puzzleStates) - 1}")
                print(f"-Time Complexity: {solver.timeComplexity}")
                print(f"-Space Complexity: {solver.spaceComplexity}")
                print("--------------------------------------------")

            else:
                PuzzleNode.printPuzzle(puzzle, parserIstance.shape)