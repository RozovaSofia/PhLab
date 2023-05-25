from copy import copy
from Space import space
from Classes.Platform import Platform
from Classes.Circle import Circle
from Classes.Square import Square
from Classes.Spring import Spring
from Classes.JointCircles import RigidConnection
import yaml
from yaml.loader import FullLoader
#НАДО НАПИСАТЬ КОМЕНТАРИЙ
class Unpacking_Modul:
    def Option(self):
        with open(r".\objects.yaml") as f:
            garbage1 = yaml.load(f, Loader=FullLoader)
            Option1 = garbage1["Option"]
            return (Option1)

    def Objects(self):
        with open(r".\objects.yaml") as f:
            garbage1 = yaml.load(f, Loader=FullLoader)
            Objects1 = garbage1["Objects"]
            return (Objects1)

    def add(self,space):
        a = Unpacking_Modul().Objects()
        b = {}
        for i in a.keys():
            for j in a[i]:
                if i == "RigidConnection":
                    c = {"first": b[a[i][j]["first"]], "second": b[a[i][j]["second"]]}
                    j = globals()[i](c)
                    j.create(space)
                elif i == "Spring":
                    c = {"first": b[a[i][j]["first"]], "second": b[a[i][j]["second"]],
                         "rest_length": a[i][j]["rest_length"],
                         "stiffness": a[i][j]["stiffness"], "damping": a[i][j]["damping"]}
                    j = globals()[i](c)
                    j.create(space)
                else:
                    j1 = copy(j)
                    j = globals()[i](a[i][j])
                    b[j1] = j
                    j.create(space)