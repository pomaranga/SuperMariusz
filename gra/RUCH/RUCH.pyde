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
    if ((keyPressed) and (key == 'A')):  # If the key is pressed
        x -= 1   # add 1 to x 
    if ((keyPressed) and (key == 'D')): 
        x += 1   
    if ((keyPressed) and (key == 'S')):  # If the key is pressed
        y += 1   # add 1 to x 
    if ((keyPressed) and (key == 'W')): 
        y -= 1   
    
    image(img, x, y, -40, 80)
