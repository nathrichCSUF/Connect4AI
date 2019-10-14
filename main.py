"""
FALL 2019 CPSC 481 Artificial Intelligence Project
File Description: main.py
    Main game file for Connect 4AI Project

Authors:
    Nathaniel Richards
    Yash Bhambani
    Matthew Camarena
    Dustin Vuong

"""

import pygame


class Game:
    def __init__(self):
        pygame.init()  # initialize pygame
        self.screen = pygame.display.set_mode((680, 740))  # screen size
