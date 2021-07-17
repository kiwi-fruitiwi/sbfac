# represents an object with position, velocity, acceleration, 
# max_speed, max_force, and radius


class Vehicle:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector(random(-1, 1), random(-1, 1))
        self.acc = PVector(0, 0)
        self.max_speed = random(4, 7)
        self.max_force = 0.05
        self.r = 10
    
    
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
