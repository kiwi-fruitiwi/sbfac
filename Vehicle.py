# represents an object with position, velocity, acceleration, 
# max_speed, max_force, and radius


class Vehicle:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector(random(-1, 1), random(-1, 1))
        self.acc = PVector(0, 0)
        self.max_speed = random(3, 5)
        self.max_force = 0.2
        self.r = 10
    
    
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
    
    
    # pursue is seek except we predict where our target is going to be based on its velocity
    # then we seek that predicted location
    def pursue(self, target): 
        # target is not a position vector, but a vehicle 
        # because we need to know its velocity
        target_pos = target.pos.copy()
        
        # we have to copy position and velocity because we don't want to mutate the original copy
        target_prediction = target.vel.copy()
        
        target_pos.add(target_prediction.mult(15))
        
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
        self.acc.add(force)
        
    
    # how do the position and velocity change with each frame?
    # don't forget to limit the velocity!
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.vel.limit(self.max_speed)
        self.acc = PVector(0, 0)
        
        
    # display the object
    def show(self):        
        # rotate the object to point where its velocity vector points
        fill(0, 0, 100, 50)
        
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(self.vel.heading())
        # circle(self.pos.x, self.pos.y, self.r*2)
        r = self.r
        triangle(r, 0,
                 -r/2, r/2, 
                 -r/2, -r/2)
        
        popMatrix()
        # draw the velocity vector
    
    
    def edge_wrap(self):
        if self.pos.x + self.r > width:
            self.pos.x = self.r
        if self.pos.x - self.r < 0:
            self.pos.x = width - self.r
        
        if self.pos.y + self.r > height:
            self.pos.y = self.r
        if self.pos.y - self.r < 0:
            self.pos.y = height - self.r


class Target(Vehicle):
    def __init__(self, x, y):
        # Vehicle.__init__(self, x, y)
        Vehicle.__init__(self, x, y)
        self.pos = PVector(width/2, height/2-250)
        self.max_speed = 8
        
        
    def show(self):
        # rotate the object to point where its velocity vector points        
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(self.vel.heading())
        circle(0, 0, self.r*2)
        popMatrix()        
