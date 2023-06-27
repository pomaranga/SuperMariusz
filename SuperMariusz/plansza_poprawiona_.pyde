size(800, 400)
background(255)


class Platformy():
    fill(50, 200, 0)
    #od lewej do prawej
    p01 = rect(70, 100, 50, 20)
    p02 = rect(100, 325, 70, 15)
    p03 = rect(180, 125, 30, 20)
    p04 = rect(250, 275, 50, 20)
    p05 = rect(280, 125, 30, 20)
    p06 = rect(375, 225, 175, 15)
    p07 = rect(400, 75, 230, 15)
    p08 = rect(600, 175, 70, 15)
    p09 = rect(700, 125, 50, 20)



class Drzwi():
    fill(150, 75, 0)
    drzwi1 = ellipse(710, 350, 100, 100)
    
class Klucz():
    loadImage('key.png'(70, 80))
    
class Klucz():
    klucz = loadImage('key.png')
    image(klucz, 85, 80, 20, 20)
