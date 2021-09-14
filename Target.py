from Vehicle import *

class Target(Vehicle):
    def __init__(self, x, y):
        super(Target, self).__init__(x, y)
        self.pos = PVector(x, y)
        self.max_speed = 18
        self.max_force = 15
        self.ACC_VECTOR_SCALE = 250
        
        
    def show(self):
        # rotate the object to point where its velocity vector points        
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(self.vel.heading())
        circle(0, 0, self.r*2)
        popMatrix()
        
        self.show_acc_vector()
