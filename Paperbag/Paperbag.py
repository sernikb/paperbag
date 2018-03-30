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
import gui


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
        graph.DrawSprite( gameDisplay, 0.01, 0, "clouds_bg_pattern2.png", display_width, display_height, None, None, -BgSMF, BgSMF/10  )
        graph.DrawSprite( gameDisplay, 0.01, 0, "clouds_bg_pattern.png", display_width, display_height, None, None, -BgSMF+BgSMF/10, BgSMF/10+BgSMF/10  )
        FontList = [
            "ARCADE.TTF",
            "VTCBelialsBlade.ttf",
            "VTCBelialsBlade3d.ttf",
            "VTCBelialsBladeItalic.ttf",
            "VTCBelialsBladeShadow.ttf",
            "VTCBelialsBladeTricked.ttf",
            "wager.ttf",
            "wagerlos.ttf",
            "wagerwon.ttf",
            "Warlords.ttf",
            "Werbedeutsch.ttf",
            "Will-Harris.ttf",
            "XAyax.ttf",
            "XAyaxOutline.ttf",
            "Ye Olde Oak.ttf",
            "YES!.ttf"
            ]
        #draw main menu title
        gui.text_object( gameDisplay, 115, "paperbag", "Ye Olde Oak.ttf", (255,255,255), (100,100) )   #random.choice(FontList)
        #version
        gui.text_object( gameDisplay, 30, "Version: GUI_test 0.1", "ARCADE.TTF", (255,255,255), (100,220) )   #random.choice(FontList)
        #paper bag head
        graph.DrawSprite( gameDisplay, 600, 100, "paperbag_head1"+random.choice((".png","_alt1.png","_alt2.png")), 120, 160, None, None, 20, 90  )

        if inputevents.isKeyPressed(97):
            BgSMF += 10
        
        BgSMF += 2

        #dummy main menu buttons
        colors = ["New game", "Load Game", "Enter Code", "Set Operator Mode",]
        i = 0
        while i < len(colors):
            print(colors[i])
            i += 1
        gui.text_object( gameDisplay, 50, "New game", "wagerlos.ttf", (255,255,255), (120,300) )
        gui.text_object( gameDisplay, 50, "Load Game", "wagerlos.ttf", (255,255,255), (120,340) )
        gui.text_object( gameDisplay, 50, "Enter Code", "wagerlos.ttf", (255,255,255), (120,380) )
        gui.text_object( gameDisplay, 50, "Set Operator Mode", "wagerlos.ttf", (255,255,255), (120,420) )
        gui.text_object( gameDisplay, 50, "Arcade System Options", "wagerlos.ttf", (255,255,255), (120,460) )
        gui.text_object( gameDisplay, 50, "Credits", "wagerlos.ttf", (255,255,255), (120,500) )

        #debug text stuffs
        PressedKeys = inputevents.getPressedKeys()
        str1 = ''.join(str(e) for e in PressedKeys)
        gui.text_object( gameDisplay, 20, "Pressed Buttons: ", "Warlords.ttf", (255,255,255), (10,20) )
        gui.text_object( gameDisplay, 20, str1, "Warlords.ttf", (255,255,255), (10,40) )
        gui.text_object( gameDisplay, 20, "Time: "+str(clock.get_time()), "Warlords.ttf", (255,255,255), (10,60) )
        ###gameDisplay.blit(SplashScreen,(0,0))
        
        #UPDATE SURFACE
        pygame.display.update()

        #FPS settings
        clock.tick( 60 )


    #gameDisplay.blit(pygame.image.load(os.path.join("content\img","ERROR.png")),(100,100))




program_loop()
pygame.quit()
quit()
        

    
