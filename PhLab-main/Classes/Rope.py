


class Rope :
    def __init__(self, a):
        self.mass = a["mass"]
        self.pos_x = a["pos_x"]
        self.pos_y = a["pos_y"]
        self.radius = a["radius"]

    def create(self,space):
        for i in len(position):
            c[i] = Circle()
            c[i].create(space)
            if i!=0 :
                r = RigidConnection()
                r.create(space)