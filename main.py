import pygame
import sys
from title.title import LogoPrinter

pygame.init()
vInfo = pygame.display.Info()
size = height = vInfo.current_h
height = int(0.7 * height)
width = int(height * 0.75)
screen = pygame.display.set_mode((width, height))

if __name__ == '__main__':

    pygame.display.set_caption("海绵宝宝x逆转裁判")
    action = 0

    lp = LogoPrinter(width, height, screen)
    if action == 0:
        lp.display_logo()
        input()

