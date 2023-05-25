import pymunk
from Space import space
import pygame as pg
import pymunk.pygame_util
from Unpacing import Unpacking_Modul
b = Unpacking_Modul()
b = b.Option()

# Настройки экрана и фона. Параметры для отрисовки.
RES = WIDTH, HEIGHT = b["WIDTH"], b["HEIGHT"]
FPS = b["FPS"]
Backgroud_Color = (b["Backgroud_Color_R"], b["Backgroud_Color_G"], b["Backgroud_Color_B"])

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

# Параметры физического пространства

space.gravity = b["gravity_x"], b["gravity_y"]









