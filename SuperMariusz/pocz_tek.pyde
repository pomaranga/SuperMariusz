value = 255
clr = 127   

def draw():
    global value, clr 
    fill(value)
    rect(170, 330, 250, 100)
    text("       WELCOME \nTO SUPERMARIUSZ!",width/4-40, height/3)
    fill(clr, 0, 0)
    text("START", 235, 395)
    
    if mousePressed == True:   
        if mouseX>=250 and mouseX<=420 and mouseY>=330 and mouseY<=430: 
            noLoop()    
        background(255)
        fill(50, 200, 0)
        rect(375, 225, 175, 15)
        rect(70, 100, 50, 20)
        rect(600, 175, 70, 15)
        rect(700, 125, 50, 20)
        rect(100, 325, 70, 15)
        rect(250, 275, 50, 20)
        rect(400, 75, 230, 15)
        rect(280, 125, 30, 20)
        rect(180, 125, 30, 20)
        fill(150, 75, 0)
        ellipse(710, 350, 100, 100)
    
def mouseClicked(): 
    if mouseX>=250 and mouseX<=420 and mouseY>=330 and mouseY<=430:
        global value, clr
        if value == 255:
            value = 0
        if clr == 127:
            clr = 0
        
def setup():
    size(600, 600)
    text_size = 40
    textSize(text_size)
    background(0)
    

    

    
