#by sernikb2
#sernikb@gmail.com
#KeyUP & KeyDown event manager

import pygame

#table containing all the ID of keyboard keys currently pressed
KayboardStatus = []

def addKeyEv(key):
        KayboardStatus.append(pygame.key.name(key))

def removeKeyEv(key):
        KayboardStatus.remove(pygame.key.name(key))
        
def getPressedKeys():
        return KayboardStatus

def isKeyPressed(key):
        keyStatus = False
        
        for K in KayboardStatus:
                if K == key:
                        keyStatus = True
              
        return keyStatus

