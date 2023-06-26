from Constants import *
from Constants import *
from Classes.Circle import Circle


class Spring:
    def __init__(self, a):
        self.joint = pymunk.DampedSpring( a["first"].body, a["second"].body, (0, 0), (0, 0), a["rest_length"], a["stiffness"], a["damping"])

    def create(self, space):
        space.add(self.joint)