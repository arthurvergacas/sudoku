import numpy as np


class Game:

    def createBoard(self):
        """
        Nested function that solves a given sudoku board.

        Returns:
            array: A solved board.
        """

        # stores the board in a local varibale, so it can be used by nonlocal
        b = np.zeros((9, 9), dtype=int)
        # initialize the new variable to receive the value of the solved board
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
                        for k in range(1, 10):
                            if self.isPossible(b, i, j, k):
                                counter += 1
                                print((counter / 9**81) * 100, "%", end='\r')
                                b[i][j] = k
                                solve()
                                b[i][j] = 0
                        return

            new = b.copy()

        # call the function to solve board b
        solve()
        # return the solved board
        return new

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


if __name__ == "__main__":
    game = Game()
    game.createBoard()
