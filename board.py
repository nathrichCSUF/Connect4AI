"""
FALL 2019 CPSC 481 Artificial Intelligence Project
File Description: board.py
    Class representing the gamme board

Authors:
    Nathaniel Richards
    Yash Bhambani
    Matthew Camarena
    Dustin Vuong

"""

import pygame
import slot as sl


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load_extended("")
        self.rect = self.image.get_rect()
        rows = 6
        columns = 7

        self.grid = [[sl.Slot(self.screen) for c in range(columns)] for r in range(rows)]
        # 2D Array Representing all Slots in Game Board

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update_slots(self): #update the board
        for slots in self.grid:
            slots.blit();