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
        self.playButton = pygame.image.load_extended("images/play_button.png")
        self.playButton = pygame.transform.scale(self.playButton, (96, 92))
        self.background = pygame.image.load_extended("images/bg-c4.png")
        self.background = pygame.transform.scale(self.background, (696, 700))

        # self.titlerect = self.title.get_rect()
        self.playrect = self.playButton.get_rect()

        # self.titlerect.center = self.screen_rect.center
        # self.titlerect.top = self.screen_rect.top

        self.playrect.center = self.screen_rect.center

    def draw_menu(self):
        self.screen.blit(self.background, self.screen_rect)
        # self.screen.blit(self.title, self.titlerect)
        self.screen.blit(self.playButton, self.playrect)

    def checkForPlayButtonClick(self,mouseX,mouseY, settings):
        button_clicked = self.playrect.collidepoint(mouseX, mouseY) # check if mouse button clicked play button

        if button_clicked and not settings.gameActive:
            pygame.mouse.set_visible(False)
            settings.gameActive = True
