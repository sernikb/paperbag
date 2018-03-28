#by sernikb2
#sernikb@gmail.com

import pygame
import graph

class GUIMainMenuButton:

    IsGUI = True
    IsMainMenu = True
    

    def __init__(self, name):
        self.name = "Main Menu Button"
        self.texture = "ERROR.png"
        self.size = (100,500)

    def set_texture(self, trick):
        self.tricks.append(trick)
