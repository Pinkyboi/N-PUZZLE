from puzzle import PuzzleNode

from puzzleSolver import PuzzleSolver


if __name__ == "__main__":
    start_puzzle = [8, 1, 2, 0, 4, 3, 7, 6, 5]
    end_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    size = 3
    f_node = PuzzleNode(start_puzzle, size, None)
    e_node = PuzzleNode(end_puzzle, size, None)
    f_node.printNode()
    e_node.printNode()
    
    PuzzleSolver(f_node, e_node)