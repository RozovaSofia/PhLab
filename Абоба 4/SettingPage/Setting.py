import pygame

class Setting:
    def __init__(self,setting_page_buttons):
        self.buttons = setting_page_buttons
        self.state = 'setting'

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            mouse_x,mouse_y = mouse_position
            for button in self.buttons:
                if button.position[0]<mouse_x<button.position[0]+button.size[0] and button.position[1] \
                        < mouse_y < button.position[1] + button.size[1] :
                    print(button.clicked())
                    self.state = button.clicked()

    def draw(self,surface):
        for button in self.buttons :
            button.create(surface)