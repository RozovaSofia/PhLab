from GameBody.Drawing import vel
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

from Constants import *

from MenuPage.DrawingTheMenu import DrawTheMenu
from GameBody.Drawing import DrawThePicture
from GraphsPage.DrawtheGraphs import DrawTheGraphs

current_state = 'menu'

while True:

 if current_state == 'menu':

     current_state = DrawTheMenu(space)
     print(current_state)

 if current_state == 'game':

     current_state = DrawThePicture(space)
     print(current_state)

 if current_state == 'graphs':

     current_state = DrawTheGraphs(space)
     print(current_state)
     print(vel)









