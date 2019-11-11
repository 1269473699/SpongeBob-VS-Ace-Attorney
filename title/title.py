import pygame
from time import sleep

class LogoPrinter:
    def __init__(self, width, height, screen):#构造函数
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
        sleep(1)


class TitleInterface:
    def __init__(self,width,height,screen):
        self.screen = screen
        self.top_title = pygame.image.load('resources/pics/titleBackground.ver1.jpg')
        self.bottom_title = pygame.image.load('resources/pics/UnderTheTitle.jpg')
        self.top_title = pygame.transform.scale(self.top_title, (width, int(0.5*height)))
        self.bottom_title = pygame.transform.scale(self.bottom_title,(width,int(0.5*height)))
        self.top_title_rect = self.top_title.get_rect()
        self.bottom_title_rect = self.bottom_title.get_rect()
        self.bottom_title_rect.top = 0.5*height
        self.fps = 30
        self.fClock = pygame.time.Clock()
        self.stb1 = StartButton(width, height, screen)
        self.stb1.button_rect.top = 0.625 * height - 0.5 * self.stb1.button_rect.height
        self.stb1.button_rect.left = 0.15 * width
        self.stb2 = StartButton(width, height, screen)
        self.stb2.button_rect.top = 0.75 * height - 0.5 * self.stb2.button_rect.height
        self.stb2.button_rect.left = 0.15 * width
        self.stb3 = StartButton(width, height, screen)
        self.stb3.button_rect.top = 0.875 * height - 0.5 * self.stb3.button_rect.height
        self.stb3.button_rect.left = 0.15 * width

    def display_title(self):
        i = [0, 0, 0]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and False:
                        print('nextPart')
                elif event.type == pygame.MOUSEMOTION:
                    if on_button(self.stb1, event):
                        i[0] = 1
                    elif on_button(self.stb2, event):
                        i[1] = 1
                    elif on_button(self.stb3, event):
                        i[2] = 1
                    else:
                        i = [0, 0, 0]
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if on_button(self.stb1, event):
                        i[0] = 2
                    elif on_button(self.stb2, event):
                        i[1] = 2
                    elif on_button(self.stb3, event):
                        i[2] = 2

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.top_title, self.top_title_rect)
            self.screen.blit(self.bottom_title, self.bottom_title_rect)
            self.stb1.display_button(i[0]);
            self.stb2.display_button(i[1]);
            self.stb3.display_button(i[2]);
            pygame.display.update()
            self.fClock.tick(self.fps)


def on_button(sb, event):
    if event.pos[0] > sb.button_rect.left and event.pos[0] < sb.button_rect.left + sb.button_rect.width and event.pos[1] > sb.button_rect.top and event.pos[1] < sb.button_rect.top + sb.button_rect.height:
        return 1
    else:
        return 0


class StartButton:
    def __init__(self, width, height, screen):
        self.surface = [pygame.image.load('resources/pics/jellyfish(origin).png'),
                        pygame.image.load('resources/pics/jellyfish(on).png'),
                        pygame.image.load('resources/pics/jellyfish(click).png')]

        self.screen = screen
        for i in (0, 1, 2):
            self.surface[i] = pygame.transform.scale(self.surface[i], (
            int(height * 0.25 * 0.4 * 0.9 / 1.65), int(0.25 * 0.9 * height * 0.4)))
        self.button_rect = self.surface[0].get_rect();

    def display_button(self, i):
        self.screen.blit(self.surface[i], self.button_rect)