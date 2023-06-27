import pygame as pg
from Constants import *
from Classes.Platform import Platform
from Classes.Circle import Circle
from Classes.Square import Square
from Classes.Point import Point
from GameBody.Unpacing import Unpacking_Modul
from AllButtons import setting_page_buttons
from GameBody.Picture import Picture
from GameBody.Unpacing import k
from SettingPage.Setting import Setting

a = Unpacking_Modul()
def DrawTheSetting (space):
    space.gravity = 0,0
    c = a.add(space)
    pict = Setting(setting_page_buttons)
    while pict.state == 'setting':
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
    for i in k.keys():
        k[i].delete_object(space)
    return pict.state