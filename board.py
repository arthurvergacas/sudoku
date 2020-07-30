import numpy as np
import random
import timeit
from game import Game


class Board(Game):
    """
    Class object to handle a single board as a game.
    Inherits Game

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
        new = []
        counter = 0

        def solve():
            """
            Recursively solves the board. 
            """
            nonlocal b, new, counter

            for i in range(9):
                for j in range(9):
                    if b[i][j] == 0:
                        # possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                        for k in range(1, 10):

                            # n = random.choice(possibles)
                            # possibles.remove(n)

                            if self.isPossible(b, i, j, k):
                                # counter += 1
                                # print((counter / 9**81) * 100, "%", end='\r')

                                b[i][j] = k
                                solve()
                                b[i][j] = 0

                        return

            # transform it in a numpy array because numpy arrays are immutable
            new = np.array(b)

        # call the function to solve board b
        solve()
        # return the solved board
        return new.tolist()


if __name__ == "__main__":
    grid = [[4, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 7, 8, 5],
            [0, 0, 7, 0, 4, 8, 0, 5, 0],
            [0, 0, 1, 3, 0, 0, 0, 0, 0],
            [0, 0, 6, 0, 7, 0, 0, 0, 0],
            [8, 6, 0, 0, 0, 0, 9, 0, 3],
            [7, 0, 0, 0, 0, 5, 0, 6, 2],
            [0, 0, 3, 7, 0, 0, 0, 0, 0]]

    game = Board(grid)

    start = timeit.default_timer()
    print(game.solveBoard())
    end = timeit.default_timer()
    elapsedTime = str("{:.6f}".format(end - start))
    print(elapsedTime)
