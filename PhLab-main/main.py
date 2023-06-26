
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

from Constants import *

from MenuPage.DrawingTheMenu import DrawTheMenu
from GameBody.Drawing import DrawThePicture
from GraphsPage.DrawtheGraphs import DrawTheGraphs



while True:
 DrawTheMenu(space)
 DrawThePicture(space)
 DrawTheGraphs(space)







