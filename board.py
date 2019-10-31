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

# board contains 6 rows and 7 columns

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.background = pygame.image.load("outline.png")    # might be used for the background?
        self.select_button = pygame.image.load("button.png")
        self.trans = pygame.image.load("trans.png")
        self.winhigh = pygame.image.load("win.png")
        self.rect = self.background.get_rect()                         # dimensions of image
        rows = 6
        columns = 7
        self.place_board_slots()
        self.grid = [[sl.Slot(self.screen) for c in range(columns)] for r in range(rows)]
        self.buttonPos = (0,600)
        self.rowPos = [100,100,100,100,100,100,100]
        # 2D Array Representing all Slots in Game Board


        #self.rect.centerx = self.screen_rect.centerx
        #self.rect.centery = self.screen_rect.centery

    def load_board(self):
        print("loading board...")
        for i in range(7):
            for j in range(6):
                self.screen.blit(self.background,(100*i,100*j))
        self.screen.blit(self.select_button,self.buttonPos)


    def move(self, turn):

        #print("Button is: " + str(self.buttonPos) + "rowPos" + str(self.rowPos))
        l = list(self.buttonPos)
        ok = int(l[0]/100)

        subnum = self.rowPos[ok]

        if  subnum > 600:
            print("column full")
            return
        else:           
            l[1] -= subnum
            self.rowPos[ok] += 100
            #print("this" + str(int(l[0]/100))+  " " + str(int(l[1]/100)))
            slot = self.grid[int(l[1]/100)][int(l[0]/100)]
            slot.set_slot_position(l[0],l[1])
            slot.change_state(turn) 
            slot.blit()

    def move_button(self,direction):
        #need to check if valid move
        l = list(self.buttonPos)
        c = self.buttonPos
        x = l[0]
        if direction is "right":
            if (x + 100) > 600:
                print("can't go right anymore")
                return
            else:
                l[0] += 100
                self.buttonPos = tuple(l)
                self.screen.blit(self.trans,c)
                self.screen.blit(self.select_button,self.buttonPos)
        elif direction is "left":
            if (x - 100) < 0:
                print("can't go left anymore")
            else:
                l[0] -= 100
                self.buttonPos = tuple(l)
                self.screen.blit(self.trans,c)
                self.screen.blit(self.select_button,self.buttonPos)

    def check_win(self):
        '''checking for 
        *
        *
        *
        *
        '''
        for i in range(3):
            for j in range(7):
                if self.grid[i][j].state is not "black":
                    if self.grid[i][j].state is "yellow":
                        if self.grid[i+1][j].state is "yellow" and self.grid[i+2][j].state is "yellow" and  self.grid[i+3][j].state is "yellow":
                            print("yellow wins")
                            # highlight win spaces
                            self.screen.blit(self.winhigh,self.grid[i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+1][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+2][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+3][j].rect)
                            

                    if self.grid[i][j].state is "red":
                        if self.grid[i+1][j].state is "red" and self.grid[i+2][j].state is "red" and  self.grid[i+3][j].state is "red":
                            print("red wins")
                            self.screen.blit(self.winhigh,self.grid[i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+1][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+2][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+3][j].rect)
        '''checking for 
        * * * *
        '''

        for i in range(6):
            for j in range(4):
                if self.grid[i][j].state is not "black":
                    if self.grid[i][j].state is "yellow":
                        if self.grid[i][j+1].state is "yellow" and self.grid[i][j+2].state is "yellow" and  self.grid[i][j+3].state is "yellow":
                            print("yellow wins")
                            # highlight win spaces
                            self.screen.blit(self.winhigh,self.grid[i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i][j+1].rect)
                            self.screen.blit(self.winhigh,self.grid[i][j+2].rect)
                            self.screen.blit(self.winhigh,self.grid[i][j+3].rect)
                            

                    if self.grid[i][j].state is "red":
                        if self.grid[i][j+1].state is "red" and self.grid[i][j+2].state is "red" and  self.grid[i][j+3].state is "red":
                            print("red wins")
                            self.screen.blit(self.winhigh,self.grid[i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i][j+1].rect)
                            self.screen.blit(self.winhigh,self.grid[i][j+2].rect)
                            self.screen.blit(self.winhigh,self.grid[i][j+3].rect)


        ''' checking for
        *
          *
            *
              *
        '''
        for i in range(3):
            for j in range(4):
                if self.grid[i][j].state is not "black":
                    if self.grid[i][j].state is "yellow":
                        if self.grid[i+1][j+1].state is "yellow" and self.grid[i+2][j+2].state is "yellow" and  self.grid[i+3][j+3].state is "yellow":
                            print("yellow wins")
                            # highlight win spaces
                            self.screen.blit(self.winhigh,self.grid[i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+1][j+1].rect)
                            self.screen.blit(self.winhigh,self.grid[i+2][j+2].rect)
                            self.screen.blit(self.winhigh,self.grid[i+3][j+3].rect)
                            

                    if self.grid[i][j].state is "red":
                        if self.grid[i+1][j+1].state is "red" and self.grid[i+2][j+2].state is "red" and  self.grid[i+3][j+3].state is "red":
                            print("red wins")
                            self.screen.blit(self.winhigh,self.grid[i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+1][j+1].rect)
                            self.screen.blit(self.winhigh,self.grid[i+2][j+2].rect)
                            self.screen.blit(self.winhigh,self.grid[i+3][j+3].rect)
        

        ''' checking for
              *
            *
          *
        *
        '''
        for i in range(3):
            for j in range(4):
                if self.grid[5-i][j].state is not "black":
                    if self.grid[5-i][j].state is "yellow":
                        if self.grid[5-i-1][j+1].state is "yellow" and self.grid[5-i-2][j+2].state is "yellow" and  self.grid[5-i-3][j+3].state is "yellow":
                            print("yellow wins")
                            # highlight win spaces
                            self.screen.blit(self.winhigh,self.grid[5-i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[5-i-1][j+1].rect)
                            self.screen.blit(self.winhigh,self.grid[5-i-2][j+2].rect)
                            self.screen.blit(self.winhigh,self.grid[5-i-3][j+3].rect)
                            

                    if self.grid[5-i][j].state is "red":
                        if self.grid[5-i-1][j+1].state is "red" and self.grid[5-i-2][j+2].state is "red" and  self.grid[5-i-3][j+3].state is "red":
                            print("red wins")
                            self.screen.blit(self.winhigh,self.grid[5-i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[5-i-1][j+1].rect)
                            self.screen.blit(self.winhigh,self.grid[5-i-2][j+2].rect)
                            self.screen.blit(self.winhigh,self.grid[5-i-3][j+3].rect)

                    

    def place_board_slots(self):
        
        #background = pygame.image.load("red.png")
        print("what")
        #self.screen.blit(self.background,self.rect)

        '''
        self.rect.x = 100
        self.rect.y = 100
        self.screen.blit(self.image,self.rect)
        #setting positions of the slots
        '''
        '''
        for i in range(6):
            for j in range(7):
                self.screen.blit(self.image,(400,400))
        '''

        def reset_board(self):
            print("resetting board")