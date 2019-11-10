import pygame
from time import sleep

class LogoPrinter:
    def __init__(self, width, height, screen):
        self.screen = screen
        self.logo_size = int(0.25 * height)
        self.whu = pygame.image.load("resources/pics/WHULogo.jpg").convert()
        self.whu = pygame.transform.scale(self.whu, (self.logo_size, self.logo_size))
        self.whu_rect = self.whu.get_rect()
        self.whu_rect.top = 0.125*height
        self.whu_rect.left = 0.25*height
        self.fps = 30
        self.fClock = pygame.time.Clock()

    def display_logo(self):
        for i in range(0, 256, 8):
            self.whu.set_alpha(i)
            #print(self.whu.get_alpha())
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.whu, self.whu_rect)
            pygame.display.update()
            self.fClock.tick(self.fps)

        sleep(1)

        for i in range(255, -1, -8):
            self.whu.set_alpha(i)
            #print(self.whu.get_alpha())
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.whu, self.whu_rect)
            pygame.display.update()
            self.fClock.tick(self.fps)

        #sleep(1)