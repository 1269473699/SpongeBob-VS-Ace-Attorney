import pygame
from time import sleep
from util.Button import Button


class LogoPrinter:
    def __init__(self, width, height, screen):#构造函数
        self.screen = screen
        self.logo_size = int(0.25 * height)
        self.whu = pygame.image.load("resources/pics/WHULogo.jpg").convert()
        self.member = pygame.image.load("resources/pics/MemberInfo.png").convert()
        self.whu = pygame.transform.scale(self.whu, (self.logo_size, self.logo_size))
        self.member = pygame.transform.scale(self.member, (width, int(0.5*height)))
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
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.whu, self.whu_rect)
            self.screen.blit(self.member, self.member_rect)
            pygame.display.update()
            self.fClock.tick(self.fps)

        sleep(2)

        for i in range(255, -1, -8):
            self.whu.set_alpha(i)
            self.member.set_alpha(i)
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.whu, self.whu_rect)
            self.screen.blit(self.member, self.member_rect)
            pygame.display.update()
            self.fClock.tick(self.fps)
        sleep(1)


class TitleInterface:
    def __init__(self, width, height, screen):
        self.screen = screen
        self.top_title = pygame.image.load('resources/pics/titleBackground_ver1.jpg')
        self.bottom_title = pygame.image.load('resources/pics/UnderTheTitle.jpg')
        self.top_title = pygame.transform.scale(self.top_title, (width, int(0.5*height)))
        self.bottom_title = pygame.transform.scale(self.bottom_title, (width, int(0.5*height)))
        self.top_title_rect = self.top_title.get_rect()
        self.bottom_title_rect = self.bottom_title.get_rect()
        self.bottom_title_rect.top = 0.5*height
        self.title_text = [pygame.image.load('resources/pics/GameStart.png').convert_alpha(),
                           pygame.image.load('resources/pics/ChooseChapter.png').convert_alpha(),
                           pygame.image.load('resources/pics/GameExit.png').convert_alpha()]
        button_width = int(height * 0.25 * 0.4 * 0.9 / 1.65)
        button_height = int(0.25 * 0.9 * height * 0.4)
        button1_top = 0.625 * height - 0.5 * button_height
        button2_top = 0.75 * height - 0.5 * button_height
        button3_top = 0.875 * height - 0.5 * button_height
        button_left = 0.15 * width
        for i in (0,1,2):
            self.title_text[i] = pygame.transform.scale(self.title_text[i], (int(button_height * 0.7 * 3.93), int(button_height * 0.7)))
        self.title_text_rect = [self.title_text[0].get_rect(),
                                self.title_text[0].get_rect(),
                                self.title_text[0].get_rect()]
        self.title_text_rect[0].top = 0.625 * height - 0.35 * button_height
        self.title_text_rect[0].left = 0.33 * width
        self.title_text_rect[1].top = 0.75 * height - 0.35 * button_height
        self.title_text_rect[1].left = 0.33 * width
        self.title_text_rect[2].top = 0.875 * height - 0.35 * button_height
        self.title_text_rect[2].left = 0.33 * width
        self.fps = 30
        self.fClock = pygame.time.Clock()
        button_surfaces = [pygame.image.load('resources/pics/Jellyfish(origin).png'),
                           pygame.image.load('resources/pics/Jellyfish(on).png'),
                           pygame.image.load('resources/pics/Jellyfish(click).png')]
        pygame.mixer.init()
        onse1 = pygame.mixer.Sound("resources/music/Jellyfishh.wav")
        onse2 = pygame.mixer.Sound("resources/music/Jellyfishc.wav")
        self.stb1 = Button(button_width, button_height, screen, button_surfaces, button1_top, button_left, onse1, onse2)
        self.stb2 = Button(button_width, button_height, screen, button_surfaces, button2_top, button_left, onse1, onse2)
        self.stb3 = Button(button_width, button_height, screen, button_surfaces, button3_top, button_left, onse1, onse2)

    def display_title(self):
        pygame.mixer.music.load("resources/music/Title.mp3")
        pygame.mixer.music.play(-1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and False:
                        print('nextPart')
                elif event.type == pygame.MOUSEMOTION:
                    self.stb1.respond_to_hovering(event)
                    self.stb2.respond_to_hovering(event)
                    self.stb3.respond_to_hovering(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.stb1.respond_to_clicking(event)
                    self.stb2.respond_to_clicking(event)
                    self.stb3.respond_to_clicking(event)

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.top_title, self.top_title_rect)
            self.screen.blit(self.bottom_title, self.bottom_title_rect)
            self.stb1.display_button()
            self.stb2.display_button()
            self.stb3.display_button()
            for i in(0,1,2):
                self.screen.blit(self.title_text[i],self.title_text_rect[i])
            pygame.display.update()
            self.fClock.tick(self.fps)
