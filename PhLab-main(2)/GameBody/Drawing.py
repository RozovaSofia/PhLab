import pygame as pg
from Constants import *
from Classes.Platform import Platform
from Classes.Circle import Circle
from Classes.Square import Square
from Classes.Point import Point
from GameBody.Unpacing import Unpacking_Modul

# Класс Рисование
# Рисует и создает объекты в соответствии с нажатием мыши
a = Unpacking_Modul()
def DrawThePicture (space):
    a.add(space)
    while True:
        surface.fill(pg.Color('white'))

        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()

            # if i.type == pg.MOUSEBUTTONDOWN:
            #     if i.button == 1:
            #         C=Square(12,100,100,1,1)
            #         C.create(i.pos,space)


        space.step(1 / FPS)
        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)
