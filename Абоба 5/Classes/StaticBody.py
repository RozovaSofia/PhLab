import pymunk
from random import randrange


class StaticBody:
    def __init__(self, a):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        if a["type"]!="triangle":
            self.pos_x=a["pos_x"]
            self.pos_y=a["pos_y"]
        if a["type"] == "triangle":
            self.pos_x = a["pos_x_1"]
            self.pos_y = a["pos_y_1"]

        if a["type"] == "circle":
            self.radius = a["radius"]
            self.shape = pymunk.Circle(self.body, self.radius)

        if a["type"] == "square":
            self.size_x = a["size_x"]
            self.size_y = a["size_y"]
            self.size = (self.size_x, self.size_y)
            self.shape = pymunk.Poly.create_box(self.body, self.size)

        if a["type"] == "triangle":
            self.pos_x_1 = a["pos_x_1"]
            self.pos_y_1 = a["pos_y_1"]
            self.pos_x_2 = a["pos_x_2"]
            self.pos_y_2 = a["pos_y_2"]
            self.pos_x_3 = a["pos_x_3"]
            self.pos_y_3 = a["pos_y_3"]
            self.size = [(0, 0), (self.pos_x_2 - self.pos_x_1, self.pos_y_2 - self.pos_y_1),
                         (self.pos_x_3 - self.pos_x_1, self.pos_y_3 - self.pos_y_1)]
            self.shape = pymunk.Poly(self.body, self.size)





        self.shape.elasticity = a["elasticity"]
        self.shape.friction = a["friction"]


    def create (self, space):
        self.body.position = (self.pos_x,self.pos_y)
        self.shape.color = [randrange(256) for i in range(4)]
        space.add(self.body, self.shape)


    def delete_object(self,space):
        pymunk.Space.remove(space, self.shape)
        pymunk.Space.remove(space, self.body)