#by sernikb2
#sernikb@gmail.com

import pygame
import graph
import os

SpriteLoadedText = []

#this is a button 
class GUIMenuButton:

    IsGUI = True

    def __init__(self, name, POS):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(POS)
        self.image.fill((255,150,100))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        
        self.name = "Main Menu Button"
        self.texture = "ERROR.png"


#basic text object
def text_object( Surface, Size, Text, Font, Color, POS ):
        #                                               V String Escape! 
        FontObj = pygame.font.Font(os.path.join("content\\fonts", Font ), Size)

        LoadedSurface = False
        LoadedSurfaceShadow = False
        for K in SpriteLoadedText:
                if K[0] == Text+"&"+Font+"&"+str(Size):
                        LoadedSurface = K[1]
                if K[0] == Text+"&"+Font+"&"+str(Size)+"&shadow":
                        LoadedSurfaceShadow = K[1]
                        
        if LoadedSurface != False:
            TextSurface = LoadedSurface
        else:
            TextSurface = FontObj.render(Text, False, Color, None)
            SpriteLoadedText.append([Text+"&"+Font+"&"+str(Size),TextSurface])

        if LoadedSurfaceShadow != False:
            TextSurface = LoadedSurface
        else:
            LoadedSurfaceShadow = FontObj.render(Text, False, (0,0,0), None)
            SpriteLoadedText.append([Text+"&"+Font+"&"+str(Size)+"&shadow",LoadedSurfaceShadow])
            
        Surface.blit(LoadedSurfaceShadow,(POS[0]-5,POS[1]-5))
        Surface.blit(TextSurface,POS)
        

##class basic_button():
##    def basic_button( surface, size , text, function, pos ):
##    text_object( surface, size, text, "Warlords.ttf", (255,255,255), (pos[0],pos[1]) )
    
