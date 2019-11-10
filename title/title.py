import pygame
from time import sleep

class LogoPrinter:
    def __init__(self, width, height, screen):
        self.screen = screen
        self.logo_size = int(0.25 * height)
        self.whu = pygame.image.load("resources/pics/WHULogo.jpg").convert()
        self.member = pygame.image.load("resources/pics/MemberInfo.png").convert()
        self.whu = pygame.transform.scale(self.whu, (self.logo_size, self.logo_size))
        self.member = pygame.transform.scale(self.member,(width,int(0.5*height)))
        self.whu_rect = self.whu.get_rect()
        self.member_rect = self.member.get_rect()
        self.whu_rect.top = 0.125*height
        self.whu_rect.left = 0.25*height
        self.member_rect.top = 0.5*height
        self.fps = 30
        self.fClock = pygame.time.Clock()

    def display_logo(self):
        for i in range(0, 256, 8):
            self.whu.set_alpha(i)
            self.member.set_alpha(i)
            #print(self.whu.get_alpha())
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.whu, self.whu_rect)
            self.screen.blit(self.member, self.member_rect)
            pygame.display.update()
            self.fClock.tick(self.fps)

        sleep(2)

        for i in range(255, -1, -8):
            self.whu.set_alpha(i)
            self.member.set_alpha(i)
            #print(self.whu.get_alpha())
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.whu, self.whu_rect)
            self.screen.blit(self.member, self.member_rect)
            pygame.display.update()
            self.fClock.tick(self.fps)

class TitleInterface:
    def __init__(self,width,height,screen):
        self.screen = screen
        self.toptitle = pygame.image.load('resources/pics/titleBackground.ver1.jpg')
        self.bottomtitle = pygame.image.load('resources/pics/UnderTheTitle.jpg')
        self.toptitle = pygame.transform.scale(self.toptitle,(width,int(0.5*height)))
        self.bottomtitle = pygame.transform.scale(self.bottomtitle,(width,int(0.5*height)))
        self.toptitle_rect = self.toptitle.get_rect()
        self.bottomtitle_rect = self.bottomtitle.get_rect()
        self.bottomtitle_rect.top = 0.5*height
        self.fps = 30
        self.fClock = pygame.time.Clock()
    def display_title(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and False:
                        print('nextPart')

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.toptitle, self.toptitle_rect)
            self.screen.blit(self.bottomtitle, self.bottomtitle_rect)
            pygame.display.update()
            self.fClock.tick(self.fps)
