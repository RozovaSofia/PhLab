from AddPage.DrawtheAdd import DrawTheAdd
from GameBody.Drawing import vel
import pymunk.pygame_util

from SettingPage.DrawtheSetting import DrawTheSetting

pymunk.pygame_util.positive_y_is_up = False

from Constants import *

from MenuPage.DrawingTheMenu import DrawTheMenu
from GameBody.Drawing import DrawThePicture
from GraphsPage.DrawtheGraphs import DrawTheGraphs

current_state = 'menu'

while True:
 if current_state == 'menu':
     current_state = DrawTheMenu(space)


 if current_state == 'game':
     current_state = DrawThePicture(space)


 if current_state == 'graphs':
     current_state = DrawTheGraphs(space)

 if current_state == "setting":
     current_state = DrawTheSetting(space)

 if current_state == "add":
     current_state = DrawTheAdd(space)
