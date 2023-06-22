value = 255
clr = 127   

def draw():
    global value, clr 
    fill(value)
    rect(170, 330, 250, 100)
    text("       WELCOME \nTO SUPERMARIUSZ!",width/4-40, height/3)
    fill(clr, 0, 0)
    text("START", 235, 395)
    
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
    

    

    
