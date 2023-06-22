def setup():
    size (1000, 500) #do zmiany

    #Mariusz chodzi i ladowanie tla
    global pos_x, pos_y, sm_Stand, sm_Walk, is_walk
    pos_x=0
    pos_y=0
    sm_Stand = loadImage("SuperMariuszSpriteStand.png")
    sm_Walk = loadImage("SuperMariuszSpriteWalk.png")
    is_walk = False
    
def draw():
    global pos_x, pos_y, sm_Stand, sm_Walk, is_walk
    clear()
    def sm_walk():
        global is_walk
        if pos_x%17==0:
            is_walk = not is_walk
        if is_walk:
            image(sm_Walk, pos_x, pos_y)
        else:
            image(sm_Stand, pos_x, pos_y)
        #https://py.processing.org/reference/rotateY.html
        
    if keyPressed:
        if keyCode == RIGHT: #prawo
            sm_walk()
            pos_x+=5
        if keyCode == LEFT: #lewo
            sm_walk()
            pos_x-=5
        if keyCode == UP: #w gore
            sm_walk()
            pos_y-=5
        if keyCode == DOWN: #w dol
            sm_walk()
            pos_y+=5
    else:
        image(sm_Stand, pos_x, pos_y)
            
