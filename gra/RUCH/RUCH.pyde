y = 300

x = 80
def setup():
    global img
    size(400, 400)
    strokeWeight(4)
    img = loadImage('SuperMariuszSpriteChod.png')

def draw():
    global x, y, img
    background(204)
    if keyCode == LEFT and keyPressed == True:  
        x -= 1   
    if keyPressed== True and keyCode == RIGHT: 
        x += 1   
    if keyPressed == True and keyCode == DOWN: 
        y += 1  
    if keyCode == UP and keyPressed == True: 
        y -= 1   
    
    image(img, x, y, -40, 80)
