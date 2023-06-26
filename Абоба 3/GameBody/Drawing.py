import pygame as pg
from Constants import *
from Classes.Platform import Platform
from Classes.Circle import Circle
from Classes.Square import Square
from Classes.Point import Point
from GameBody.Unpacing import Unpacking_Modul
from AllButtons import game_page_buttons
from GameBody.Picture import Picture
from GameBody.Unpacing import k

# Класс Рисование
# Рисует и создает объекты в соответствии с нажатием мыши

a = Unpacking_Modul()
vel = {}

def DrawThePicture (space):
    c = a.add(space)
    pict = Picture(game_page_buttons)
    cnt = 0
    b = a.Objects()

    while pict.state == 'game':
        surface.fill(pg.Color('white'))
        pict.draw(surface)
        pict.update()

        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()

        cnt=cnt+1

        if cnt%10 == 0:
            o=c['1t']
            o.velocities.append(o.body.velocity)

        space.step(1 / FPS)
        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)

    global vel
    vel['1st']= c['1t'].velocities


    print(k)

    for i in k.keys():
        print(i)
        print (k[i])
        k[i].delete_object(space)


    return pict.state
