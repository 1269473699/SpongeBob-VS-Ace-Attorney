import linecache
import sys
import pygame
import pygame.freetype
from util.RoleBuilder import RoleBuilder
from util import Background
from time import sleep


class DialogBox:
    roles, role_rects = [], []
    speed = 1
    def __init__(self, screen, width, height, background, buttons):
        '''self.top = top
        self.left = left'''
        self.buttons = buttons
        self.height = height
        self.width = width
        self.screen = screen
        #self.rect = self.surface.get_rect()
        self.fps = 30
        self.fClock = pygame.time.Clock()
        self.f = pygame.freetype.Font('resources/fonts/站酷文艺体.ttf', 36)
        self.dialog_sayer = pygame.image.load('resources/pics/DialogBox_sayer.png').convert_alpha()
        self.dialog_sayer = pygame.transform.scale(self.dialog_sayer, (int(width * 0.25), int(0.125 * 0.35 * height)))
        self.dialog_text = pygame.image.load('resources/pics/DialogBox_text.png').convert_alpha()
        self.dialog_text = pygame.transform.scale(self.dialog_text, (width, int(0.125 * height)))
        self.dialog_sayer_rect = self.dialog_sayer.get_rect()
        self.dialog_text_rect = self.dialog_text.get_rect()
        self.dialog_text_rect.top = int(3 * height / 8)
        self.dialog_sayer_rect.top = self.dialog_text_rect.top - self.dialog_sayer_rect.height
        self.font_size = int(self.dialog_text_rect.height * 0.25)
        self.sayer_font_size = int(self.dialog_sayer_rect.height*0.6)
        self.back_g = background
        self.sayer_text = ""
        mtop = int((self.dialog_text_rect.height - self.font_size) / 2) + self.dialog_text_rect.top
        self.text_pos = (self.font_size, mtop)
        mtop = int((self.dialog_sayer_rect.height - self.sayer_font_size) / 2) + self.dialog_sayer_rect.top
        self.sayer_pos = (self.font_size, mtop)
        '''
        self.role = pygame.image.load('resources/pics/MayaStand1.gif').convert_alpha()
        self.role = pygame.transform.scale(self.role, (int(height*0.5*1.5), int(height*0.5)))
        self.role_rect = self.role.get_rect()
        self.role_rect.top = 0
        self.role_rect.left = 0
        '''
        self.i = 0

    def clean_dialog(self):
        self.back_g.display_background()
        self.screen.blit(self.roles[self.i//self.speed], self.role_rects[self.i//self.speed])
        self.i = (self.i+1) % (len(self.roles)*self.speed)
        for button in self.buttons:
            button.display_button()
        if self.dialog_text != "":
            self.screen.blit(self.dialog_text, self.dialog_text_rect)
        if self.sayer_text != "":
            self.screen.blit(self.dialog_sayer, self.dialog_sayer_rect)
            self.f.render_to(self.screen, self.sayer_pos, self.sayer_text, fgcolor=(255, 255, 255),
                             size=self.sayer_font_size)


    def print_text(self, path, line_no, sound):
        text = linecache.getline(path, line_no)
        texts = text.split("$")
        color = texts[1]
        dialogue = texts[2]
        self.speed = eval(texts[3])
        texts[4].rstrip()
        builder = RoleBuilder(texts[4], self.height)
        self.roles, self.role_rects = builder.get_roles()
        self.sayer_text = texts[0]
        i = 0
        while i < self.speed*len(dialogue):
            self.clean_dialog()
            words = dialogue[:i//self.speed+1:1]
            self.f.render_to(self.screen, self.text_pos, words, fgcolor=pygame.Color(color),
                             size=self.font_size)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.respond_to_clicking(event):
                            i = (len(dialogue)-1)*self.speed
                elif event.type == pygame.MOUSEBUTTONUP:
                    for button in self.buttons:
                        if button.respond_to_up(event):
                            button.display_button()
                            None
            pygame.display.update()
            sound.stop()
            sound.play()
            i = i+1
            self.fClock.tick(self.fps)

        for button in self.buttons:
            if button.i == 2:
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            button.respond_to_up(event)
                            button.display_button()
                            return
