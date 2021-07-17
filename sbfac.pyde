# this is a python tutorial based on coding train's 
# 5.2 Seeking a Target video: nature of code 2.0 in P5.js
# https://www.youtube.com/watch?v=p1Ws1ZhG36g
# which is itself based on Craig Reynolds's paper
# "Steering Behaviors For Autonomous Characters"
# 
# v0.1: project template, Vehicle.py +comments
# v0.2: basic triangle chases ball
# v0.3: 
    

from Vehicle import *
from random import randint

def setup():
    global vehicles, seek
    
    colorMode(HSB, 360, 100, 100, 100)
    size(1200, 700)
    # cam = PeasyCam(this, width/2, height/2, 0, 500)
    noStroke()
    vehicles = []
    seek = True
    
    # create the vehicles
    for i in range(0, 20):
        v = Vehicle(randint(10, width-10), randint(10, height-10))
        vehicles.append(v)    
    
    
def draw():
    global vehicles, seek
    
    background(210, 80, 40)    
    fill(0, 100, 80, 80)
    
    # create and display the target
    # TODO maybe make this ball a mover! - Cody
    target_pos = PVector(mouseX, mouseY)
    
    if seek:
        fill(90, 100, 100, 50)
    else:
        fill(0, 100, 100, 50)
            
    circle(target_pos.x, target_pos.y, 32)
    
    # display the vehicles
    for v in vehicles:
        if seek:
            v.apply_force(v.seek(target_pos))
        else:
            v.apply_force(v.flee(target_pos))
        v.update()
        v.show()

def mousePressed():
    global seek
    
    seek = not seek
