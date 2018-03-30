#by sernikb2
#sernikb@gmail.com

import pygame
import graph
import os

class GUIMainMenuButton:

    IsGUI = True
    IsMainMenu = True
    

    def __init__(self, name):
        self.name = "Main Menu Button"
        self.texture = "ERROR.png"
        self.size = (100,500)

    def set_texture(self, trick):
        self.tricks.append(trick)


#basic text object
def text_object( Surface, Size, Text, Font, Color, POS ):
        #                                              V String Escape! 
        Font = pygame.font.Font(os.path.join("content\\fonts", Font ), Size)
        NewSurface = Font.render(Text, False, Color, None)
        NewSurfaceShadow = Font.render(Text, False, (0,0,0), None)
        Surface.blit(NewSurfaceShadow,(POS[0]-5,POS[1]-5))
        Surface.blit(NewSurface,POS)
