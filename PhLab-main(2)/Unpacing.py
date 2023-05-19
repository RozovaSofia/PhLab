from Classes.Platform import Platform
from Classes.Circle import Circle
from Classes.Square import Square
import yaml
from Constants import space
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
        for i in a.keys():
            for j in a[i]:
                c = globals()[i](a[i][j])
                c.create(space)