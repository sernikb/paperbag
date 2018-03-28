#by sernikb2
#sernikb@gmail.com

#KeyUP & KeyDown event manager

#table containing all the ID of keyboard keys currently pressed
KayboardStatus = []

def addKeyEv(key):
        KayboardStatus.append(key)

def removeKeyEv(key):
        KayboardStatus.remove(key)
        
def getPressedKeys():
        return KayboardStatus

def isKeyPressed(key):
        keyStatus = False
        
        for K in KayboardStatus:
                if K == key:
                        keyStatus = True
              
        return keyStatus

