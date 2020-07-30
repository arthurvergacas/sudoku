import numpy as np
from game import Game


class Board(Game):
    """
    Class object to handle a single board as a game.

    Args:
        board (array): A 2 dimensional array (9, 9) representing the board. Empty spaces are represented with zeros. 
    """

    def __init__(self, board):
        self.board = board

    def solveBoard(self):
        """
        Nested function that solves a given sudoku board.  

        Returns:
            array: A solved board.
        """

        # stores the board in a local varibale, so it can be used by nonlocal
        b = self.board.copy()
        # initialize the new variable to receive the value of the solved board
        new = []

        def solve():
            """
            Recursively solves the board. 
            """
            nonlocal b, new

            for i in range(9):
                for j in range(9):
                    if b[i][j] == 0:
                        for k in range(1, 10):
                            if self.isPossible(b, i, j, k):
                                b[i][j] = k
                                solve()
                                b[i][j] = 0
                        return

            new = b.copy()

        # call the function to solve board b
        solve()
        # return the solved board
        return new


if __name__ == "__main__":
    grid = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                     [6, 0, 0, 1, 9, 5, 0, 0, 0],
                     [0, 9, 8, 0, 0, 0, 0, 6, 0],
                     [8, 0, 0, 0, 6, 0, 0, 0, 3],
                     [4, 0, 0, 8, 0, 3, 0, 0, 1],
                     [7, 0, 0, 0, 2, 0, 0, 0, 6],
                     [0, 6, 0, 0, 0, 0, 2, 8, 0],
                     [0, 0, 0, 4, 1, 9, 0, 0, 5],
                     [0, 0, 0, 0, 8, 0, 0, 7, 9]], ndmin=2)

    game = Board(grid)

    print(game.solveBoard())
