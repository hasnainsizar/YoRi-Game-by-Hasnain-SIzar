# import required modules/classes
import pygame
import os


class Board:
    """
    The Board class encapsulates the properties and behavior of the game board.
    Attributes:
    board_img : pygame.Surface
    The image of the game board, initialized to the YoRi board image.
    """
    def __init__(self):
        # load the board image
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, 'Ludo-Game-Board-Vector-Free.png')
        self.board_image = pygame.image.load(image_path)
        self.board_image = pygame.transform.scale(self.board_image, (700, 700))

    def draw_board(self, screen):
        """
        Draws the game board on the game screen.
        Parameters:
        ----------
        screen : pygame.Surface
            The game screen.
        Returns: None
        """
        screen.blit(self.board_image, (0, 0))
