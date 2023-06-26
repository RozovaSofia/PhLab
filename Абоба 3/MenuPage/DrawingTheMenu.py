import pygame as pg
from Constants import *
from MenuPage.Menu import Menu
from AllButtons import menu_buttons



def DrawTheMenu(space):

    menu = Menu(menu_buttons)

    while menu.state == 'menu':

        menu.draw(surface)
        menu.update()

        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()




        pg.display.flip()
        clock.tick(FPS)

    return menu.state