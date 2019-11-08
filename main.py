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
import time
import random
import argparse
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
        #self.turn = "red"
        self.player = 1
    def play(self):


       
        gameover = False                # play until game is done
        while not gameover:

            if self.settings.gameActive is "pvp":
                for event in pygame.event.get(): # Events from player

                    if event.type == pygame.QUIT: # Player chose to quit
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            #print("player decided to place here")
                            if self.game_board.check_valid_move():
                                self.game_board.move()
                                pygame.display.update()

                                if self.game_board.check_win(): 
                                    pygame.display.update()
                                    pygame.event.pump()
                                    time.sleep(2)
                                    self.settings.toggle_game_active()
                                    pygame.mouse.set_visible(True)
                                    #blit win thing too?
                                if self.game_board.move_count is 42:
                                    pygame.event.pump()                                    #blit tie game
                                    time.sleep(2)
                                    self.settings.toggle_game_active()
                                    pygame.mouse.set_visible(True)

                                self.game_board.change_turn()
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
            elif self.settings.gameActive is "pvai":
                if self.player:
                    for event in pygame.event.get(): # Events from player

                        if event.type == pygame.QUIT: # Player chose to quit
                            pygame.quit()
                            quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_w:
                                #print("player decided to place here")
                                if self.game_board.check_valid_move():
                                    self.game_board.move()
                                    pygame.display.update()
                                    pygame.event.pump() 
                                    if self.game_board.check_win(): 
                                        pygame.display.update()
                                        pygame.event.pump()
                                        time.sleep(2)
                                        self.settings.toggle_game_active()
                                        pygame.mouse.set_visible(True)
                                        #blit win thing too?
                                    if self.game_board.move_count is 42:
                                        pygame.event.pump()                                    #blit tie game
                                        time.sleep(2)
                                        self.settings.toggle_game_active()
                                        pygame.mouse.set_visible(True)

                                    self.game_board.change_turn()
                                    self.player = 0
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
                    print("ai")
                    #ai
                    moved = False
                    while not moved:
                        
                        move = random.randint(0,6)

                        while self.game_board.button_position < move:
                            self.game_board.move_select_button("right")
                            pygame.event.pump()
                            pygame.display.update()
                            print("right")
                            x = 10000000
                            while(x):
                                x = x-1
                        while self.game_board.button_position > move:
                            self.game_board.move_select_button("left")
                            pygame.event.pump()
                            pygame.display.update()
                            print("left")
                            x = 10000000
                            while(x):
                                x = x-1
                        if self.game_board.check_valid_move():
                            x = 10000000
                            while(x):
                                x = x-1
                            self.game_board.move()
                            pygame.event.pump()
                            pygame.display.update()
                            x = 10000000
                            while(x):
                                x = x-1
                            moved = True

                    if self.game_board.check_win(): 
                        pygame.display.update()
                        pygame.event.pump()
                        time.sleep(2)
                        self.settings.toggle_game_active()
                        pygame.mouse.set_visible(True)
                        #blit win thing too?
                    if self.game_board.move_count is 42:
                        pygame.event.pump()                                    #blit tie game
                        time.sleep(2)
                        self.settings.toggle_game_active()
                        pygame.mouse.set_visible(True)
                    pygame.event.pump()
                    pygame.display.update()
                    x = 10000000
                    while(x):
                        x = x-1
                    
                    self.game_board.change_turn()
                    self.player = 1



                            
            else:
                self.menu.draw_menu()
                pygame.display.update()
                for event in pygame.event.get(): # Events from player
                    if event.type == pygame.QUIT: # Player chose to quit
                        pygame.quit()
                        quit()
                        gameover = True
                    elif event.type == pygame.MOUSEBUTTONDOWN:
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

def get_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--debug",
            type=int,
            default=0,
            help="0 for no debug, 1 for debug mode")
    args = vars(ap.parse_args())
    return args

args = get_arguments()
game = Game()
game.play()
