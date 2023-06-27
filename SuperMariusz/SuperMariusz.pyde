import time

class Klucz():
    def __init__(self):
        klucz = loadImage("key.png")
        image(klucz, 85, 80, 20, 20)

def setup():
    size (1000, 500) #do zmiany
    klucz = loadImage("key.png")
    image(klucz, 85, 80, 20, 20)
    global pos_x, pos_y, sm_Stand, sm_Walk, sm_Jump, is_walk, is_flipped, sm_StandFlipped, sm_WalkFlipped, sm_JumpFlipped
    pos_x=0
    pos_y=0
    sm_Stand = loadImage("SuperMariuszSpriteStand.png")
    sm_StandFlipped = loadImage("SuperMariuszSpriteStandLeft.png")
    sm_Walk = loadImage("SuperMariuszSpriteWalk.png")
    sm_WalkFlipped = loadImage("SuperMariuszSpriteWalkLeft.png")
    sm_Jump = loadImage("SuperMariuszSpriteJUMPMEN.png")
    sm_JumpFlipped = loadImage("SuperMariuszSpriteJUMPMENleft.png")
    is_walk = False
    is_flipped = False
    
def draw():
    global pos_x, pos_y, sm_Stand, sm_Walk, is_walk, is_flipped, sm_StandFlipped, sm_WalkFlipped, sm_JumpFlipped
    clear()
    
    klucz = Klucz()
    
    def FlipCheck(noflip,flip):
        if is_flipped == True:
            image(flip, pos_x, pos_y, 100, 100)
        else:
            image(noflip, pos_x, pos_y, 100, 100)
    
    def sm_walk():
        global is_walk
        if pos_x%17==0:
            is_walk = not is_walk
        if is_walk:
            FlipCheck(sm_Walk, sm_WalkFlipped)
        else:
            FlipCheck(sm_Stand, sm_StandFlipped)
        #https://py.processing.org/reference/rotateY.html - nie działa, trzeba bylo drogą siłową
        
    def sm_jump(): #he do be flyin'
        FlipCheck(sm_Jump, sm_JumpFlipped)
        
    if keyPressed:
        if keyCode == RIGHT: #prawo
            is_flipped = False
            sm_walk()
            pos_x+=5
        if keyCode == LEFT: #lewo
            is_flipped = True
            sm_walk()
            pos_x-=5
        if keyCode == UP: #w gore
            sm_jump()
            pos_y-=5
        if keyCode == DOWN: #w dol
            sm_jump()
            pos_y+=5
    else:
        FlipCheck(sm_Stand, sm_StandFlipped)
        
        
        
