#by sernikb2
#sernikb@gmail.com

import pygame
import pygame.gfxdraw
import os

#sprite module

SpriteLoadedImages = []
ERROR_IMAGE = pygame.image.load(os.path.join("content\img","error.png"))

def DrawSprite( display, posX, posY, Texture, SizeX, SizeY, Rescale, Rotation, Tx, Ty ):
    #THIS IS A VERY HEAVY FUNCTION - NEEDS OPTIMALISATION IN THE FUTURE
    #Tx and Ty are Tiles cordinatess for animations and different sprites

    #convert to float
    Tx = int(Tx)
    Ty = int(Ty)

    if not Texture:
        SpriteTexture = ERROR_IMAGE
    else:
        LoadedImage = False
        for K in SpriteLoadedImages:
                if K[0] == Texture:
                        LoadedImage = K[1]             
        if LoadedImage != False:
            SpriteTexture = LoadedImage
        else:
            SpriteTexture = pygame.image.load(os.path.join("content\img",Texture))
            SpriteLoadedImages.append([Texture,SpriteTexture])

    if display:
        pygame.gfxdraw.textured_polygon( display, [(posX,posY),(posX,posY+SizeY),(posX+SizeX,posY+SizeY),(posX+SizeX,posY)], SpriteTexture, Tx, Ty )    

        
#def UnloadImages():
        #SpriteLoadedImages.remove(pygame.key.name(key))
