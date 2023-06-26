import pygame
from Constants import *
from OutPage.ExitPage import exitPage
from AllButtons import exit_page_buttons

def ExitWindow(space):
    while True:
        e = exitPage(exit_page_buttons)
        e.update()
        e.draw(surface)
        font = pygame.font.Font(None, 200)
        text_image = font.render("Are you sure?", True, "black")

        image = pygame.surface.Surface([400, 400])
        image.fill('white')
        image.blit(text_image, (0, 0))
        surface.fill((100, 100, 100))
        surface.blit(image, [0, 0])
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()


        space.step(1 / FPS)
        space.debug_draw(draw_options)

        pg.display.flip()
        clock.tick(FPS)
