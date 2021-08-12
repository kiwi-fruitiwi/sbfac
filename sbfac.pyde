# this is a python tutorial based on coding train's 
# 5.2 Seeking a Target video: nature of code 2.0 in P5.js
# https://www.youtube.com/watch?v=p1Ws1ZhG36g
# which is itself based on Craig Reynolds's paper
# "Steering Behaviors For Autonomous Characters"
# 
# v0.1:    project template, Vehicle.py +comments
# v0.2:    basic triangle chases ball with seek
# v0.3:    flee
# v0.4:    pursue, evade
# v0.4.1:  quadratic pursuit + evade in method
# v0.5:    draw velocity and acceleration vectors in Vehicle
# v0.6:    arrive
# v0.7:    9S hackbot
    

from Vehicle import *
from random import randint

def setup():
    global vehicles, target, seek
    
    colorMode(HSB, 360, 100, 100, 100)
    size(700, 700)
    # cam = PeasyCam(this, width/2, height/2, 0, 500)
    noStroke()
    frameRate(144)
    
    vehicles = []
    target = Target(randint(10, width-10), randint(10, height-10))
    seek = True
    
    # create the vehicles
    for i in range(0, 12):
        v = Vehicle(randint(10, width-10), randint(10, height-10))
        vehicles.append(v)    
    
    
def draw():
    global vehicles, target, seek
    
    background(210, 80, 40)    
    fill(0, 100, 80, 80)
    
    # quadratic_pursuit()
    
    # TODO: test target evade
    

    # create and display the target
    # TODO maybe make this ball a mover! - Cody
    # target_pos = PVector(mouseX, mouseY)
    target_pos = target.pos
        
    if seek:
        fill(90, 100, 100, 50)
    else:
        fill(0, 100, 100, 50)

    # target, which ellipses around our canvas
    target.show()
    # target.apply_force(PVector(150*cos(PI/180*frameCount), 150*sin(PI/180*frameCount)))
    target.pos.x = mouseX
    target.pos.y = mouseY
    target.update()    
    target.edge_wrap()


    # arrival demo
    for v in vehicles:
        if seek:
            v.apply_force(v.arrive(target_pos))
        else:
            v.apply_force(v.flee(target_pos))
        v.update()
        v.show()
    
    '''
    # display the vehicles in seek and flee mode
    for v in vehicles:
        if seek:
            v.apply_force(v.seek(target_pos))
        else:
            v.apply_force(v.flee(target_pos))
        v.update()
        v.show()
    '''
    

    # pursue and evade mode
    for v in vehicles:
        if seek:
            v.apply_force(v.pursue(target))
        else:
            v.apply_force(v.evade(target))
        v.show()
        v.update()
        v.edge_wrap()
        v.evade(v)
        
        

# each vehicle either pursues or evades all other vehicles
def quadratic_pursuit():
    global vehicles, seek
       
    for i in range(0, len(vehicles)):
        v = vehicles[i]
        
        for j in range(0, len(vehicles)):
            if i != j:
                if seek:
                    v.apply_force(v.pursue(vehicles[j]))
                else:
                    v.apply_force(v.evade(vehicles[j]))
            
        v.show()
        v.edge_wrap()    
        v.update()
        

def mousePressed():
    global seek
    
    seek = not seek
