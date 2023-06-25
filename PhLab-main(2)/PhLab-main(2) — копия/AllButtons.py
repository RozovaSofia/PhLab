from Classes.Button import Button
from Drawing import DrawThePicture
from Constants import *

menu_buttons=[]

start = Button([100,50],[200,200],"Start",[255,255,255],DrawThePicture)
menu_buttons.append(start)

end = Button([100,50],[100,100],"End",[0,100,0],exit)
menu_buttons.append(end)