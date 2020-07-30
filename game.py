class Game:

    def createGame(self):
        pass

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
        for i in range(len(board)):
            if board[i][x] == n:
                return False
        # check in square
        # number between 0 and 2 to indicate the x square
        squareX = (x // 3) * 3
        squareY = (y // 3) * 3  # same for y square

        for i in range(squareY, squareY+3):
            for j in range(squareX, squareX+3):
                if board[i][j] == n:
                    return False

        return True
