from puzzle import PuzzleNode

from puzzleSolver import PuzzleSolver
from parser import parser

if __name__ == "__main__":
    parserIstance = parser("puzzle.txt")
    parserIstance.loadData()
    parserIstance.cleanPuzzle()
    start_puzzle = parserIstance.flattenedPuzzle
    end_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    f_node = PuzzleNode(start_puzzle, parserIstance.shape, None)
    e_node = PuzzleNode(end_puzzle, parserIstance.shape, None)
    f_node.printNode()
    e_node.printNode()
    
    PuzzleSolver(f_node, e_node)