import pymunk

class Point:
    def __init__(self, a):
        self.pos_x = a["x"]
        self.pos_y = a["y"]
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)

    def create(self, space):
        self.body.position = (self.pos_x,self.pos_y)
        space.add(self.body)

    def delete_object(self,space):
        pymunk.Space.remove(space, self.body)