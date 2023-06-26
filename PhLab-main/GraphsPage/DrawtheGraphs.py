from Constants import *
from GraphsPage.Graph import GraphsPage
from AllButtons import graphs_page_buttons
import pygame


def DrawTheGraphs (space):
    graphspage = GraphsPage(graphs_page_buttons)
    while True:

        menu.draw(surface)
        menu.update()

        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()


        space.step(1 / FPS)
        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)

