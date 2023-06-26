import pymunk
import pygame as pg
import pymunk.pygame_util

# Настройки экрана и фона. Параметры для отрисовки.

RES = WIDTH, HEIGHT = 1000, 1000
FPS = 300

pg.init()
surface = pg.display.set_mode(RES)
surface1 = pg.display.set_mode(RES)
surface2 = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)
draw_options1 = pymunk.pygame_util.DrawOptions(surface1)
draw_options2 = pymunk.pygame_util.DrawOptions(surface2)

# Параметры физического пространства

space = pymunk.Space()

