#fuck you vidubel
print(" ===================== START =====================")

import pygame
#gfx import is broken so we need to force it
import pygame.gfxdraw
import os
import math
import random
#paperbag modules
import inputevents
import graph


##import math


def program_loop():

    display_width = 1200
    display_height = 800

    #ID of the displayed menus
    # 1 = splash screen
    # 2 = game main menu
    Menu_ID = 1

    pygame.init()
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("paperbag: call for revenge")

    #set icon
    pygame.display.set_icon( pygame.image.load(os.path.join("content\img","icon.png")) )

    #Runtime Timer
    clock = pygame.time.Clock()

    _EXIT = False

    #Set up events

    BgSMF = -2200

    #basic font thingy - needs to be moved to gui lib
    def text_object( Surface, Text, Font, Color, X, Y ):
        #                                              V String Escape! 
        Font = pygame.font.Font(os.path.join("content\\fonts", Font ), 115)
        Surface = Font.render(Text, False, Color, None)
        gameDisplay.blit(Surface,(X,Y))
        

    #Load temp images
    SplashScreen = pygame.image.load(os.path.join("content\img","splashscreen.png"))

    while not _EXIT:
        
        # =======================================================
        # ==== handle LIST OF SDL EVENTS in pygame lib ==========
        # =======================================================
        
        for event in pygame.event.get(): #table of events

            #LIST OF EVENTS:
            ##QUIT             none
            ##ACTIVEEVENT      gain, state
            ##KEYDOWN          unicode, key, mod
            ##KEYUP            key, mod
            ##MOUSEMOTION      pos, rel, buttons
            ##MOUSEBUTTONUP    pos, button
            ##MOUSEBUTTONDOWN  pos, button
            ##JOYAXISMOTION    joy, axis, value
            ##JOYBALLMOTION    joy, ball, rel
            ##JOYHATMOTION     joy, hat, value
            ##JOYBUTTONUP      joy, button
            ##JOYBUTTONDOWN    joy, button
            ##VIDEORESIZE      size, w, h
            ##VIDEOEXPOSE      none
            ##USEREVENT        code

            # QUIT event [X]
            if event.type == pygame.QUIT:
                print(" ===================== QUIT =====================")
                pygame.quit()
                quit()


            #chandle key presses KEYDOWN
            if event.type == pygame.KEYDOWN:
                key = event.key
                inputevents.addKeyEv(key)
                
            #chandle key presses KEYUP
            if event.type == pygame.KEYUP:
                key = event.key
                inputevents.removeKeyEv(key)

            #if event.event_name == "main_menu":
            #print(event)
                

        #fill screen with black color
        #gray for now so i can see layout
        gameDisplay.fill((10,10,10))

        #render splash screen
        graph.DrawSprite( gameDisplay, 0.01, 0, "clouds_bg_pattern2.png", display_width, display_height, None, None, -BgSMF, 0  )

        #draw main menu title
        text_object( gameDisplay, "paperbag", "Warlords.ttf", (255,255,255),100,100 )

        if inputevents.isKeyPressed(97):
            BgSMF += 10
        
        BgSMF += 2

        PressedKeys = inputevents.getPressedKeys()
        str1 = ''.join(str(e) for e in PressedKeys)

        text_object( gameDisplay, str1, "Warlords.ttf", (255,255,255),100,100 )
        ###gameDisplay.blit(SplashScreen,(0,0))
        
        #UPDATE SURFACE
        pygame.display.update()

        #FPS settings
        clock.tick( 60 )


    #gameDisplay.blit(pygame.image.load(os.path.join("content\img","ERROR.png")),(100,100))




program_loop()
pygame.quit()
quit()
        

    
