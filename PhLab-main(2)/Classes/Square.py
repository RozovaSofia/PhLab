import pymunk
from random import randrange

# Класс Прямоугольник.
# Входные параметры: масса, сторона x, сторона y.
# Возможные параметры: коэффициенты трения и упругости.
# Умеет создаваться в определенном месте

class Square:
    def __init__(self, a):
        self.mass = a["mass"]
        self.pos_x = a["pos_x"]
        self.pos_y = a["pos_y"]
        self.size_x = a["size_x"]
        self.size_y = a["size_y"]
        self.size = (self.size_x,self.size_y)
        self.moment = pymunk.moment_for_box(self.mass,self.size)
        self.body = pymunk.Body(self.mass, self.moment)
        self.shape = pymunk.Poly.create_box(self.body, self.size)
        self.shape.elasticity = a["elasticity"]
        self.shape.friction = a["friction"]

    def create(self, space):
        self.body.position = (self.pos_x,self.pos_y)
        self.shape.color = [randrange(256) for i in range(4)]
        space.add(self.body, self.shape)