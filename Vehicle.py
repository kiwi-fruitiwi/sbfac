# represents an object with position, velocity, acceleration, 
# max_speed, max_force, and radius


class Vehicle(object):
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector(random(-1, 1), random(-1, 1))
        self.acc = PVector(0, 0)
        self.max_speed = random(3, 5) #* 0.1666
        self.max_force = random(0.02, 0.03)
        self.r = 20
        
        self.ACC_VECTOR_SCALE = 2000
            
    
    # this is the inverse of seek; you literally multiply the seek function's returned
    # force vector by -1
    def flee(self, target):
        return self.seek(target).mult(-1)
        
    
    # seek means: steer toward target at maximum speed
    # set this object's acceleration to follow the target it's seeking
    def seek(self, target):
        # remember: target is a location PVector
        
        # our desired velocity is to move at max speed directly toward the target
        desired = PVector.sub(target, self.pos) # difference of positions gives us a direction
        desired.setMag(self.max_speed)
        
        # steering = desired velocity - current velocity 
        # we want to convert this direction and magnitude into an acceleration vector
        desired.sub(self.vel)
        desired.limit(self.max_force)
        
        # apply force! be careful of force vs acc
        return desired
    
    
    # this function is seek, except the magnitude of our acceleration decreases
    # as the distance to the target decreases within a threshold radius r
    def arrive(self, target):
        # remember: target is a location PVector
        
        seek_result = self.seek(target)
        # our desired velocity is to move at max speed directly toward the target
        
        
        # new arrival code!
        threshold = 200  # the radius at which we should start slowing down
        force = PVector.sub(target, self.pos) # difference of positions gives us a direction
        distance = force.mag()
        if distance < threshold:
            f = map(distance, 0, threshold, 0, self.max_speed)
            force.setMag(f)
        else:
            force.setMag(self.max_speed)
        
        
        # steering = desired velocity - current velocity 
        # we want to convert this direction and magnitude into an acceleration vector
        force.sub(self.vel)
        force.limit(self.max_force)
        
        # apply force! be careful of force vs acc
        return force
    
    
    # pursue is seek except we predict where our target is going to be based on its velocity
    # then we seek that predicted location
    def pursue(self, target):
        # we want to predict where the target will be based on its velocity
        # this is the number of frames ahead our prediction is
        FRAMES_AHEAD = 15 
          
        # target is not a position vector, but a vehicle 
        # because we need to know its velocity
        target_pos = target.pos.copy()
        
        # we have to copy position and velocity because we don't want to mutate the original copy
        target_prediction = target.vel.copy()
        target_pos.add(target_prediction.mult(FRAMES_AHEAD))
        
        # fill(210, 80, 80, 50)
        # circle(target_pos.x, target_pos.y, 16)
        
        return self.seek(target_pos)

    
    # evade is the inverse of pursue, where we predict where our pursuer will be and flee
    # from that prediction
    def evade(self, pursuer):
        return self.pursue(pursuer).mult(-1)
        
        
    # assume self.mass is 1 so we don't need to worry about mass
    def apply_force(self, force):
        # F=ma. Since m=1, F=a
        force.limit(self.max_force)
        self.acc.add(force)
        
    
    # how do the position and velocity change with each frame?
    # don't forget to limit the velocity!
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.vel.limit(self.max_speed)
        self.acc = PVector(0, 0)
        
    
    # draw the acceleration vector    
    # TODO: add arrow
    def show_acc_vector(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        stroke(200, 100, 100, 50)
        strokeWeight(2)
        line(0, 0, self.ACC_VECTOR_SCALE*self.acc.x, self.ACC_VECTOR_SCALE*self.acc.y)
        noStroke()    
        popMatrix()
        print self.acc.mag()
        
    
    # display the object
    def show(self):        
        
        self.show_acc_vector()
        # rotate the object to point where its velocity vector points        
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        
        # draw vel vector
        VEL_VECTOR_SCALE = 10
        stroke(0, 100, 100, 50)
        strokeWeight(1)
        # velocity vector isn't useful because vehicles rotate in that direction
        # line(0, 0, VEL_VECTOR_SCALE*self.vel.x, VEL_VECTOR_SCALE*self.vel.y)
        noStroke()
        
        # rotate 
        rotate(self.vel.heading())
        
        # this is where we draw our object. we're going to try for a 9S Hackbot
        # https://puu.sh/I3E19/9d32002c25.png
        r = self.r
        
        T = 0.4 # how far away is the tip away from the origin?
        C = 0.2 # what is the radius of the inner circle?
        B = 0.3 # how far away is the butt away from the origin?
        
        fill(0, 0, 100, 75)
        stroke(0, 0, 0, 100)
        strokeWeight(1)
        beginShape()
        vertex(r, 0) # front tip
        vertex(0, r*T) # top
        vertex(-r*T, 0) # butt
        vertex(0, -r*T) # bottom
        vertex(r, 0) # front tip
        endShape()
        
        fill(0, 0, 0, 90)
        circle(0, 0, r*C)
        stroke(0, 0, 0, 100)
        strokeWeight(1)
        line(0, 0, -r*T, 0) # line to the butt
        
        x = (r*T)/(sqrt(3)+T)
        line(0, 0, x, sqrt(3)*x) # line to the top 120 degrees
        line(0, 0, x, -sqrt(3)*x) # line to the bottom 120 degrees
        
        # two little squares in the back
        rectMode(CENTER)
        fill(0, 0, 100, 50)
        strokeWeight(1)
        square(r*-B, r*T, r*0.2)
        square(r*-B, -r*T, r*0.2)        
        
        popMatrix()
        # draw the velocity vector? unnecessary because we rotate to that direction
    
    
    def edge_wrap(self):
        if self.pos.x + self.r > width:
            self.pos.x = self.r
        if self.pos.x - self.r < 0:
            self.pos.x = width - self.r
        
        if self.pos.y + self.r > height:
            self.pos.y = self.r
        if self.pos.y - self.r < 0:
            self.pos.y = height - self.r
        
