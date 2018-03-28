#by sernikb2
#sernikb@gmail.com

import pygame
import pygame.gfxdraw
import os

#sprite module

def DrawSprite( display, posX, posY, Texture, SizeX, SizeY, Rescale, Rotation, Tx, Ty ):
    #THIS IS A VERY HEAVY FUNCTION - NEEDS OPTIMALISATION IN THE FUTURE
    #Tx and Ty are Tiles cordinatess for animations and different sprites

    #convert to float
    Tx = int(Tx)
    Ty = int(Ty)

    if not Texture:
        SpriteTexture = pygame.image.load(os.path.join("content\img","error.png"))
    else:
        SpriteTexture = pygame.image.load(os.path.join("content\img",Texture))


    if display:
        pygame.gfxdraw.textured_polygon( display, [(posX,posY),(posX,posY+SizeY),(posX+SizeX,posY+SizeY),(posX+SizeX,posY)], SpriteTexture, Tx, Ty )    
