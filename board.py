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
'''
board contains 6 rows and 7 columns 
(5,0) (5,1) .. .. (5,6)
..                 ..
..                 ..
(1,0)
(0,0) (0,1) .. .. (0,6)

'''
class Board:
    
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Board images (background, buttons)
        self.background = pygame.image.load("outline.png")    # might be used for the background?
        self.rect = self.background.get_rect() 
        self.select_button = pygame.image.load("button.png")
        self.select_button = pygame.transform.scale(self.select_button, (96, 92))
        self.red_select_button = pygame.image.load("button-red.png")
        self.red_select_button = pygame.transform.scale(self.red_select_button, (96, 92))
        self.clear_select_button = pygame.image.load("clear_select_button.png")
        self.clear_select_button= pygame.transform.scale(self.clear_select_button, (96, 92))
        self.winhigh = pygame.image.load("win-star.png")
        self.winhigh= pygame.transform.scale(self.winhigh, (96, 92))
        #dimensions and grid                       
        rows = 6
        columns = 7
        self.grid = [ [sl.Slot(self.screen) for c in range(columns)] for r in range(rows)] 

        self.button_position = 0 # 0-6 column of where button is
        self.rows_position = [0, 0, 0, 0, 0, 0, 0] # 0-5 row of where coin on 7 columns
        self.debug_mode = 0
        self.define_slot_positions()
        self.turn = "red"
        self.move_count = 0
        self.oppGrid = [0,0,0,0,0,0,0]
        self.optMoveRow = 0
        self.optMoveCol = 0

    def define_slot_positions(self):
        for i in range(6):
            for j in range(7):
                self.grid[i][j].set_slot_position((100*j)+6,(500-100*i+50)+6)
    
    def reset_game(self):
        #print("reset game")
        self.reset_slots()
        self.rows_position = [0, 0, 0, 0, 0, 0, 0]
        self.button_position = 0
        self.move_count = 0
        self.turn="red"

    def change_selector_color(self, color):
        if color is "yellow":
            self.screen.blit(self.select_button,(self.button_position*100,-25))
        else:
            self.screen.blit(self.red_select_button,(self.button_position*100,-25))
        pygame.display.update()

    def reset_slots(self):
        #print("reset slots")
        for i in range(6):
            for j in range(7):
                self.grid[i][j].reset()

    def change_turn(self):
        if self.turn is "red":
            self.turn = "yellow"
        else:
            self.turn = "red"

        self.change_selector_color(self.turn)

    # loads board slots, defines slots, and places select button
    def load_board(self):
        if self.debug_mode:
            print("Loading board.")
        for i in range(7):
            for j in range(6):
                self.screen.blit(self.background,(100*i,100*j+50))
        #loading selector Button 
        self.screen.blit(self.red_select_button,(self.button_position,-25)) 


    # Checks if there is an available space on the column
    def check_valid_move(self):
        if self.debug_mode:
            print("Checking valid move")
        if self.rows_position[self.button_position] < 6:
            if self.debug_mode:                    
                print("Space to place!")
            return True
        else:
            if self.debug_mode:
                print("This column is full.")
            return False

    # places a chip in the column then updates the rows position
    def move(self):
        #print("in move: " + str(self.button_position))
        # need to check valid move before moving
        self.move_count = self.move_count + 1
        #print("trying to move: " + str(self.button_position) + str(self.rows_position[self.button_position]))
        slot = self.grid[self.rows_position[self.button_position]][self.button_position]
        slot.change_state(self.turn)
        slot.blit()
        self.rows_position[self.button_position] += 1
        #print(str(self.move_count))

    # select button with checks on bounds
    def move_select_button(self,direction):
        # Valid move Clear last button --> update position --> place new button
        self.screen.blit(self.clear_select_button,(self.button_position*100,-25))
        if direction is "right":
            if self.button_position < 6:    self.button_position += 1      
            else:
                if(self.debug_mode):    print("You've hit the right wall! Try moving left! button_position: " + str(self.button_position))
        elif direction is "left":
            if self.button_position > 0:    self.button_position -= 1
            else:
                if(self.debug_mode):    print("You've hit the left wall! Try moving right! button_position: " + str(self.button_position))
        if self.turn is "red":
            self.screen.blit(self.red_select_button,(self.button_position*100,-25)) 
        else:
            self.screen.blit(self.select_button,(self.button_position*100,-25))


    # check the board to win (theres an easier way to do this) from last move?
    def check_win(self): # fix the turn = self.turn later
        # check for 4 UP 
        turn = self.turn
        for i in range(3):
            for j in range(7):
                if self.grid[i][j].state is not "black":
                    if self.grid[i][j].state is turn:
                        if self.grid[i+1][j].state is turn and self.grid[i+2][j].state is turn and  self.grid[i+3][j].state is turn:
                            print(str(turn) + " wins up")
                            # highlight win spaces
                            self.screen.blit(self.winhigh,self.grid[i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+1][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+2][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+3][j].rect)
                            pygame.display.update()
                            return True
        #check 4 across 
        for i in range(6):
            for j in range(4):
                if self.grid[i][j].state is not "black":
                    if self.grid[i][j].state is turn:
                        if self.grid[i][j+1].state is turn and self.grid[i][j+2].state is turn and  self.grid[i][j+3].state is turn:
                            print(str(turn) + " wins across")
                            # highlight win spaces
                            self.screen.blit(self.winhigh,self.grid[i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i][j+1].rect)
                            self.screen.blit(self.winhigh,self.grid[i][j+2].rect)
                            self.screen.blit(self.winhigh,self.grid[i][j+3].rect)
                            pygame.display.update()
                            return True
                            
       # check diagnoal to the right
        for i in range(3):
            for j in range(4):
                if self.grid[i][j].state is not "black":
                    if self.grid[i][j].state is turn:
                        if self.grid[i+1][j+1].state is turn and self.grid[i+2][j+2].state is turn and  self.grid[i+3][j+3].state is turn:
                            print(str(turn) + " wins diag right")
                            # highlight win spaces
                            self.screen.blit(self.winhigh,self.grid[i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[i+1][j+1].rect)
                            self.screen.blit(self.winhigh,self.grid[i+2][j+2].rect)
                            self.screen.blit(self.winhigh,self.grid[i+3][j+3].rect)  
                            pygame.display.update()
                            return True                   
        
        # check diagnol to the left
        for i in range(3):
            for j in range(4):
                if self.grid[5-i][j].state is not "black":
                    if self.grid[5-i][j].state is turn:
                        if self.grid[5-i-1][j+1].state is turn and self.grid[5-i-2][j+2].state is turn and  self.grid[5-i-3][j+3].state is turn:
                            print(str(turn) + " wins diag left")
                            # highlight win spaces
                            self.screen.blit(self.winhigh,self.grid[5-i][j].rect)
                            self.screen.blit(self.winhigh,self.grid[5-i-1][j+1].rect)
                            self.screen.blit(self.winhigh,self.grid[5-i-2][j+2].rect)
                            self.screen.blit(self.winhigh,self.grid[5-i-3][j+3].rect)
                            pygame.display.update()
                            return True
        return False

    def evalFunction(self):
        turn = self.turn
        print("AI Color: " + str(self.turn))
        self.change_turn()
        opp = self.turn
        self.change_turn()
        placeholder = 0
        print("First Loop")
        for i in range(3):
            for j in range(7):
                if self.grid[i][j].state is self.grid[i+1][j].state and self.grid[i+1][j].state is self.grid[i+2][j].state:
                    if self.grid[i][j].state is not "black":
                        #and self.grid[i+2][j].state is not "black" and self.grid[i+3][j].state is not "black"
                        # print(str(self.grid[i][j].state))
                        # print(str(self.grid[i+1][j].state))
                        # print(str(self.grid[i+2][j].state))
                        # print(str(self.grid[i+3][j].state))

                        print("Vertical Win Area\n")
                        if self.grid[i][j].state is self.turn:
                            print("Going for AI Win Move")
                            if self.grid[i + 3][j].state is self.turn:
                                self.optMoveRow = j
                                self.optMoveCol = i + 3
                                print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                                return 1000
                        elif self.grid[i + 3][j].state is not self.turn:
                            print("Blocking Player Win Move")
                            self.optMoveRow = j
                            self.optMoveCol = i + 3
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return -1000
                        elif self.grid[i][j].state is "black":
                            pass
        print("Horizontal Win Loop")
        for i in range(6):
            for j in range(4):
                if self.grid[i][j].state == self.grid[i][j+1].state and self.grid[i][j+1].state == self.grid[i][j+2].state:
                    if self.grid[i][j].state is not "black":

                        print("Horizontal Four in a Row Win Area\n")
                        if self.grid[i][j].state is self.turn:
                            print("Going for AI Win Move")
                            if self.grid[i][j + 3].state is self.turn:
                                self.optMoveRow = j + 3
                                self.optMoveCol = i
                                print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                                return 1000
                        elif self.grid[i][j + 3].state is not self.turn:
                            print("Blocking Player Win Move")
                            self.optMoveRow = j + 3
                            self.optMoveCol = i
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return -1000
                        elif self.grid[i][j].state is "black":
                            pass

                elif self.grid[i][j].state == self.grid[i][j + 2].state and self.grid[i][j + 2].state == self.grid[i][j + 3].state:
                    if self.grid[i][j + 1].state is "black":
                        print("Horizontal 2nd Piece Missing Win Area\n")
                        if self.grid[i][j].state is self.turn:
                            print("Going for AI Win Move")
                            self.optMoveRow = j + 1
                            self.optMoveCol = i
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return 1000
                        elif self.grid[i][j].state is not self.turn:
                            print("Blocking Player Win Move")
                            self.optMoveRow = j + 1
                            self.optMoveCol = i
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return -1000
                        elif self.grid[i][j].state is "black":
                            pass

                elif self.grid[i][j].state == self.grid[i][j + 1].state and self.grid[i][j + 1].state == self.grid[i][j + 3].state:
                    if self.grid[i][j + 2].state is "black":
                        print("Horizontal 3rd Piece Missing Win Area\n")
                        if self.grid[i][j].state is self.turn:
                            print("Going for AI Win Move")
                            self.optMoveRow = j + 2
                            self.optMoveCol = i
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return 1000
                        elif self.grid[i][j].state is not self.turn:
                            print("Blocking Player Win Move")
                            self.optMoveRow = j + 2
                            self.optMoveCol = i
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return -1000
                        elif self.grid[i][j].state is "black":
                            pass
                if self.grid[i][j + 1].state == self.grid[i][j+2].state and self.grid[i][j+2].state == self.grid[i][j+3].state and self.grid[i][j+1].state is not "black":
                    if self.grid[i][j].state is "black":

                        print("Horizontal Four a Row Win 1st Piece Missing Area\n")
                        if self.grid[i][j + 1].state is self.turn:
                            print("Going for AI Win Move")
                            self.optMoveRow = j
                            self.optMoveCol = i
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return 1000
                        elif self.grid[i][j + 1].state is not self.turn:
                            print("Blocking Player Win Move")
                            self.optMoveRow = j
                            self.optMoveCol = i
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return -1000

        print("Checking Diagonal of the right")
        for i in range(3):
            for j in range(4):
                if self.grid[i][j].state == self.grid[i+1][j+1].state and self.grid[i+1][j+1].state == self.grid[i+2][j+2].state:
                    if self.grid[i + 3][j + 3].state is "black":
                        print("Blocking Diagonal Four in a Row")
                        if self.grid[i][j].state is self.turn:
                            self.optMoveRow = j + 3
                            self.optMoveCol = i + 3
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return 1000
                        elif self.grid[i][j].state is opp:
                            self.optMoveRow = j + 3
                            self.optMoveCol = i + 3
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return -1000
                if self.grid[i][j].state == self.grid[i+1][j+1].state and self.grid[i+1][j+1].state == self.grid[i+3][j+3].state:
                    if self.grid[i+2][j+2].state is "black":
                        print("Blocking Diagonal Four in a Row 3rd Piece Missing")
                        if self.grid[i][j].state is self.turn:
                            self.optMoveRow = j + 2
                            self.optMoveCol = i + 2
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return 1000
                        elif self.grid[i][j].state is opp:
                            self.optMoveRow = j + 2
                            self.optMoveCol = i + 2
                            return -1000
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                        elif self.grid[i][j].state is "black":
                            pass
                if self.grid[i][j].state == self.grid[i+2][j+2].state and self.grid[i+2][j+2].state == self.grid[i+3][j+3].state:
                    if self.grid[i+1][j+1].state is "black":
                        print("Blocking Diagonal Four in a Row 2nd Piece Missing")
                        if self.grid[i][j].state is self.turn:
                            self.optMoveRow = j + 1
                            self.optMoveCol = i + 1
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                            return 1000
                        elif self.grid[i][j].state is opp:
                            self.optMoveRow = j + 1
                            self.optMoveCol = i + 1
                            return -1000
                            print("OptMove: [" + str(self.optMoveRow) + "," + str(self.optMoveCol) + "]")
                        elif self.grid[i][j].state is "black":
                            pass


        # print("Forth")
        # for i in range(3):
        #     for j in range(4):
        #         if self.grid[5-i][j].state is not "black":
        #             if self.grid[5-i-1][j+1].state == self.grid[5-i-2][j+2].state and self.grid[5-i-2][j+2].state == self.grid[5-i-3][j+3].state is turn  and self.grid[5-i-1][j+1].state is not "black" and self.grid[5-i-2][j+2].state is not "black" and self.grid[5-i-3][j+3].state is not "black":
        #                 if self.grid[i][j].state is self.turn:
        #                     self.optMove = i
        #                     return 1000
        #                 elif self.grid[i][j].state is opp:
        #                     self.optMove = i
        #                     return -1000

        return 0
            

    def minimax(self, depth, isMaxiPlayer):
        val = 0
        if self.move_count is 42:
            return 0
        score = self.evalFunction()
        print("Depth: " + str(depth))
        print("Score: " + str(score))
        if score == 1000:
            print("My turn to win!")
            return self.optMoveRow
        elif score == -1000:
            print("Player Winning Move is being Blocked by AI")
            return self.optMoveRow

        placeholder = 0
        minValueRow = [0, 0, 0, 0, 0, 0, 0]
        minValueCol = [0, 0, 0, 0, 0, 0, 0]

        for i in range(6):
            for j in range(7):
                if self.grid[i][j].state is "black":
                    minValueRow[placeholder] = i
                    minValueCol[placeholder] = j
                    placeholder = placeholder + 1
                    break
        #print("\nRecursive\n")
        if isMaxiPlayer:
            print("Entering Maxi Player Loop")
            bestVal = -1000

            print("7th Col State: " + str(self.grid[0][6].state))

            for i in range(7):
                print("Available Spot: [" + str(minValueRow[i]) + "," + str(minValueCol[i]) + "]")
            placeholder = 0
            for i in range(7):
                    if self.grid[minValueRow[i]][minValueCol[i]].state is "black":
                        self.button_position = minValueRow[i]
                        if self.check_valid_move():
                            self.grid[minValueRow[i]][minValueCol[i]].state = self.turn
                            if(depth < 2):
                                print("Thinking for Spot: " + str(i) + " " + str(j))
                                bestVal = max(bestVal, self.minimax(depth+1, True))
                                print("I reset the slot?\n")
                                val = i
                            self.grid[minValueRow[i]][minValueCol[i]].state = "black"
            return minValueRow[i]
            print("Val: " + str(bestVal))
        
        else:
            print("Entering Mini Player Lopp")
            bestVal = 1000

            placeholder = 0
            for i in range(7):
                print("Available Spot: [" + str(minValueRow[i]) + "," + str(minValueCol[i]) + "]")

            for i in range(7):
                    if self.grid[minValueRow[i]][minValueCol[i]].state is "black":
                        self.button_position = minValueRow[i]
                        if self.check_valid_move():
                            self.grid[i][j].state = self.turn
                            if(depth < 2):
                                print("Thinking for Spot: " + str(i) + " " + str(j))
                                bestVal = min(bestVal, self.minimax(depth+1, False))
                                print("I reset the value\n")
                                val = i
                            self.grid[minValueRow[i]][minValueCol[i]].state = "black"
                        else:
                            break
            return minValueRow[i]
            print("Val: " + str(bestVal))

        return 5