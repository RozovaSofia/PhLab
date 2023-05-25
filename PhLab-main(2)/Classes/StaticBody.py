import pymunk
from random import randrange


class StaticBody:
    def __init__(self, a):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.pos_x=a["pos_x"]
        self.pos_y=a["pos_y"]

        if a["type"] == "circle":
            self.radius = a["radius"]
            self.shape = pymunk.Circle(self.body, self.radius)

        if a["type"] == "square":
            self.size_x = a["size_x"]
            self.size_y = a["size_y"]
            self.size = (self.size_x, self.size_y)
            self.shape = pymunk.Poly.create_box(self.body, self.size)

        self.shape.elasticity = a["elasticity"]
        self.shape.friction = a["friction"]


    def create (self, space):
        self.body.position = (self.pos_x,self.pos_y)
        self.shape.color = [randrange(256) for i in range(4)]
        space.add(self.body, self.shape)


