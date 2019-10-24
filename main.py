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
from board import Board


class Game:
    BLACK = (50, 94, 168)

    def __init__(self):
        pygame.init()  # initialize pygame
        self.screen = pygame.display.set_mode((680, 740))  # screen size
        self.game_board = Board(self.screen)
        

    def play(self):

        intro = True
        while intro:
            self.update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def update_screen(self):
        self.screen.fill(game.BLACK)
        self.game_board.blit()

        pygame.display.flip()


game = Game()
game.play()
