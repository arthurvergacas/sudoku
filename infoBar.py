import pygame
import pygame_gui


class InfoBar:
    """
    Handles the info bar below the board.

    Args:
        game (Board object): The current game, so the class can keep track of game information.
        screen (Pygame Surface): The screen to draw the UI elements.
    """

    def __init__(self, game, screen):

        self.game = game
        self.screen = screen
