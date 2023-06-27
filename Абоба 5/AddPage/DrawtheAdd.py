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
from AllButtons import setting_page_buttons
from GameBody.Picture import Picture
from SettingPage.Setting import Setting


def DrawTheAdd(space):
    surface.fill([255,255,255])

    white = (255, 255, 255)
    black = (0, 0, 0)

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Mass', True, black, white)
    textRect = text.get_rect()
    textRect.center = (50,50)
    surface.blit(text, textRect)

    input_rect = pygame.Rect(100, 35, 140, 32)
    input_rect1 = pygame.Rect(400, 300, 300, 32)
    active = False
    active1 = False
    base_font = pygame.font.Font(None, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    user_text = ''
    user_text1 = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect1.collidepoint(event.pos):
                    active1 = True
                else:
                    active1 = False
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            if event.type == pygame.KEYDOWN and active1:
                if event.key == pygame.K_BACKSPACE:
                    user_text1 = user_text1[:-1]
                else:
                    user_text1 += event.unicode
            if active or active1:
                color = color_active
            else:
                color = color_passive

        pygame.draw.rect(surface, color, input_rect)
        pygame.draw.rect(surface, color, input_rect1)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        text_surface1 = base_font.render(user_text1, True, (255, 255, 255))
        surface.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        surface.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)
        input_rect1.w = max(100, text_surface1.get_width() + 10)
        pygame.display.flip()
        clock.tick(60)