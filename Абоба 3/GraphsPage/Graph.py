
import pygame

class GraphsPage:

    def __init__(self,graphs_page_buttons):
        self.buttons = graphs_page_buttons
        self.state = 'graphs'



    def update(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            mouse_x,mouse_y = mouse_position
            for button in self.buttons:
                if button.position[0]<mouse_x<button.position[0]+button.size[0] and button.position[1] < mouse_y < button.position[1] + button.size[1] :
                    self.state = button.clicked()



    def draw(self,surface):

        image = pygame.surface.Surface([100, 200])
        image.fill([0, 0, 255])
        surface.fill((100, 100, 100))
        surface.blit(image, [200, 200])
        surface.blit(image, [200, 500])
        surface.blit(image, [200, 700])

        for button in self.buttons :
            button.create(surface)

