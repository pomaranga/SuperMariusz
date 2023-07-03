import time

class Klucz():
    def __init__(self):
        self.klucz = loadImage("key.png")
        self.klucz_podniesiony = False
        
    def sprawdz_kolizje(self):
        # Sprawdza kolizję postaci z kluczem
        if pos_x > 65 and pos_x < 105 and pos_y > 60 and pos_y < 100:
            self.klucz_podniesiony = True
            return True
        else:
            return False
        
class Drzwi():
    def __init__(self):
        self.otwarte = False
        self.kolor_drzwi = color(150, 75, 0)
        self.drzwi1 = ellipse(710, 350, 100, 100)
        
    def otworz_drzwi(self):
        self.otwarte = True
        self.kolor_drzwi = color(255, 255, 255)

klucz = None
drzwi = None
victory = False
na_drzwiach = False

def setup():
    size(1000, 500)
    global klucz, drzwi, pos_x, pos_y, sm_Stand, sm_Walk, sm_Jump, is_walk, is_flipped, sm_StandFlipped, sm_WalkFlipped, sm_JumpFlipped
    
    pos_x = 0
    pos_y = 0
    sm_Stand = loadImage("SuperMariuszSpriteStand.png")
    sm_StandFlipped = loadImage("SuperMariuszSpriteStandLeft.png")
    sm_Walk = loadImage("SuperMariuszSpriteWalk.png")
    sm_WalkFlipped = loadImage("SuperMariuszSpriteWalkLeft.png")
    sm_Jump = loadImage("SuperMariuszSpriteJUMPMEN.png")
    sm_JumpFlipped = loadImage("SuperMariuszSpriteJUMPMENleft.png")
    is_walk = False
    is_flipped = False
    
    klucz = Klucz()
    drzwi = Drzwi()

def draw():
    global pos_x, pos_y, sm_Stand, sm_Walk, is_walk, is_flipped, sm_StandFlipped, sm_WalkFlipped, sm_JumpFlipped, victory, na_drzwiach
    
    background(0)
    
    fill(drzwi.kolor_drzwi)
    drzwi.drzwi1 = ellipse(710, 350, 100, 100)
    
    # Sprawdza kolizję z kluczem
    if not klucz.klucz_podniesiony:
        klucz.sprawdz_kolizje()
    
    if klucz.sprawdz_kolizje():
        drzwi.otworz_drzwi()
        
    if not drzwi.otwarte:
        fill(drzwi.kolor_drzwi)
        drzwi.drzwi1 = ellipse(710, 350, 100, 100)
    
    if drzwi.otwarte:
        na_drzwiach = pos_x > 650 and pos_x < 780 and pos_y > 300 and pos_y < 400
    
    if drzwi.otwarte and na_drzwiach:
        victory = True
        fill(255)
        textSize(48)
        textAlign(CENTER, CENTER)
        text("Victory", width/2, height/2)
    
    def FlipCheck(noflip, flip):
        if is_flipped == True:
            image(flip, pos_x, pos_y, 100, 100)
        else:
            image(noflip, pos_x, pos_y, 100, 100)
    
    def sm_walk():
        global is_walk
        if pos_x % 17 == 0:
            is_walk = not is_walk
        if is_walk:
            FlipCheck(sm_Walk, sm_WalkFlipped)
        else:
            FlipCheck(sm_Stand, sm_StandFlipped)
    
    def sm_jump(): # he do be flyin'
        FlipCheck(sm_Jump, sm_JumpFlipped)
        
    if keyPressed:
        if keyCode == RIGHT: # prawo
            is_flipped = False
            sm_walk()
            pos_x += 5
        if keyCode == LEFT: # lewo
            is_flipped = True
            sm_walk()
            pos_x -= 5
        if keyCode == UP: # w górę
            sm_jump()
            pos_y -= 5
        if keyCode == DOWN: # w dół
            sm_jump()
            pos_y += 5
    else:
        FlipCheck(sm_Stand, sm_StandFlipped)
        
    if not klucz.klucz_podniesiony:
        image(klucz.klucz, 85, 80, 20, 20)
        
    
    
        

        
        
        
        
        
