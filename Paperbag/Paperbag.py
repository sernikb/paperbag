#created by sernikb and MichaelWill
print(" ===================== START =====================")

import pygame
#gfx import is broken so we need to force it
import pygame.gfxdraw
import os
import math
import random
import sqlite3
#paperbag modules
import inputevents
import graph
import gui

import json

with open('data.json') as json_data:
    data = json.load(json_data)

#variable used to run things only once on startup
IsFirst_Program_Loop = True

#stuff that happens before first loop here
def setup():

    #databases test
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("create table people (name_last, age)")

    who = "Yeltsin"
    age = 72

    # This is the qmark style:
    cur.execute("insert into people values (?, ?)", (who, age))

    # And this is the named style:
    cur.execute("select * from people where name_last=:who and age=:age", {"who": who, "age": age})

    print("> SQLite3 test:")
    print(cur.fetchone())
    

def program_loop():
    global IsFirst_Program_Loop


    #ID of the displayed menus
    # 1 = splash screen
    # 2 = game main menu
    Menu_ID = 1

    pygame.init()
    gameDisplay = pygame.display.set_mode((data['display']['width'],data['display']['height']))
    pygame.display.set_caption(data['window_title'])

    #set icon
    pygame.display.set_icon( pygame.image.load(os.path.join("content\img","icon.png")) )

    #Runtime Timer
    clock = pygame.time.Clock()

    _EXIT = False

    #Set up evesurfacents


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
            ##KEYUP           gameDisplay key, mod
            ##MOUSEMOTION      pos, rel, buttons
            ##MOUSEBUTTONUP    pos, button
            ##MOUSEBUTTONDOWN  pos, button
            ##JOYAXISMOTION    joy, axis, value
            ##JOYBALLMOTION    joy, ball, rel
            ##JOYHATMOTION     joy, hat, value
            ##JOYBUTTONUP      joy, button
            ##JOYBUTTONDOWN    joy, button
            ##VIDEORESIZsurfaceE      size, w, h
            ##VIDEOEXPOSE      none
            ##USEREVENT        code

            # QUIT event [X]
            if event.type == pygame.QUIT:
                print(" ===================== QUIT =====================")
                pygame.quit()
                quit()


            #handle key presses KEYDOWN
            if event.type == pygame.KEYDOWN:
                key = event.key
                inputevents.addKeyEv(key)
            #handle key presses KEYUP
            if event.type == pygame.KEYUP:
                key = event.key
                inputevents.removeKeyEv(key)

            #handle mouse motion
            #MOUSEMOTION  pos, rel, buttons
            if event.type == pygame.MOUSEMOTION:
                inputevents.addMousePos(event.pos)
                
            #handle mouse key up
            #MOUSEBUTTONUP  pos, button
            if event.type == pygame.MOUSEBUTTONUP:
                inputevents.removeMouseClick(event.button)

            #handle mouse key down
            #MOUSEBUTTONDOWN  pos, button
            if event.type == pygame.MOUSEBUTTONDOWN:
                inputevents.addMouseClick(event.button)

            #if event.event_name == "main_menu":
            #print(event)
                

        #fill screen witsurfaceh black color
        #gray for now so i can see layout
        gameDisplay.fill((10,10,10))

        #render splash screen
        ## it was too laggy so i need to disable it!
        ## graph.DrawSprite( gameDisplay, 0.01, 0, "clouds_bg_pattern2.png", data['display']['width'], data['display']['height'], None, None, -BgSMF, BgSMF/10  )
        ## graph.DrawSprite( gameDisplay, 0.01, 0, "clouds_bg_pattern.png", data['display']['width'], data['display']['height'], None, None, -BgSMF+BgSMF/10, BgSMF/10+BgSMF/10  )
        FontList = [
            "ARCADE.TTF",
            "VTCBelialsBlade.ttf",
            "VTCBelialsBlade3d.ttf",
            "VTCBelialsBladeItalic.ttf",
            "VTCBelialsBsurfaceladeShadow.ttf",
            "VTCBelialsBladeTricked.ttf",
            "wager.ttf",
            "wagerlos.ttf",
            "wagerwon.ttf",
            "Warlords.ttf",
            "Werbedeutsch.ttf",
            "Will-Harris.ttf",
            "XAyax.ttf",
            "XAyaxOutline.ttf",
            "Ye Olde Oaksurface.ttf",
            "YES!.ttf"
            ]
        #draw main menu title
        gui.text_object( gameDisplay, 115, "paperbag", "Ye Olde Oak.ttf", (255,255,255), (100,100) )   #random.choice(FontList)
        #version
        gui.text_object( gameDisplay, 30, "Version: " + data['version'], "ARCADE.TTF", (255,255,255), (100,220) )   #random.choice(FontList)
        #paper bag head (OLD and Lagy)
        ##graph.DrawSprite( gameDisplay, 600, 100, "paperbag_head1"+random.choice((".png","_alt1.png","_alt2.png")), 120, 160, None, None, 20, 90  )

        #background thingy movement control (for testing)
        if inputevents.isKeyPressed(97):
            BgSMF += 10
        
        BgSMF += 2

		
		
        # RUN ONLY ONE TIME
        if IsFirst_Program_Loop == True:


            GUIs = pygame.sprite.Group() # define a sprite group for guis
            
            # [X] START NEW GAME
            def MENUStartNewGame():
                gui.text_object( gameDisplay, 115, "MENUStartNewGame():", "Ye Olde Oak.ttf", (255,255,255), (100,100) )
            # [X] DEF CONNECT TO SERVER
            def MENUConnectToServer():
                gui.text_object( gameDisplay, 115, "MENUConnectToServer()", "Ye Olde Oak.ttf", (255,255,255), (100,100) )
            # [X] OPTIONS
            def MENUOptions():
                gui.text_object( gameDisplay, 115, "MENUOptions()", "Ye Olde Oak.ttf", (255,255,255), (100,100) )
            # [X] CREDITS
            def MENUCredits():
                gui.text_object( gameDisplay, 115, "MENUCredits()", "Ye Olde Oak.ttf", (255,255,255), (100,100) )
            # [X] EXIT
            def MENUExitTheGame():
                _EXIT = True

            #main menu buttons
            MenuButtons = [("Start New Game",MENUStartNewGame()),
                           ("Connect To Server",MENUConnectToServer()),
                           ("Options",MENUOptions()),
                           ("Credits",MENUCredits()),
                           ("Exit",MENUExitTheGame())
                           ]
                
            i = 0
            while i < len(MenuButtons):

                MButton = gui.GUIMainMenuButton()
                MButton.set_target_surface( gameDisplay )
                MButton.set_pos( (120,300+(i*60)) )
                MButton.text = MenuButtons[i][0]
                MButton.rebuild_Rectangle()
                MButton.functionM1 = MenuButtons[i][1]
                GUIs.add(MButton) # add an instance to group
                ##gui.text_object( gameDisplay, 50, MenuButtons[i], "wagerlos.ttf", (255,255,255), (120,300+(i*60)) )
                
                i += 1


            #paper bag head
            PaperbagHead = gui.GUISpriteElement()
            PaperbagHead.set_target_surface( gameDisplay )
            PaperbagHead.set_image( "paperbag_head1.png" ) # "paperbag_head1"+random.choice((".png","_alt1.png","_alt2.png"))
            PaperbagHead.set_pos( (560,100) )
            GUIs.add(PaperbagHead) # add an instance to group
            
        
        GUIs.update() #calls the update function on all sprites in group
        GUIs.draw(gameDisplay) #draws all sprites in the group
		
		
        #debug text stuffs
        PressedKeys = inputevents.getPressedKeys() + inputevents.getPressedMouseKeys()
        str1 = ' '.join(str(e) for e in PressedKeys)
        gui.text_object( gameDisplay, 20, "Pressed Buttons: ", "Warlords.ttf", (255,255,255), (10,20) )
        gui.text_object( gameDisplay, 20, str1, "Warlords.ttf", (255,255,255), (10,40) )
        gui.text_object( gameDisplay, 20, " FPS: "+str(round(clock.get_fps(),1))+" Time: "+str(clock.get_time()), "Warlords.ttf", (255,255,255), (10,60) )
        ###gameDisplay.blit(SplashScreen,(0,0))
        
        #UPDATE SURFACE
        pygame.display.update()

        #FPS settings
        clock.tick( 60 )

        #End of program loop
        IsFirst_Program_Loop = False




setup()
program_loop()
pygame.quit()
quit()
        

    
