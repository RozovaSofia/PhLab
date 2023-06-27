import sys
from Constants import surface
import pygame
import pygame as pg
from Constants import *
from Classes.Platform import Platform
from Classes.Circle import Circle
from Classes.Square import Square
from Classes.Point import Point
from GameBody.Unpacing import Unpacking_Modul
from AllButtons import add_page_buttons
from GameBody.Picture import Picture
from SettingPage.Setting import Setting
from AddPage.Add import Add
Data = {}


def DrawTheAdd(space):

    surface.fill([255,255,255])
    addpage = Add(add_page_buttons)
    white = (255, 255, 255)
    black = (0, 0, 0)

    font = pygame.font.Font('freesansbold.ttf', 32)
    text_mass = font.render('Mass', True, black, white)
    textRect = text_mass.get_rect()
    textRect.center = (50,50)
    surface.blit(text_mass, textRect)
    text_type = font.render('Type', True, black, white)
    textRect = text_mass.get_rect()
    textRect.center = (50, 250)
    surface.blit(text_type, textRect)

    input_rect_mass = pygame.Rect(100, 35, 140, 32)
    input_rect_type = pygame.Rect(300, 35, 240, 32)

    active = False
    active1 = False
    base_font = pygame.font.Font(None, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive


    user_text_mass = ''
    user_text_type = ''



    while addpage.state=='add':

        addpage.draw(surface)
        addpage.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_mass.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_type.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    user_text_mass = user_text_mass[:-1]
                else:
                    user_text_mass += event.unicode

            if event.type == pygame.KEYDOWN and active1:
                if event.key == pygame.K_BACKSPACE:
                    user_text_type = user_text_type[:-1]
                else:
                    user_text_type += event.unicode
            if active or active1:
                color = color_active
            else:
                color = color_passive

        pygame.draw.rect(surface, color, input_rect_mass)
        pygame.draw.rect(surface, color, input_rect_type)

        text_surface_mass = base_font.render(user_text_mass, True, (255, 255, 255))
        text_surface_type = base_font.render(user_text_type, True, (255, 255, 255))

        surface.blit(text_surface_mass, (input_rect_mass.x + 5, input_rect_mass.y + 5))
        surface.blit(text_surface_type, (input_rect_type.x + 5, input_rect_type.y + 5))

        input_rect_mass.w = max(100, text_surface_mass.get_width() + 10)
        input_rect_type.w = max(100, text_surface_type.get_width() + 10)

        pygame.display.flip()
        clock.tick(60)
    addpage.datamassive['mass'] = user_text_mass
    global Data
    Data['mass']=int(user_text_mass)
    Data['type']= 'circle'
    Data['radius'] = 80
    Data['pos_x'] = 700
    Data['pos_y'] = 100
    Data['friction'] = 10
    Data['elasticity'] = 0.1

    return addpage.state