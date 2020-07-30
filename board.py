import numpy as np
import random
import timeit


class Board:
    """
    Class object to handle a single board as a game.
    Inherits Game

    Args:
        board (array): A 2 dimensional array (9, 9) representing the board. Empty spaces are represented with zeros. 
    """

    def __init__(self, board=None):
        self.board = self.createBoard(30) if board is None else board

    def isPossible(self, board, y, x, n):
        """
        Checks if a given number in given positions on a given board is possible

        Args:
            board (array): A 2 dimensional array that contains the board
            y (int): The line position
            x (inte): The column postion
            n (int): The number from 1 to 9 that check against the board in the postion

        Returns:
            boolean: True if it is possible, otherwise returns False
        """

        # check in line
        for i in board[y]:
            if i == n:
                return False

        # check in column
        for i in range(9):
            if board[i][x] == n:
                return False

        # check in square
        # number between 0 and 2 to indicate the x square
        squareX = (x // 3) * 3
        # same for y square
        squareY = (y // 3) * 3

        for i in range(squareY, squareY+3):
            for j in range(squareX, squareX+3):
                if board[i][j] == n:
                    return False

        return True

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

    def createBoard(self, starter_nums):

        board = []

        def create():
            new = np.zeros((9, 9), dtype=int).tolist()

            for i in range(starter_nums):
                # pick random row, collumn and number to fill a cell
                row = np.random.randint(0, 9)
                col = np.random.randint(0, 9)
                num = np.random.randint(1, 10)

                # while the current spot is not avilable, keep picking
                while (not self.isPossible(new, row, col, num) or new[row][col] != 0):
                    row = np.random.randint(0, 9)
                    col = np.random.randint(0, 9)
                    num = np.random.randint(1, 10)

                # assign the number to the cell
                new[row][col] = num
            return new

        # check if game is possible and if not, redo the process
        possible = False
        tests = 0
        while (not possible):
            try:
                self.board = create()
                board = self.board[:]
                self.solveBoard()
                possible = True
            except AttributeError:
                tests += 1
                print(tests, end="\r")
                possible = False

        return board


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

    game = Board()
    print(np.array(game.board))
    print(np.array(game.solveBoard()))
