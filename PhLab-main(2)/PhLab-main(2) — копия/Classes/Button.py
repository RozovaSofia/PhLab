import pygame

from Constants import *

class Button:
    def __init__(self,size,position,text,color,function):
        self.size = size
        self.position = position
        self.text = text
        self.color = pygame.color.Color(color)
        self.function = function

        self.font = pygame.font.Font(None,50)
        self.text_image = self.font.render(self.text,True,"black")
        self.image = pygame.surface.Surface(self.size)
        self.image.fill(self.color)
        self.image.blit(self.text_image, (0,0))

    def create(self,surface):
        surface.blit(self.image,self.position)

    def clicked(self):
        self.function(space)







