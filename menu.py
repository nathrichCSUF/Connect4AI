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
        self.pvpButton = pygame.image.load("images/pvp.png")
        self.pvpButton = pygame.transform.scale(self.pvpButton, (460, 115))
        self.pvaiButton = pygame.image.load("images/pvai.png")
        self.pvaiButton = pygame.transform.scale(self.pvaiButton, (460, 115))
        self.quitButton = pygame.image.load("images/quit_button.png")
        self.quitButton = pygame.transform.scale(self.quitButton, (460, 135))
        self.background = pygame.image.load("images/bg-c4.png")
        self.background = pygame.transform.scale(self.background, (696, 700))

        # self.titlerect = self.title.get_rect()
        self.pvprect = self.pvpButton.get_rect()
        self.pvairect = self.pvaiButton.get_rect()
        self.quitrect = self.quitButton.get_rect()
        self.pvprect.center = self.screen_rect.center
        self.pvprect.top = 125
        self.pvairect.center = self.screen_rect.center
        self.pvairect.top = 225
        self.quitrect.center = self.screen_rect.center
        self.quitrect.top = 330

    def draw_menu(self):
        self.screen.blit(self.background, (0,0))
        # self.screen.blit(self.title, self.titlerect)
        self.screen.blit(self.pvpButton, self.pvprect)
        self.screen.blit(self.pvaiButton, self.pvairect)
        self.screen.blit(self.quitButton, self.quitrect)

    def checkForPlayButtonClick(self,mouseX,mouseY, settings):
        pvp_clicked = self.pvprect.collidepoint(mouseX, mouseY) # check if mouse button clicked play button
        pvai_clicked = self.pvairect.collidepoint(mouseX, mouseY)
        quit_clicked = self.quitrect.collidepoint(mouseX, mouseY)
        if pvp_clicked:
            pygame.mouse.set_visible(False)
            settings.gameActive = "pvp"
        if pvai_clicked:
            settings.gameActive = "pvai"
        if quit_clicked:
            pygame.quit()
            quit()


        

