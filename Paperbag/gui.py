#by sernikb2
#sernikb@gmail.com

import pygame
import graph
import os
import math

SpriteLoadedText = []

#this is a button 
class GUIMenuButton(pygame.sprite.Sprite):

        def __init__(self):
                pygame.sprite.Sprite.__init__(self) # necessary to initialize Sprite class
                self.image = pygame.image.load(os.path.join("content\img","error.png"))
                self.rect = self.image.get_rect() #define rect
                self.rect.x = 300 # set up sprite location
                self.rect.y = 300 # set up sprite location
                self.startingPosX = self.rect.x
                self.startingPosY = self.rect.y
                self.tickCount = 0
		
        def update(self):
                self.tickCount += 1
                self.rect.x = self.startingPosX+1000*math.sin(self.tickCount/80)
                print(str(self)+" is now alive for "+str(self.tickCount)+" ticks")


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
        

