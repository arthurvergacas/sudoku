import numpy as np
import pygame
from board import Board


class Main:

    def __init__(self):
        self.currentBoard = Board(difficulty=2)

        self.HEIGHT = 450
        self.WIDTH = 450

        pygame.display.set_caption("Sudoku!")
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.backgound = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.backgound.fill(pygame.Color("#ffffff"))

        self.running = True
        self.clock = pygame.time.Clock()

    def drawGrid(self):
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

        # 8 because I want to draw the border lines ou of the loop
        for i in range(8):
            # horizontal lines
            y = i * resY + resY
            # vertical lines
            x = i * resX + resX
            if (i + 1) % 3 == 0:
                # horizontal bold
                pygame.draw.line(self.backgound, (0, 0, 0),
                                 (0, y),
                                 (self.WIDTH, y), 3)
                # vertical bold
                pygame.draw.line(self.backgound, (0, 0, 0),
                                 (x, 0),
                                 (x, self.HEIGHT), 3)
            else:
                # horizontal
                pygame.draw.line(self.backgound, (0, 0, 0),
                                 (0, y),
                                 (self.WIDTH, y))
                # vertical
                pygame.draw.line(self.backgound, (0, 0, 0),
                                 (x, 0),
                                 (x, self.HEIGHT))

            pygame.draw.line(self.backgound, (0, 0, 0),
                             (x, 0),
                             (x, self.HEIGHT))

    def run(self):
        while self.running:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(self.backgound, (0, 0))
            self.drawGrid()
            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()
