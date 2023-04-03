import pygame as pg
from pymunk import Vec2d

from PyMunkSettings import *
from PyGameSettings import *
from Platform import Platform
from Circle import Circle
from Spring import Spring
from Square import Square
from JointCircles import RigidConnection
# Класс Рисование
# Рисует и создает объекты в соответствии с нажатием мыши

def DrawThePicture (space):
    P = Platform(2,9,2)
    P.create(space)
    #c1 = Circle(10, 25)
    #c2 = space.static_body
    #c2.position = [100, 100]
    #c3 = RigidConnection(c1, c2, [100, 100])
    #c3.create([100,100], space)
    while True:
        surface.fill(pg.Color('white'))
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()

            if i.type == pg.MOUSEBUTTONDOWN:
                if i.button == 1:
                    c1=Circle(10,25)
                    c0=Circle(10,25)
                    c0.create(Vec2d(*i.pos)+Vec2d(80,50),space)
                    c1.create(i.pos,space)
                    c2=Square(20,40,40)
                    c2.create(Vec2d(*i.pos)+Vec2d(-50,-70),space)

                    c3=RigidConnection(c1,c2,i.pos,Vec2d(*i.pos)+Vec2d(-50,-70))
                    c4=RigidConnection(c1,c0,i.pos,Vec2d(*i.pos)+Vec2d(80,50))
                    c3.create(space)
                    c4.create(space)






        space.step(1 / FPS)
        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)
