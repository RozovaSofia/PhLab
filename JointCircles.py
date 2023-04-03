import pymunk
from PyMunkSettings import *

# Класс Жесткое Соединение
# Соединяет два объекта, сохраняя расстояние между ними
# Входные параметры: два тела и позиция первого тела

class RigidConnection:

    def __init__(self,first,second,firstpos,secondpos):

        #first.create(firstpos,space)
        #second.create(secondpos, space)
        self.body = pymunk.PinJoint(first.body,second.body,(0,0))

    def create(self, space):
        #self.body.position = pos
        space.add(self.body)

