

# represents an object with position, velocity, acceleration, 
# max_speed, max_force, and radius
class Vehicle:
    def __init__(self, x, y):
        pass
    
    
    # set this object's velocity to follow the target it's seeking
    def seek(self, target):  # target is a location PVector
        # find the distance between us and the target
        
        # our steering direction is our target's location minus ours
        
        # our desired velocity is the position vector set to our max speed
        
        # apply force! be careful of force vs acc
        
        pass
        
        
    # assume self.mass is 1 so we don't need to worry about mass
    def apply_force(self, force):
        pass
        
    
    # how do the position and velocity change with each frame?
    # don't forget to limit the velocity!
    def update(self):
        pass
        
        
    # display the object
    def show(self):
        pass
        
        # rotate the object to point where its velocity vector points
        
        # draw the velocity vector
