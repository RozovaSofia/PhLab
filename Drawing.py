import pygame as pg
from PyMunkSettings import *
from PyGameSettings import *
from Platform import Platform
from Circle import Circle
from Square import Square

# Класс Рисование
# Рисует и создает объекты в соответствии с нажатием мыши

def DrawThePicture (space):
    while True:
        surface.fill(pg.Color('white'))
        P = Platform(2,1,2)
        P.create(space)
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()

            if i.type == pg.MOUSEBUTTONDOWN:
                if i.button == 1:
                    C=Circle(1,60)
                    C.create(i.pos,space)


        space.step(1 / FPS)
        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)
