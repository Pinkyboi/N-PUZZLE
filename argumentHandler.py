from puzzleSolver import PuzzleSolver
import puzzleGoalGenerator
import os, argparse

def heuristicCheck(heuristic):
    if heuristic == 'manhattan_distance':
        return PuzzleSolver.manhatanDistance
    elif heuristic == 'euclidean_distance':
        return PuzzleSolver.euclideanDistance
    elif heuristic == 'misplaced_tile':
        return PuzzleSolver.misplacedTile
    else:
        print(f"Heuristic: {heuristic} is not a valid heuristic")
        exit()

def seachAlgorithmCheck(algorithm):
    if algorithm == 'A*':
        return PuzzleSolver.aStarSearch
    elif algorithm == 'Djikstra':
        return PuzzleSolver.dijkstraSearch
    elif algorithm == "Greedy":
        return PuzzleSolver.greedySearch
    else:
        print(f"Algorithm: {algorithm} is not a valid search algorithm")
        exit()

def file_path(path):
    if os.path.isfile(path):
        return path
    else:
        print(f"Path: {path} is not a valid path")
        exit()

def getExectionParameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("--heuristic", type=heuristicCheck, default='manhattan_distance', help="The heuristic to use for the puzzle solver:-1: manhattan_distance\n-2: euclidean_distance\n-3: misplaced_tile", required=False)
    parser.add_argument('--algorithm', type=seachAlgorithmCheck, default='A*', help="The search algorithm to use for the puzzle solver:-1: A*\n-2: Djikstra\n-3: Greedy", required=False)
    parser.add_argument("-v", action="store_true", default=False , help="Visualize the solution", required=False)
    parser.add_argument("-p", "--path", type=file_path, help="Path to a puzzle file", required=True)
    return parser.parse_args()