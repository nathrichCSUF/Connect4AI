"""
FALL 2019 CPSC 481 Artificial Intelligence Project
File Description: menu.py
    Holds Main Menu

Authors:
    Nathaniel Richards
    Yash Bhambani
    Matthew Camarena
    Dustin Vuong

"""

import pygame

class Menu:
    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # self.title = pygame.image.load_extended("images/connect4_logo.png")
        self.pvpButton = pygame.image.load_extended("images/pvp.png")
        self.pvpButton = pygame.transform.scale(self.pvpButton, (460, 115))
        self.pvaiButton = pygame.image.load("images/pvai.png")
        self.pvaiButton = pygame.transform.scale(self.pvaiButton, (460, 115))
        self.background = pygame.image.load_extended("images/bg-c4.png")

        # self.titlerect = self.title.get_rect()
        self.pvprect = self.pvpButton.get_rect()
        self.pvairect = self.pvaiButton.get_rect()
        # self.titlerect.center = self.screen_rect.center
        # self.titlerect.top = self.screen_rect.top

    def draw_menu(self):
        self.screen.blit(self.background, (0,0))
        # self.screen.blit(self.title, self.titlerect)
        self.screen.blit(self.pvpButton, (20,300))
        self.screen.blit(self.pvaiButton, (20,450))

    def checkForPlayButtonClick(self,mouseX,mouseY, settings):
        button_clicked = self.playrect.collidepoint(mouseX, mouseY) # check if mouse button clicked play button

        if button_clicked and not settings.gameActive:
            pygame.mouse.set_visible(False)
            settings.gameActive = True


        

