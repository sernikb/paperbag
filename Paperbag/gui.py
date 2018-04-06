#by sernikb2
#sernikb@gmail.com

import pygame
import graph
import os
import math
import inputevents

SpriteLoadedText = []

#this is a button 
class GUISpriteElement(pygame.sprite.Sprite):

        def __init__(self):
                pygame.sprite.Sprite.__init__(self) # necessary to initialize Sprite class
                self.image = pygame.image.load(os.path.join("content\img","error.png"))
                self.rect = self.image.get_rect() #define rect
                self.rect.x = 300 # set up sprite location
                self.rect.y = 300 # set up sprite location
                self.startingPosX = self.rect.x
                self.startingPosY = self.rect.y
                self.tickCount = 0

        def set_target_surface( self, target_surface ):
                self.surface = target_surface

        def set_image( self, image ):
                self.image = pygame.image.load(os.path.join("content\img",image))

        def set_pos( self, pos ): 
                self.rect.x = pos[0]
                self.rect.y = pos[1]
                #reset starting pos too!
                self.startingPosX = self.rect.x
                self.startingPosY = self.rect.y
		
        def update(self):
                self.tickCount += 1
                self.rect.x = self.startingPosX+20*math.sin(self.tickCount/8)
                self.rect.y = self.startingPosY-10*math.sin(self.tickCount/6)
                #print(str(self)+" is now alive for "+str(self.tickCount)+" ticks")

                #if clicked by mouse - test
                pos = inputevents.getMousePos()
                if self.rect.collidepoint(inputevents.getMousePos()) and inputevents.isMouseKeyPressed("Left Mouse button"):
                        text_object( self.surface, 115, "CLICKED!", "Ye Olde Oak.ttf", (255,255,255), pos )
                


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
        

