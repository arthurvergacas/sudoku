import numpy as np
import pygame
from board import Board


class Main:

    def __init__(self):
        self.currentBoard = Board()

        self.HEIGHT = 450
        self.WIDTH = 450

        pygame.display.set_caption("Sudoku!")
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.backgound = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.backgound.fill(pygame.Color("#ffffff"))

        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(self.backgound, (0, 0))

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()
