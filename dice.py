# import required modules/classes
import pygame
import random
import os


class Dice:
    """
    Dice class encapsulates the properties and behavior of a dice in the game.

    Attributes:
    ----------
    value : int
    The face value of the dice, initialized to 1.
    """
    def __init__(self):
        self.dice_images = []
        current_dir = os.path.dirname(__file__)
        for i in range(1, 7):
            image_path = os.path.join(current_dir, f"dice-{i}.png")
            image = pygame.image.load(image_path)
            resized_image = pygame.transform.scale(image, (80, 80))
            self.dice_images.append(resized_image)
            self.value = 1

    def draw_dice(self, screen):
        """
        Draws the dice on the game screen.
        Parameters:
        screen : pygame.Surface
        The game screen.
        Returns: None
        """
        screen.blit(self.dice_images[self.value - 1], (310, 294))

    def roll_dice(self):
        """
        Simulates the rolling of a dice, generating a random number between 1 and 6.
        Returns:
        None
        """
        self.value = random.randint(1, 6)
        return self.value
