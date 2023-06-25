import pygame as pg
from Constants import *
from Menu.Menu import Menu
from AllButtons import menu_buttons



def DrawTheMenu(space):

    while True:

        menu=Menu(menu_buttons)
        menu.draw(surface)
        menu.update()
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()


        space.step(1 / FPS)
        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)
