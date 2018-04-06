#by sernikb2
#sernikb@gmail.com
#KeyUP & KeyDown event manager

import pygame

#Keyboard functions
#table containing all the ID of keyboard keys currently pressed
PressedKeyButtons = []

def addKeyEv(key):
        PressedKeyButtons.append(pygame.key.name(key))

def removeKeyEv(key):
        PressedKeyButtons.remove(pygame.key.name(key))
        
def getPressedKeys():
        return PressedKeyButtons

def isKeyPressed(key):
        keyStatus = False
        
        for K in PressedKeyButtons:
                if K == key:
                        keyStatus = True
              
        return keyStatus



#Mouse functions
MousePos = (0,0)
MouseButtons = []

def translateMouseID(ID):
        #i should put this inside table to make this look nicer
        KeyName = "unknown button"
        if (ID==1):
             KeyName = "Left Mouse button"   
        elif(ID==2):
             KeyName = "Middle Mouse button"   
        elif(ID==3):
             KeyName = "Right Mouse button"   
        return KeyName

def addMouseClick(button):
        MouseButtons.append(translateMouseID(button))

def addMousePos(pos):
        global MousePos
        MousePos = pos

def removeMouseClick(button):
        MouseButtons.remove(translateMouseID(button))
        
def getMousePos():
        return MousePos

def getPressedMouseKeys():
        return MouseButtons

def isMouseKeyPressed(key):
        keyStatus = False
        
        for K in MouseButtons:
                if K == key:
                        keyStatus = True
              
        return keyStatus
