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
from settings import Settings
from menu import Menu

class Game:
    #Background Color
    BLACK = (0, 0, 0)
    BLUE = (0, 126, 231) # 007EE7 hex number
    def __init__(self):
        pygame.init()  # initialize pygame
        self.red_selector = pygame.image.load("button-red.png")
        self.screen = pygame.display.set_mode((696, 700))  # screen size
        self.game_board = Board(self.screen)               # initialize Game board with screen size
        self.settings = Settings()
        self.menu = Menu(self.screen)
        self.turn = "red"

    def play(self):


        won = False
        gameover = False                # play until game is done
        while not gameover:
            if won:
                okten = 100000
                while okten > 0:
                    print(str(okten))
                    okten = okten -1
                self.settings.toggle_game_active()
                pygame.mouse.set_visible(True)
                won = False

            if self.settings.gameActive:
                for event in pygame.event.get(): # Events from player

                    if event.type == pygame.QUIT: # Player chose to quit
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            #print("player decided to place here")
                            if self.game_board.check_valid_move():
                                self.game_board.move(game.turn)
                                pygame.display.update()

                                if self.game_board.check_win(game.turn): 
                                    pygame.display.update()
                                    pygame.event.pump()
                                    won = True
                                    
                                self.change_turn()
                        elif event.key == pygame.K_a:
                            #   print("Player moved left!")
                            self.game_board.move_select_button("left")
                            pygame.display.update()
                        elif event.key == pygame.K_s:
                            print("Player knowns nothing")
                        elif event.key == pygame.K_d:
                            #   print("Player moved right!")
                            self.game_board.move_select_button("right")
                            pygame.display.update()
                        elif event.key == pygame.K_q:
                            pygame.quit()
                            quit()
            else:
                
                self.menu.draw_menu()
                pygame.display.update()
                for event in pygame.event.get(): # Events from player

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        self.menu.checkForPlayButtonClick(mouse_x,mouse_y,self.settings)
                        if self.settings.gameActive:
                            self.update_screen()  # initialize window
                            self.game_board.reset_game()
                            self.game_board.load_board()
                            


                    # can be made in board



    def update_screen(self):
        self.screen.fill(game.BLUE)
        #self.game_board.blit() # call gameboard
        self.game_board.load_board()
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
