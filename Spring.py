from PyMunkSettings import *
from PyGameSettings import *
from Circle import Circle
class Spring:
    def __init__(self,firstpos):

        self.b0 = space.static_body
        self.b0.position = [100, 200]

        self.body = Circle(50,90).body
        self.body.position = firstpos
        self.shape = Circle(50,90).shape


        self.joint = pymunk.DampedSpring(self.b0, self.body,(0,0),(0,0), 1, 10, 10)

    def create(self, pos, space):
        self.body.position = pos

        space.add(self.body,self.shape)
        space.add(self.joint)