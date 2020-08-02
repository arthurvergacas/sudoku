import numpy as np
import pygame
from board import Board


class Main:

    def __init__(self):
        pygame.init()

        self.game = Board(board_path="./boards/easy-boards.json")

        self.solvedBoard = self.game.solveBoard()

        # copy the board to a new array to keep track of things
        self.originalBoard = np.zeros((9, 9), dtype=int).tolist()
        for i in range(9):
            for j in range(9):
                self.originalBoard[i][j] = self.game.board[i][j]

        # the board to keep track of the pencil numbers
        self.pencilBoard = np.zeros((9, 9), dtype=int).tolist()

        self.currentSelected = None

        # WINDOW DIMENSIONS
        self.WIDTH = 450
        self.HEIGHT = 525

        # BOARD DIMENSIONS
        self.BOARD_HEIGHT = 450
        self.BOARD_WIDTH = 450

        pygame.display.set_caption("Sudoku!")
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(pygame.Color("#A7B3A1"))

        self.backgound = pygame.Surface((self.WIDTH, self.BOARD_HEIGHT))
        self.backgound.fill(pygame.Color("#ffffff"))

        # FONTS
        self.numbersFont = pygame.font.SysFont('arial', 35)

        self.running = True
        self.clock = pygame.time.Clock()

    def drawGrid(self):
        """
        Draw the 9x9 grid.
        """
        resY = int(self.BOARD_HEIGHT / 9)
        resX = int(self.BOARD_WIDTH / 9)

        # border lines
        pygame.draw.line(self.backgound, (0, 0, 0),
                         (0, 0), (self.BOARD_WIDTH, 0))
        pygame.draw.line(self.screen, (0, 0, 0),
                         (0, self.BOARD_HEIGHT), (self.BOARD_WIDTH, self.BOARD_HEIGHT), 3)
        pygame.draw.line(self.backgound, (0, 0, 0),
                         (0, 0), (0, self.BOARD_HEIGHT))
        pygame.draw.line(self.backgound, (0, 0, 0),
                         (self.BOARD_WIDTH, 0), (self.BOARD_WIDTH, self.BOARD_HEIGHT))

        # 8 because I want to draw the border lines out of the loop
        for i in range(8):
            # horizontal lines
            y = i * resY + resY
            # vertical lines
            x = i * resX + resX
            if (i + 1) % 3 == 0:
                # horizontal bold
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (0, y),
                                 (self.BOARD_WIDTH, y), 3)
                # vertical bold
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (x, 0),
                                 (x, self.BOARD_HEIGHT), 3)
            else:
                # horizontal
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (0, y),
                                 (self.BOARD_WIDTH, y))
                # vertical
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (x, 0),
                                 (x, self.BOARD_HEIGHT))

            pygame.draw.line(self.screen, (0, 0, 0),
                             (x, 0),
                             (x, self.BOARD_HEIGHT))

    def drawNumbers(self):
        """
        Draw the number on the grid.
        """

        resY = int(self.BOARD_HEIGHT / 9)
        resX = int(self.BOARD_WIDTH / 9)

        for i in range(9):
            for j in range(9):

                # the main board
                if self.game.board[i][j] != 0:
                    # the current number
                    text = str(self.game.board[i][j])
                    if self.originalBoard[i][j] != 0:
                        n = self.numbersFont.render(
                            text, True, pygame.Color("#B32D32"))
                    else:
                        n = self.numbersFont.render(
                            text, True, pygame.Color("#000000"))

                    # to center the number
                    x, y = self.numbersFont.size(text)

                    yPos = int((i * resY + resY / 2) - y / 2)
                    xPos = int((j * resX + resX / 2) - x / 2)

                    self.screen.blit(n, (xPos, yPos))

                # the pencil board
                if self.pencilBoard[i][j] != 0:
                    # the current number
                    text = str(self.pencilBoard[i][j])
                    n = self.numbersFont.render(
                        text, True, pygame.Color("#8C8C8C"))

                    # to center the number
                    x, y = self.numbersFont.size(text)

                    yPos = int((i * resY + resY / 2) - y / 2)
                    xPos = int((j * resX + resX / 2) - x / 2)

                    self.screen.blit(n, (xPos, yPos))

    def selectCell(self, mouse_pos):
        """
        Select a cell from the grid. If the cell is already selected, deselect it.

        Args:
            mouse_pos (tuple of integers): The x and y positions of the mouse. e.g. selectCell(pygame.mouse.get_pos())
        """

        mouseX, mouseY = mouse_pos

        resY = int(self.BOARD_HEIGHT / 9)
        resX = int(self.BOARD_WIDTH / 9)

        # a number between 0 and 8 to indicate the position in the outter array
        cellY = mouseY // resY
        # a number between 0 and 8 to indicate the position in the inner array
        cellX = mouseX // resX

        if (cellX, cellY) == self.currentSelected:
            self.currentSelected = None
        else:
            self.currentSelected = (cellX, cellY)

    def moveSelected(self, direction):
        """
        Move the selected cell in the grid.

        Args:
            direction (str): The direction to move. Can be: "up", "down", "right", or "left".
        """

        x, y = self.currentSelected

        canMove = False
        offset = 1

        if direction == "up":
            if y != 0:
                self.currentSelected = (x, y - offset)

        elif direction == "down":
            if y != 8:
                self.currentSelected = (x, y + offset)

        elif direction == "right":
            if x != 8:
                self.currentSelected = (x + offset, y)
        elif direction == "left":
            if x != 0:
                self.currentSelected = (x - offset, y)

    def highlightCell(self, pos, color):
        """
        Highlight a cell in a given postion with a given color

        Args:
            pos (int): A tuple containing x and y coordinates in the array. e.g. (3, 2)
            color (Pygame Color Object / tuple of three int): The color to highlight the cell. Can be either a Pygame Color Object or a tuple, like (255, 255, 255)
        """

        resY = int(self.BOARD_HEIGHT / 9)
        resX = int(self.BOARD_WIDTH / 9)

        x, y = pos

        xRec = x * resX
        yRec = y * resY

        pygame.draw.rect(self.screen, color,
                         pygame.Rect(xRec, yRec, resX, resY))

    def drawSelected(self):
        """
        Highlight the selected cell
        """

        resY = int(self.BOARD_HEIGHT / 9)
        resX = int(self.BOARD_WIDTH / 9)

        if self.currentSelected is not None:
            self.highlightCell(self.currentSelected, pygame.Color(
                "#73FF98"))

    def drawAllEqual(self):
        """
        Highlight the cells that contain the same number in the selected cell.
        """

        if self.currentSelected is not None:
            x, y = self.currentSelected
            curr = self.game.board[y][x]

            if curr != 0:
                for i in range(9):
                    for j in range(9):
                        if self.game.board[i][j] == curr:
                            self.highlightCell((j, i), pygame.Color("#AEFFAB"))

    def setNumber(self, num):
        """
        Receive a number and set the current selected cell to this number.

        Args:
            num (int): The number to be set
        """

        x, y = self.currentSelected
        if self.originalBoard[y][x] == 0:
            if self.pencilBoard[y][x] != 0:
                self.pencilBoard[y][x] = 0
            self.game.board[y][x] = num

    def pencilNumber(self, num):
        """
        Receive a number and set it to temporary number. Mark the number as a "pencil".

        Args:
            num (int): The number to be set
        """

        x, y = self.currentSelected
        if self.originalBoard[y][x] == 0:
            if self.game.board[y][x] != 0:
                self.game.board[y][x] = 0
            self.pencilBoard[y][x] = num

    def validateBoard(self):
        """
        Validates the current board.

        Returns:
            boolean: True if the game is valid, False if invalid.
        """

        filled = True
        # check if there are any spot still available
        for i in range(9):
            for j in range(9):
                if self.game.board[i][j] == 0:
                    filled = False

        if filled:
            for i in range(9):
                for j in range(9):
                    # if any of the game board's numbers is different from the solved board, return False
                    if self.solvedBoard[i][j] != self.game.board[i][j]:
                        return False
            # if didn't returned False, return True
            return True
        else:
            return None

    def run(self):
        while self.running:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # handle mouse clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selectCell(pygame.mouse.get_pos())

                # handle keys pressed
                if event.type == pygame.KEYDOWN:
                    if self.currentSelected is not None:
                        if event.key == pygame.K_BACKSPACE:
                            self.setNumber(0)
                        elif event.key == pygame.K_UP:
                            self.moveSelected("up")
                        elif event.key == pygame.K_DOWN:
                            self.moveSelected("down")
                        elif event.key == pygame.K_RIGHT:
                            self.moveSelected("right")
                        elif event.key == pygame.K_LEFT:
                            self.moveSelected("left")
                        else:
                            try:
                                if event.mod == pygame.KMOD_NONE:
                                    # set the number pressed
                                    self.setNumber(
                                        int(pygame.key.name(event.key)))
                                else:
                                    if event.mod & pygame.KMOD_LSHIFT:
                                        # set the number as drawn with a pencil
                                        self.pencilNumber(
                                            int(pygame.key.name(event.key)))
                            except Exception:
                                pass
            self.screen.blit(self.backgound, (0, 0))

            # GAME LOGIC
            isWon = self.validateBoard()
            if isWon is not None and isWon == True:
                # what happens when you win the game?
                print("WON!")

            # HIGHLIGHTS
            self.drawAllEqual()
            self.drawSelected()

            # GAME UI
            self.drawGrid()
            self.drawNumbers()

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()
