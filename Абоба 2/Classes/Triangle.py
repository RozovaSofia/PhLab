import pymunk
from random import randrange


class Triangle :

    def __init__(self, a):
        self.mass = a["mass"]
        self.velocities = list()
        self.pos_x_1 = a["pos_x_1"]
        self.pos_y_1 = a["pos_y_1"]
        self.pos_x_2 = a["pos_x_2"]
        self.pos_y_2 = a["pos_y_2"]
        self.pos_x_3 = a["pos_x_3"]
        self.pos_y_3 = a["pos_y_3"]
        self.size = [(0,0),(self.pos_x_2-self.pos_x_1,self.pos_y_2-self.pos_y_1),(self.pos_x_3-self.pos_x_1,self.pos_y_3-self.pos_y_1)]
        self.moment = pymunk.moment_for_poly(self.mass,self.size)
        self.body = pymunk.Body(self.mass, self.moment)
        self.shape = pymunk.Poly(self.body, self.size)
        self.shape.elasticity = a["elasticity"]
        self.shape.friction = a["friction"]

    def create(self, space):
        self.body.position = (self.pos_x_1,self.pos_y_1)
        self.shape.color = [randrange(256) for i in range(4)]
        space.add(self.body, self.shape)
