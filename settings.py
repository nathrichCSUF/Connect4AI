"""
FALL 2019 CPSC 481 Artificial Intelligence Project
File Description: stats.py
    Holds stats and settings for game

Authors:
    Nathaniel Richards
    Yash Bhambani
    Matthew Camarena
    Dustin Vuong

"""


class Settings:
    def __init__(self):
        self.gameActive = "menu"

    def toggle_game_active(self):  # Toggle if game is active
        #if not self.gameActive: # if false
        #    self.gameActive = True
        #else:
        #    self.gameActive = False
        self.gameActive = "menu"
