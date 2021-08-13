import string
import random as r

#GLOBAL CONTROL VARIABLES
CANVAS_SIZE_X = 1920
CANVAS_SIZE_Y = 1080
BACKGROUND_COLOR = color(0)
current_circles = []
MAX_R = 500

def setup():
    global CANVAS_SIZE_X, CANVAS_SIZE_Y, BACKGROUND_COLOR, current_circles, img, PIXEL_SAMPLES, MAX_R
    size(CANVAS_SIZE_X,CANVAS_SIZE_Y)
    background(BACKGROUND_COLOR)
    noFill()
    stroke(0)
    strokeWeight(2)
    translate(width/2,height/2)
    x = random(-width/2,width/2)
    y = random(-height/2,height/2)
    r = random(5,MAX_R)
    current_circles.append(PVector(x,y,r))
    img = loadImage('bodacious-sweet-corn.jpg')
    loadPixels()
    img.loadPixels()
    rand1 = floor(random(0,len(img.pixels)))
    PIXEL_SAMPLES = [rand1]
    stroke(PIXEL_SAMPLES[0])
    createCircle(x,y,r,'image')

    
                   
    
def createCircle(x,y,rad,c_type):
    if(c_type == 'cracked'):
        crackedCircle(x,y,rad)
    elif(c_type == 'solid'):
        solidCircle(x,y,rad)
    elif(c_type == 'image'):
        imageCircle(x,y,rad)
    
def crackedCircle(x,y,rad):
    circle(x,y,rad)
    num_cracks = floor(map(rad,0,500,5,10))
    strokeWeight(1)
    for i in range(num_cracks):
        angle1 = random(0,2*PI)
        angle2 = random(0,2*PI)
        x1 = rad/2*cos(angle1)
        y1 = rad/2*sin(angle1)
        x2 = rad/2*cos(angle2)
        y2 = rad/2*sin(angle2)
        line(x+x1,y+y1,x+x2,y+y2)
    strokeWeight(2)
    
def solidCircle(x,y,rad):
    circle(x,y,rad)
    
def imageCircle(x,y,rad):
    NUM_PIXELS = len(img.pixels)
    w = img.width
    LOCATION_IN_IMAGE = floor(random(0,NUM_PIXELS-height-w*2*rad))
    print(w)
    pushMatrix()
    translate(x,y)
    for i in range(ceil(rad)):
        for j in range(ceil(rad)):
            if(dist(i-rad/2,j-rad/2,0,0) < rad/2):
                ind = LOCATION_IN_IMAGE+i+j*w
                r = red(img.pixels[ind])
                g = green(img.pixels[ind])
                b = blue(img.pixels[ind])
                x_n = x+i-rad/2+width/2
                y_n = y+j-rad/2+height/2
                set(x_n,y_n,color(r,g,b))
    popMatrix()
    PIXEL_SAMPLES.append(color(r,g,b))
    circle(x,y,rad)

def draw():
    global current_circles, img, MAX_R
    translate(width/2,height/2)
    r = MAX_R
    for i in range(50):
        x = random(-width/2,width/2)
        y = random(-height/2,height/2)
        can_draw = True
        for i in range(len(current_circles)):
            c = current_circles[i]
            d_between = dist(x,y,c.x,c.y)
            if(d_between < r/2 + c.z/2):
                can_draw = False
                break
            if(d_between < c.z/2):
                can_draw = False
                break
        if can_draw:
            type = ''
            if r > 5:
                type = 'image'
            else:
                type = 'solid'
            sel = floor(random(0,len(PIXEL_SAMPLES)))
            stroke(PIXEL_SAMPLES[sel])
            createCircle(x,y,r,type)
            current_circles.append(PVector(x,y,r))
            break
        r = r/1.1
    
    print(len(current_circles))
    
def mousePressed():
    rs = randomString()
    save("corn_" + rs + ".png")
    
def randomString(stringLength=4):
    letters = string.ascii_lowercase
    return ''.join(r.choice(letters) for i in range(stringLength))
