import linecache
import sys
import pygame
import pygame.freetype
from util.RoleBuilder import RoleBuilder
from util.ActionBuilder import ActionBuilder
from util.Background import Background
from util.Evidence import Evidence
from time import sleep


class DialogBox:
    roles, role_rects = [], []
    speed = 1
    def __init__(self, screen, width, height,  buttons, evidenceList):
        '''self.top = top
        self.left = left'''
        self.buttons = buttons
        self.height = height
        self.width = width
        self.screen = screen
        #self.rect = self.surface.get_rect()
        self.fps = 30
        self.fClock = pygame.time.Clock()
        self.f = pygame.freetype.Font('resources/fonts/方正粗圆.ttf', 36)
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
        self.back_g = Background(width, height,
                                 'resources/pics/Black.png',
                                 'resources/pics/Background2.jpg', self.screen)
        self.sayer_text = ""
        mtop = int((self.dialog_text_rect.height - self.font_size) / 2) + self.dialog_text_rect.top
        self.text_pos = (self.font_size, mtop)
        mtop = int((self.dialog_sayer_rect.height - self.sayer_font_size) / 2) + self.dialog_sayer_rect.top
        self.sayer_pos = (self.font_size, mtop)
        self.evidenceList = evidenceList
        '''
        self.role = pygame.image.load('resources/pics/MayaStand1.gif').convert_alpha()
        self.role = pygame.transform.scale(self.role, (int(height*0.5*1.5), int(height*0.5)))
        self.role_rect = self.role.get_rect()
        self.role_rect.top = 0
        self.role_rect.left = 0
        '''
        self.i = 0
        self.condition = 0

    def clean_dialog(self, puncutaion): #输出对话内容时，每一帧都要调用一次该函数，作用是绘制文本之外的部分
        self.back_g.display_background(0)
        if len(self.roles) >= 1:
            self.screen.blit(self.roles[(self.i)//self.speed], self.role_rects[(self.i)//self.speed])
            if puncutaion == False:
                self.i = (self.i+1) % (len(self.roles)*self.speed)
        if self.table != "":
            # self.screen.blit(self.table_pic, (0, int(self.height*0.5 - 0.182812*0.5*self.height)))
            self.screen.blit(self.table_pic, self.table_point)
        if self.condition == 1:
            self.evidenceList[self.evidence].display_evidence()
        for button in self.buttons:
            button.display_button()
        if self.dialog_text != "":
            self.screen.blit(self.dialog_text, self.dialog_text_rect)
        if self.sayer_text != "":
            self.screen.blit(self.dialog_sayer, self.dialog_sayer_rect)
            self.f.render_to(self.screen, self.sayer_pos, self.sayer_text, fgcolor=(255, 255, 255),
                             size=self.sayer_font_size)



    def print_text(self, path, line_no, sound):


        punctuations = ('。', '：', '、', '！', '，', '（', '）', '.','(',')')
        global punctuation
        punctuation = False
        text = linecache.getline(path, line_no) #传入文本路径，行数和音效作为参数，每次读取一行
        if text == "":
            return 999

        texts = text.split("$") #以$为分隔符将一行分为个字符串
        if texts[1] == 'action' or texts[1] == 'action2':
            ab = ActionBuilder(texts[2], self.height)
            action_pics, action_rects, action_sound = ab.get_actions()
            action_speed = eval(texts[3])
            if texts[1] == 'action2':
                action_sound.play()
            for i in range(action_speed*len(action_pics)):
                self.screen.blit(action_pics[i//action_speed], action_rects[i//action_speed])
                pygame.display.update()
            if texts[1] == 'action':
                action_sound.play()
            return line_no

        background = texts[5]
        music = texts[6]
        self.table = texts[7]
        if background != "":
            self.back_g.change_background(background)
        if music != "":
            if music == "stop":
                pygame.mixer.music.stop()
            else:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(music)
                pygame.mixer.music.play(-1)
        if self.table != "":
            if self.table =="AccusationTable":
                self.table_pic = pygame.image.load("resources/pics/AccusationTable.png").convert_alpha()
                self.table_pic = pygame.transform.scale(self.table_pic, (int(0.825*self.width), int(0.182812*0.5*self.height)))
                self.table_point = (self.width - int(0.825*self.width), int(self.height * 0.5 - 0.182812 * 0.5 * self.height))
            elif self.table =="DefendTable":
                self.table_pic = pygame.image.load("resources/pics/DefendTable.png").convert_alpha()
                self.table_pic = pygame.transform.scale(self.table_pic, (int(0.825*self.width), int(0.182812*0.5*self.height)))
                self.table_point = (0, int(self.height * 0.5 - 0.182812 * 0.5 * self.height))

            elif self.table =="WitnessTable":
                self.table_pic = pygame.image.load("resources/pics/WitnessTable.png").convert_alpha()
                self.table_pic = pygame.transform.scale(self.table_pic, (int(0.825*self.width), int(0.182812*0.5*self.height)))
                self.table_point = (0, int(self.height * 0.5 - 0.182812 * 0.5 * self.height))

        color = texts[1] #0为说话者，1为颜色，2为说话内容，3为速度，4为人物动作
        dialogue = texts[2]
        self.speed = eval(texts[3])
        builder = RoleBuilder(texts[4], self.height)
        self.roles, self.role_rects = builder.get_roles()
        self.sayer_text = texts[0]
        i = 0
        self.evidence = 0
        while i < self.speed*len(dialogue):
            punctuation = False
            words = dialogue[:i//self.speed+1:1]
            self.f.render_to(self.screen, self.text_pos, words, fgcolor=pygame.Color(color),
                             size=self.font_size)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    '''for button in self.buttons:
                        if button.respond_to_clicking(event):
                            i = (len(dialogue)-1)*self.speed'''
                    if self.buttons[0].respond_to_clicking(event):
                        None
                    elif self.buttons[1].respond_to_clicking(event):
                        if self.condition == 0:
                            i = (len(dialogue) - 1) * self.speed
                        else:
                            self.evidence = (self.evidence + 1) % len(self.evidenceList)
                    elif self.buttons[2].respond_to_clicking(event):
                        self.evidence = (self.evidence - 1) % len(self.evidenceList)
                    elif self.buttons[3].respond_to_clicking(event):
                        self.buttons[3].enable(0)
                        self.buttons[4].enable(0)
                        self.buttons[5].enable(1)
                        self.buttons[2].enable(0)
                    elif self.buttons[4].respond_to_clicking(event):
                        None
                    elif self.buttons[5].respond_to_clicking(event):
                        self.buttons[3].enable(1)
                        self.buttons[4].enable(1)
                        self.buttons[5].enable(0)
                        self.buttons[2].enable(1)
                elif event.type == pygame.MOUSEBUTTONUP:
                    for button in self.buttons:
                        if button.respond_to_up(event):
                            button.display_button()
                            None
            self.condition = self.buttons[3].condition
            pygame.display.update()
            sound.stop()

            if words[len(words)-1] not in punctuations:
                sound.play()
            else:
                punctuation = True
            self.clean_dialog(punctuation)
            i = i+1
            self.fClock.tick(self.fps)
        self.i = 0
        self.clean_dialog(False)
        self.f.render_to(self.screen, self.text_pos, dialogue, fgcolor=pygame.Color(color),
                         size=self.font_size)

        pygame.display.update()
        next_text = linecache.getline(path, line_no+1)
        if next_text != "":
            next_texts = next_text.split("$")
            if next_texts[0] == 'play':
                tmp_sound = pygame.mixer.Sound(next_texts[1])
                line_no = line_no+1
                tmp_sound.play()

            elif next_texts[0] == 'goto':
                no = eval(next_texts[1])
                return no - 1

        for button in self.buttons:
            if button.i == 2:
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            button.respond_to_up(event)
                            button.display_button()
                            return line_no

        return line_no
