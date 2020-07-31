import numpy as np
import pygame
from board import Board


class Main:

    def __init__(self):
        pygame.init()

        self.game = Board(board_path="./boards/easy-boards.json")
        self.currentSelected = None

        self.HEIGHT = 450
        self.WIDTH = 450

        pygame.display.set_caption("Sudoku!")
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.backgound = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.backgound.fill(pygame.Color("#ffffff"))

        # FONTS
        self.numbersFont = pygame.font.SysFont('arial', 35)

        self.running = True
        self.clock = pygame.time.Clock()

    def drawGrid(self):
        """
        Draw the 9x9 grid.
        """
        resY = int(self.HEIGHT / 9)
        resX = int(self.WIDTH / 9)

        # border lines
        pygame.draw.line(self.backgound, (0, 0, 0),
                         (0, 0), (self.WIDTH, 0))
        pygame.draw.line(self.backgound, (0, 0, 0),
                         (0, self.HEIGHT), (self.WIDTH, self.HEIGHT))
        pygame.draw.line(self.backgound, (0, 0, 0),
                         (0, 0), (0, self.HEIGHT))
        pygame.draw.line(self.backgound, (0, 0, 0),
                         (self.WIDTH, 0), (self.WIDTH, self.HEIGHT))

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
                                 (self.WIDTH, y), 3)
                # vertical bold
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (x, 0),
                                 (x, self.HEIGHT), 3)
            else:
                # horizontal
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (0, y),
                                 (self.WIDTH, y))
                # vertical
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (x, 0),
                                 (x, self.HEIGHT))

            pygame.draw.line(self.screen, (0, 0, 0),
                             (x, 0),
                             (x, self.HEIGHT))

    def drawNumbers(self):
        """
        Draw the number on the grid.
        """

        resY = int(self.HEIGHT / 9)
        resX = int(self.WIDTH / 9)

        for i in range(9):
            for j in range(9):
                if self.game.board[i][j] == 0:
                    continue
                # the current number
                text = str(self.game.board[i][j])
                n = self.numbersFont.render(text, True, (0, 0, 0))

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

        resY = int(self.HEIGHT / 9)
        resX = int(self.WIDTH / 9)

        # a number between 0 and 8 to indicate the position in the outter array
        cellY = mouseY // resY
        # a number between 0 and 8 to indicate the position in the inner array
        cellX = mouseX // resX

        if (cellX, cellY) == self.currentSelected:
            self.currentSelected = None
        else:
            self.currentSelected = (cellX, cellY)

    def drawSelected(self):
        """
        Highlight the selected cell
        """

        resY = int(self.HEIGHT / 9)
        resX = int(self.WIDTH / 9)

        if self.currentSelected is not None:
            x, y = self.currentSelected

            xRec = x * resX
            yRec = y * resY

            pygame.draw.rect(self.screen, pygame.Color(
                "#74FF85"), pygame.Rect(xRec, yRec, resX, resY))

    def run(self):
        while self.running:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # check mouse clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selectCell(pygame.mouse.get_pos())

            self.screen.blit(self.backgound, (0, 0))

            self.drawSelected()
            self.drawGrid()
            self.drawNumbers()
            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()
