import pygame
import sys
from title.title import LogoPrinter,TitleInterface
from part1.part1 import Part1_printer
from part2.part2 import Part2Printer
#from util.DialogBox import DialogBox

pygame.init()
vInfo = pygame.display.Info()
size = height = vInfo.current_h
height = int(0.7 * height)
width = int(height * 0.75)
icon = pygame.image.load("resources/pics/MainIcon.jpg")
pygame.display.set_caption("海绵宝宝x逆转裁判")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((width, height))

if __name__ == '__main__':

    action = 0
    lp = LogoPrinter(width, height, screen)
    tp = TitleInterface(width, height, screen)
    p1p = Part1_printer(screen, width, height)
    p2p = Part2Printer(screen, width, height)
    temp = int(0.125*height)
    temp2 = int(0.375*height)
    #dl = DialogBox(screen, width, temp, temp2, 0)
    #action = 3
    if action == 0:
        lp.display_logo()
        action = action + 1

    if action == 1:
        tp.display_title()
        action = action + 1

    if action == 2:
        pygame.mixer.music.stop()
        p1p.display_part1()
        action = action + 1

    if action == 3:
        p2p.display_part2()



