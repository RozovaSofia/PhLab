from GameBody.Unpacing import Unpacking_Modul
from Constants import space

a=Unpacking_Modul()
b=a.add(space)
d = a.Objects()

print(b)

for name in b:
    if name not in d['StaticBody']:
        mass = b[name].mass
        print(mass)






