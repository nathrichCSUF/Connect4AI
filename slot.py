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
        self.image = pygame.image.load("black.png")
        self.rect = self.image.get_rect()

    def change_state(self, color):  # Change color of coin
        self.state = color
        self.image = pygame.image.load(self.state + ".png")

    def set_slot_position(self, x, y):  # Set position of slot within the grid
        self.rect.x = x
        self.rect.y = y
        #print("slot position x: " + str(x) + " y: " + str(y))

    def get_slot_position_x(self):
        return self.rect.x

    def get_slot_position_y(self):
        return self.rect.y

    # Blit Coin to Screen
    def blit(self):  
        #print(str(self.rect) + " < - blit coin")
        self.screen.blit(self.image, self.rect)

