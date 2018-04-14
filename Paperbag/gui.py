#by sernikb2
#sernikb@gmail.com

import pygame
import graph
import os
import math
import inputevents

SpriteLoadedText = []

#basic sprite
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


#gui buttons
class GUIMainMenuButton(pygame.sprite.Sprite):

        def __init__(self):
                pygame.sprite.Sprite.__init__(self) # necessary to initialize Sprite class
                self.image = pygame.image.load(os.path.join("content\img\gui","marker.png"))
                self.rect = self.image.get_rect() #define rect
                self.rect.x = 300 # set up sprite location
                self.rect.y = 300 # set up sprite location
                self.startingPosX = self.rect.x
                self.startingPosY = self.rect.y
                self.tickCount = 0
                self.fontSize = 50                      #set def value
                self.font = "wagerlos.ttf"              #set def value
                self.text = "Undefined text - pre set!" #set def value
                self.color = (155,155,155)              #set def value
                self.color_hovered = (250,250,250)     #set def value
                self.color_selected = (55,255,55)     #set def value
                #create def rectangle
                FontObj = pygame.font.Font(os.path.join("content\\fonts", self.font ), self.fontSize)
                self.TextSurface = FontObj.render(self.text, False, self.color, None)
                self.TextSurfaceHovered = FontObj.render(self.text, False, self.color_hovered, None)
                self.TextSurfaceSelected = FontObj.render(self.text, False, self.color_selected, None)
                self.rect = self.TextSurface.get_rect()

        def set_target_surface( self, target_surface ):
                self.surface = target_surface
                

        def rebuild_Rectangle( self ):
                FontObj = pygame.font.Font(os.path.join("content\\fonts", self.font ), self.fontSize)
                self.TextSurface = FontObj.render(self.text, False, self.color, None)
                self.TextSurfaceHovered = FontObj.render(self.text, False, self.color_hovered, None)
                self.TextSurfaceSelected = FontObj.render(self.text, False, self.color_selected, None)
                #save current pos
                originalX = self.rect.x
                originalY = self.rect.y
                #rebuild rectangle
                self.rect = self.TextSurface.get_rect()
                #restore original pos
                self.rect.x = originalX
                self.rect.y = originalY
                

        def set_pos( self, pos ):
                self.rect.x = pos[0]
                self.rect.y = pos[1]
                #reset starting pos too!
                self.startingPosX = self.rect.x
                self.startingPosY = self.rect.y

        def update(self):
                self.tickCount += 1
                
                #print(str(self)+" is now alive for "+str(self.tickCount)+" ticks")

                #only when surface is present
                if self.surface:

                        #if hovered by mouse
                        pos = inputevents.getMousePos()
                        if self.rect.collidepoint(inputevents.getMousePos()):

                                #render text with color on hover
                                self.surface.blit(self.TextSurfaceHovered,(self.rect.x,self.rect.y))

                                #when clicked by mouse
                                if inputevents.isMouseKeyPressed("Left Mouse button"):
                                        #render text with color on click
                                        self.surface.blit(self.TextSurfaceSelected,(self.rect.x,self.rect.y))
                                        
                                        effect = pygame.mixer.Sound(os.path.join("content\sound", "select1.wav" ))
                                        effect.set_volume(0.04)
                                        effect.play()

                                        print(self.functionM1)
                                        if self.functionM1:
                                                print(self.functionM1)
                                                self.functionM1
                                        
                        else:
                                #render text normaly
                                self.surface.blit(self.TextSurface,(self.rect.x,self.rect.y))
                        
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
        

