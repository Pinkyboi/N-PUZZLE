from puzzleSolver import PuzzleSolver
import puzzleGoalGenerator
import os, argparse, sys

def heuristicCheck(heuristic):
    if heuristic == 'Manhattan distance':
        return PuzzleSolver.manhatanDistance
    elif heuristic == 'Euclidean distance':
        return PuzzleSolver.euclideanDistance
    elif heuristic == 'Misplaced tile':
        return PuzzleSolver.misplacedTile
    elif heuristic == 'Gaschnig':
        return PuzzleSolver.gaschnig
    elif heuristic == 'Linear conflict':
        return PuzzleSolver.linearConflict
    else:
        sys.exit(f"Heuristic: {heuristic} is not a valid heuristic.")

def seachAlgorithmCheck(algorithm):
    if algorithm == 'A*':
        return PuzzleSolver.aStarSearch
    elif algorithm == 'Uniform':
        return PuzzleSolver.uniformSearch
    elif algorithm == "Greedy":
        return PuzzleSolver.greedySearch
    else:
        sys.exit(f"Algorithm: {algorithm} is not a valid search algorithm.")

def goalGeneratorCheck(goal):
    if goal == 'vertical':
        return puzzleGoalGenerator.verticalGoalState
    if goal == 'horizontal':
        return puzzleGoalGenerator.horizontalGoalState
    if goal == 'x_spiral':
        return puzzleGoalGenerator.xMajorSpiralGoalState
    if goal == 'y_spiral':
        return puzzleGoalGenerator.yMajorSpiralGoalState
    else:
        sys.exit(f"Goal State: {goal} is not a valid goal state.")

def file_path(path):
    if os.path.isfile(path):
        return path
    else:
        sys.exit(f"Path: {path} is not a valid path")

def getExectionParameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("--heuristic", type=heuristicCheck, default='Manhattan distance', help="The heuristic to use for the puzzle solver:-1: Manhattan distance\n-2: Euclidean distance\n-3: Misplaced tile\n-4: Gaschnig", required=False)
    parser.add_argument('--algorithm', type=seachAlgorithmCheck, default='A*', help="The search algorithm to use for the puzzle solver:-1: A*\n-2: Uniform\n-3: Greedy", required=False)
    parser.add_argument('--goal', type=goalGeneratorCheck, default='x_spiral', help="The search algorithm to use for the puzzle solver:-1: vertical\n-2: horizontal\n-3: x_spiral\n-4: y_spiral", required=False)
    parser.add_argument("-v", action="store_true", default=False , help="Visualize the solution", required=False)
    parser.add_argument("-p", "--path", type=file_path, help="Path to a puzzle file", required=True)
    return parser.parse_args()