import pymunk
from Constants import *

# Класс Жесткое Соединение
# Соединяет два объекта, сохраняя расстояние между ними
# Входные параметры: два тела и позиция первого тела

class RigidConnection:

    def __init__(self,a):
        self.body = pymunk.PinJoint(a["first"].body, a["second"].body)


    def create(self, space):
        space.add(self.body)

    def delete_object(self,space):

        pymunk.Space.remove(space, self.body)

