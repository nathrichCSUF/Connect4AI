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
    #Background Color
    BLACK = (0, 0, 0)
    BLUE = (0, 126, 231)
    def __init__(self):
        pygame.init()  # initialize pygame

        self.screen = pygame.display.set_mode((696, 700))  # screen size
        self.game_board = Board(self.screen)               # initialize Game board with screen size
        self.turn = "red"

    def play(self):

        self.update_screen()            #initialize window 
        self.game_board.load_board()
        pygame.display.update()
        self.game_board.check_win()
        gameover = False                # play until game is done
        while not gameover:
            
            for event in pygame.event.get(): # Events from player

                if event.type == pygame.QUIT: # Player chose to quit
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        #print("player decided to place here")
                        self.game_board.move(game.turn)
                        self.change_turn()
                        pygame.display.update()
                        self.game_board.check_win()
                        pygame.display.update()
                    elif event.key == pygame.K_a:
                        #print("Player moved left!")
                        self.game_board.move_button("left")
                        pygame.display.update()
                    elif event.key == pygame.K_s:
                        print("Player knowns nothing")
                    elif event.key == pygame.K_d:
                        #print("Player moved right!")
                        self.game_board.move_button("right")
                        pygame.display.update()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    # can be made in board


    def update_screen(self):
        self.screen.fill(game.BLUE)
        #self.game_board.blit() # call gameboard
        pygame.display.update() # update the entire screen = flip
                                        # display.update only updates 
                                        # the portion of the screen 
                                        # that was changed

    def change_turn(self):
        if game.turn is "red":
            game.turn = "yellow"
        else:
            game.turn = "red"


game = Game()
game.play()
