import pygame as pg
from Space import space
from Constants import *
from Classes.Platform import Platform
from Classes.Circle import Circle
from Classes.Square import Square
from Classes.Spring import Spring
from Unpacing import Unpacking_Modul
# Класс Рисование
# Рисует и создает объекты в соответствии с нажатием мыши

def DrawThePicture (space):
    a = Unpacking_Modul()
    a.add(space)
    while True:
        surface.fill(Backgroud_Color)
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()

        space.step(1 / FPS)
        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)
