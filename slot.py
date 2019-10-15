"""
FALL 2019 CPSC 481 Artificial Intelligence Project
File Description: slot.py
    Class representing a slot in the Connect Four Game Grid

Authors:
    Nathaniel Richards
    Yash Bhambani
    Matthew Camarena
    Dustin Vuong

"""

import pygame


class Slot:
    def __init__(self, screen):
        self.screen = screen
        self.state = "black"  # String holding state of coin, is it red, yellow, or black(empty)
        self.image = pygame.image.load_extended("black.png")
        self.rect = self.image.get_rect()

    def change_state(self, color):  # Change color of coin
        self.state = color
        self.image = pygame.image.load_extended("images/" + self.state + ".png")

    def set_slot_position(self, x, y):  # Set position of slot within the grid
        self.rect.x = x
        self.rect.y = y

    def blit(self):  # Blit Coin to Screen
        self.screen.blit(self.image, self.rect)