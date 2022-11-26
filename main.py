from puzzle import PuzzleNode

from puzzleSolver import PuzzleSolver
from parser import Parser
import argparse
import os

def heuristicCheck(heuristic):
    if heuristic == 0:
        heuristic = PuzzleSolver.manhatanDistance
    elif heuristic == 1:
        heuristic = PuzzleSolver.euclideanDistance
    elif heuristic == 2:
        heuristic = PuzzleSolver.misplacedTile
    else:
        print(f"heuristic:{heuristic} is not a valid heuristic")
        exit()
def file_path(path):
    if os.path.isfile(path):
        return path
    else:
        print(f"readable_dir:{path} is not a valid path")
        exit()

def getExectionParameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("--heuristic", type=heuristicCheck, default=0, help="The heuristic to use for the puzzle solver:-1: Manhattan Distance\n-2: Euclidean Distance\n-3: Misplaced Tile", required=False)
    parser.add_argument("-v", action="store_true", default=False , help="Visualize the solution", required=False)
    parser.add_argument("-p", "--path", type=file_path, help="Path to a puzzle file", required=True)
    return parser.parse_args()

if __name__ == "__main__":
    execParameters  = getExectionParameters()
    parserIstance = Parser(execParameters.path)
    parserIstance.loadData()
    parserIstance.cleanPuzzle()
    start_puzzle = parserIstance.flattenedPuzzle
    end_puzzle = [2, 1, 3,4,7,6,5,8, 9, 10, 11, 12, 13, 14, 15, 0]
    firstNode = PuzzleNode(start_puzzle, parserIstance.shape, None)
    endNode = PuzzleNode(end_puzzle, parserIstance.shape, None)
    solver = PuzzleSolver(firstNode, endNode, PuzzleSolver.manhatanDistance)
    newPuzzles = solver.createChildrenNodes(firstNode)
    firstNode.printNode()
    for puzzle in newPuzzles:
        puzzle.printNode()