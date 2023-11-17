#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

# import required modules/classes
import pygame
from New_YoRi import YoRi

# screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 670

# board dimensions
BOARD_WIDTH = 800
BOARD_HEIGHT = 800

# Initialize
pygame.init()

# dimensions of a ludo piece
piece_size = (35, 35)

# Set up the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("YoRi Board")

# pass the screen window as the argument
game = YoRi(screen)
game.main_menu()
