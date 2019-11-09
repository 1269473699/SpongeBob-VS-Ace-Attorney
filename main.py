import pygame
import sys
from title.title import sel_game

pygame.init()
pygame.display.set_caption("海绵宝宝x逆转裁判")
action = 0
vInfo = pygame.display.Info()
size = width, height = vInfo.current_w, vInfo.current_h
height = int(0.7*height)
width = int(height*0.75)

screen = pygame.display.set_mode((width, height))

if action == 0:
    while True:
        for event in pygame.event.get():
            sel_game(event)
        pygame.display.update()

