import pygame as pg
from Constants import *
from Classes.Platform import Platform
from Classes.Circle import Circle
from Classes.Square import Square
from Classes.Point import Point
from GameBody.Unpacing import Unpacking_Modul
from AllButtons import game_page_buttons
from GameBody.Picture import Picture

# Класс Рисование
# Рисует и создает объекты в соответствии с нажатием мыши
a = Unpacking_Modul()
def DrawThePicture (space):
    a.add(space)
    pict = Picture(game_page_buttons)

    while pict.state == 'game':
        surface.fill(pg.Color('white'))
        pict.draw(surface)
        pict.update()

        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()



        space.step(1 / FPS)
        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)

    return pict.state
    space.quit