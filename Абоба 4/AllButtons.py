from ButtonsFunctions import *
from Classes.Button import Button

exit_page_buttons = []

menu_buttons=[]

graphs_page_buttons = []

game_page_buttons=[]

setting_page_buttons = []

to_menu_from_exit_page = Button([100,50],[100,100],"To menu",[0,100,0],to_menu)
exit_page_buttons.append(to_menu_from_exit_page)

leave = Button([100,50],[200,200],"Leave",[0,100,0],to_menu)
exit_page_buttons.append(leave)



start = Button([100,50],[200,200],"Start",[255,255,255],to_game)
menu_buttons.append(start)


see = Button([100,50],[300,300],"see",[255,255,255],to_graphs)
menu_buttons.append(see)



out = Button([100,50],[100,100],"To menu",[0,100,0],to_menu)
graphs_page_buttons.append(out)


out1 = Button([100,50],[100,100],"To menu",[0,100,0],to_menu)
game_page_buttons.append(out1)

set = Button([100,50],[300,100],"To setting",[0,100,0],to_setting)
menu_buttons.append(set)

set11 = Button([100,50],[400,150],"Platform",[0,100,0],to_add)
setting_page_buttons.append(set11)