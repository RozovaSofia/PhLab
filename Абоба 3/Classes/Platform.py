
from Constants import *
from Constants import *

# Класс Платформа
# Входные параметры: угол наклона, коэффициент трения, коэффициент упругости.
# Умеет создаваться (начало в левом нижнем углу)

class Platform:
    def __init__(self, a):

        self.pos1 = (a["pos1_x"],a["pos1_y"])
        self.pos2 = (a["pos2_x"],a["pos2_y"])
        self.width = a["width"]
        self.shape = pymunk.Segment(space.static_body, self.pos1, self.pos2, self.width)
        self.shape.elasticity = a["elasticity"]
        self.shape.friction = a["friction"]

    def create(self, space):
        space.add(self.shape)

    def delete_object(self,space):
        pymunk.Space.remove(space, self.shape)
