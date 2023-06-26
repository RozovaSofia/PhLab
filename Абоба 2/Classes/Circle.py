
import pymunk
from random import randrange

# Класс Круг.
# Входные параметры: масса, радиус.
# Возможные параметры: коэффициенты трения и упругости.
# Умеет создаваться в определенном месте


class Circle:
    def __init__(self, a):
        self.mass = a["mass"]
        self.radius = a["radius"]
        self.pos_x = a["pos_x"]
        self.pos_y = a["pos_y"]
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius, (0, 0))
        self.body = pymunk.Body(self.mass, self.moment)
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = a["elasticity"]
        self.shape.friction = a["friction"]

    def create(self, space):
        self.body.position = (self.pos_x,self.pos_y)
        self.shape.color = [randrange(256) for i in range(4)]
        space.add(self.body, self.shape)

