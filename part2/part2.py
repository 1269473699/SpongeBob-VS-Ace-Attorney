import pygame
from util.DialogBox2 import DialogBox
from util.Background import Background
from util.Button import Button, ChangeableButton
from util.Evidence import Evidence
from util.Question import QuestionBuilder
from util.ActionBuilder import ActionBuilder
from util.HealthBuilder import HealthBuilder
import sys


class Part2Printer:

    def __init__(self, screen, width, height):
        self.gameState = 1
        self.evidence = [0]
        self.add = False
        self.height = height
        self.width = width
        self.wrong = 203
        self.i = 1
        self.condition = 0
        self.screen = screen
        self.fps = 30
        self.fClock = pygame.time.Clock()
        self.question = QuestionBuilder(height, width, screen)
        self.back_g = Background(width, height,
                                 'resources/pics/Black.png',
                                 'resources/pics/Background2.jpg', self.screen)

        width1 = int(width * 0.7)
        height1 = int(width1 / 1.2)
        top1 = int(height * 0.5 + 30)
        left1 = 30
        surfaces = [pygame.image.load('resources/pics/DialogButtonR0.png'),
                    pygame.image.load('resources/pics/DialogButtonR0.png'),
                    pygame.image.load('resources/pics/DialogButtonR2.png')]
        deferSurfaces = [pygame.image.load('resources/pics/DeterButton1.png'),
                         pygame.image.load('resources/pics/DeterButton1.png'),
                         pygame.image.load('resources/pics/DeterButton2.png'),
                         pygame.image.load('resources/pics/DeterButton4.png')]
        playSurfaces = [pygame.image.load('resources/pics/DialogButtonR0.png'),
                        pygame.image.load('resources/pics/DialogButtonR0.png'),
                        pygame.image.load('resources/pics/DialogButtonR2.png'),
                        pygame.image.load('resources/pics/DialogButtonR0.png')]
        backSurfaces = [pygame.image.load('resources/pics/DialogButtonL0.png'),
                        pygame.image.load('resources/pics/DialogButtonL0.png'),
                        pygame.image.load('resources/pics/DialogButtonL1.png'),
                        pygame.image.load('resources/pics/DialogButtonL4.png')]
        returnSurfaces = [pygame.image.load('resources/pics/ReturnButton1.png'),
                          pygame.image.load('resources/pics/ReturnButton1.png'),
                          pygame.image.load('resources/pics/ReturnButton2.png'),
                          pygame.image.load('resources/pics/ReturnButton4.png')]
        evidenceSurfaces = [pygame.image.load('resources/pics/EvidenceButton1.png'),
                            pygame.image.load('resources/pics/EvidenceButton1.png'),
                            pygame.image.load('resources/pics/EvidenceButton2.png'),
                            pygame.image.load('resources/pics/EvidenceButton4.png')]
        exhibitSurfaces = [pygame.image.load('resources/pics/Exhibit.png'),
                           pygame.image.load('resources/pics/Exhibit.png'),
                           pygame.image.load('resources/pics/Exhibit.png'),
                           pygame.image.load('resources/pics/Exhibit4.png')]
        sound1 = pygame.mixer.Sound("resources/sounds/DialogClicked.ogg")
        sound2 = pygame.mixer.Sound("resources/sounds/EmbarrassingSilence.ogg")
        self.buttons = []
        button1 = Button(width1, height1, screen, surfaces, top1, left1, sound2, sound1)
        # self.buttons.append(button1)
        deterButton = ChangeableButton(int(0.15 * width), int(0.125 * width), screen, deferSurfaces,
                                       int((0.5 + 0.03 * 0.5) * height), int(0.02 * width), sound2, sound1)
        playButton = ChangeableButton(int(0.15 * width), int(0.125 * width), screen, playSurfaces,
                                      int(0.985 * height - 0.125 * width), int(0.83 * width), sound2, sound1)
        playButton.enable(1)
        backButton = ChangeableButton(int(0.15 * width), int(0.125 * width), screen, backSurfaces,
                                      int(0.985 * height - 0.125 * width), int(0.02 * width), sound2, sound1)
        # backButton.enable(1)
        returnButton = ChangeableButton(int(0.15 * width), int(0.125 * width), screen, returnSurfaces,
                                        int(0.985 * height - 0.125 * width), int(0.6 * width), sound2, sound1)
        exhibitButton = ChangeableButton(int(0.15 * width), int(0.125 * width), screen, evidenceSurfaces,
                                         int(0.985 * height - 0.125 * width), int(0.25 * width), sound2, sound1)
        exhibitBag = ChangeableButton(int(0.2 * height), int(0.2 * height), screen, exhibitSurfaces,
                                      int(0.65 * height), int(0.5 * width - 0.1 * height), sound2, sound1)
        exhibitBag.enable(1)
        self.buttons.append(deterButton)
        self.buttons.append(playButton)
        self.buttons.append(backButton)
        self.buttons.append(returnButton)
        self.buttons.append(exhibitButton)
        self.buttons.append(exhibitBag)

        self.evidenceList = []
        self.evidenceList.append(Evidence('resources/pics/Evidence2.png', 'pictureOfCanteen', height, width, screen))
        self.evidenceList.append(Evidence('resources/pics/Evidence1.png', 'autopsy', height, width, screen))
        self.evidenceList.append(Evidence('resources/pics/Evidence3.png', 'pictureOfKitchen', height, width, screen))
        self.evidenceList.append(Evidence('resources/pics/Evidence4.png', 'eggBurger', height, width, screen))

        self.dialog_p1 = DialogBox(screen, width, height, self.buttons, self.evidenceList, self.evidence)
        self.dialog_b = DialogBox(screen, width, height, self.buttons, self.evidenceList, self.evidence)
        self.dialog = self.dialog_b
        self.sound = pygame.mixer.Sound("resources/sounds/TextCommon.wav")
        self.link = {128: 138, 129: 146, 130: 158, 131: 164, 132: 176, 133: 186, 134: 193, 303: 315, 304: 325, 305: 339,
                     306: 359, 307: 367, 308: 375, 460: 470, 461: 479, 462: 485, 463: 496, 464: 504, 465:511}
        self.present = {132:'eggBurger', 305:'poison', 464: 'autopsy', 582 : 'eggBurger'}
        self.presentLine = {132:210, 305:388, 464:520, 582 : 584}
        self.deterAction = ActionBuilder("PhoenixDeter", height)
        self.objectionAction = ActionBuilder("PhoenixObjection", height)
        self.kuraeAction = ActionBuilder("Kurae", height)

    def display_part2(self):
        self.evidence[0] = 0
        self.i = 416
        while True:
            if self.i == self.wrong+5:
                self.dialog.hpbd.damaged()
                self.i = self.last_text
                continue
            if self.i == 1000:
                return None
            if self.dialog.hpbd.hp <= 0 and self.gameState:
                self.gameState = 0
                self.i = 678
            if self.i == 681 and self.gameState == 0:
                return 1
            self.i = self.dialog.print_text('resources/texts/Part2.txt', self.i, self.sound)  # 返回值为内部作用后返回的行号
            flag = True
            flag2 = False
            while True and flag:
                if pygame.event.get_blocked(pygame.MOUSEBUTTONUP):
                    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        # for button in self.buttons:
                        if self.buttons[0].respond_to_clicking(event):  # 威慑
                            if self.i in self.link:
                                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                                self.display_deter()
                                self.i = self.link.get(self.i)
                                flag2 = True
                                #print(self.i)
                        elif self.buttons[1].respond_to_clicking(event):  # 播放
                            if self.condition == 0:
                                if self.i != 582:
                                    self.i = self.i + 1
                                    flag2 = True
                            else:
                                self.evidence[0] = (self.evidence[0] + 1) % len(self.evidenceList)
                                b=3
                            if self.i == 2:
                                self.sound = pygame.mixer.Sound("resources/sounds/Speak1.ogg")

                        elif self.buttons[2].respond_to_clicking(event):  # 后退
                            self.evidence[0] = (self.evidence[0] - 1) % len(self.evidenceList)
                        elif self.buttons[3].respond_to_clicking(event):  # 返回
                            self.buttons[3].enable(0)
                            self.buttons[4].enable(0)
                            self.buttons[5].enable(1)
                            self.buttons[2].enable(0)
                        elif self.buttons[4].respond_to_clicking(event):  # 指证
                                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                                if self.i == 582:
                                    roles, role_rects, action_sound = self.kuraeAction.get_actions()
                                    action_sound.play()
                                    for i in range(15):
                                        self.screen.blit(roles[0], role_rects[0])
                                        pygame.display.update()
                                        self.fClock.tick(30)
                                    if self.present.get(self.i) == self.evidenceList[self.evidence[0]].title:
                                        pygame.mixer.music.stop()
                                        self.i = self.presentLine.get(self.i)
                                        flag2 = True
                                    else:
                                        self.last_text = self.i
                                        self.i = self.wrong
                                        flag2 = True

                                else:
                                    if self.i in self.presentLine.keys():
                                        roles, role_rects, action_sound = self.objectionAction.get_actions()
                                        action_sound.play()
                                        for i in range(15):
                                            self.screen.blit(roles[0], role_rects[0])
                                            pygame.display.update()
                                            self.fClock.tick(30)
                                        if self.present.get(self.i) == self.evidenceList[self.evidence[0]].title:
                                            pygame.mixer.music.stop()
                                            self.i = self.presentLine.get(self.i)
                                            flag2 = True
                                        else:
                                            self.last_text = self.i
                                            self.i = self.wrong
                                            flag2 = True

                        elif self.buttons[5].respond_to_clicking(event):  # 证物袋
                            self.buttons[3].enable(1)
                            self.buttons[4].enable(1)
                            self.buttons[5].enable(0)
                            self.buttons[2].enable(1)

                    elif event.type == pygame.MOUSEBUTTONUP:
                        for button in self.buttons:
                            if button.i == 2:
                                button.i = 1
                        if self.buttons[1].respond_to_up(event):
                            if flag2:
                                flag = False
                self.condition = self.buttons[3].condition
                self.back_g.display_background(1)
                # pygame.display.update()
                if self.condition == 1:
                    self.evidenceList[self.evidence[0]].display_evidence()
                for button in self.buttons:
                    button.display_button()
                self.dialog.hpbd.display_health()
                pygame.display.update()
            if self.i == 37:
                self.i = self.question.display_question(0)
            elif self.i == 542:
                self.i = self.question.display_question(1)
            elif self.i == 94 or self.i == 267:
                self.back_g.change_background("resources/pics/Witness.png")
                pygame.mixer.music.stop()
                pygame.mixer.music.load("resources/music/Witness.mp3")
                pygame.mixer.music.play(-1)
                self.back_g.fade_in()

            elif self.i == 114 or self.i == 286 or self.i == 448:
                self.back_g.change_background("resources/pics/Black.png")
                pygame.mixer.music.stop()
                self.back_g.fade_in()

            elif self.i == 614:
                self.back_g.change_background("resources/pics/Lounge.png")
                self.back_g.fade_in()

            elif self.i == 298:
                auto = Evidence('resources/pics/Autograph.png', 'autograph', self.height, self.width, self.screen)
                self.evidenceList.append(auto)

            elif self.i == 354:
                if self.add:
                    self.i = 305
                poison = Evidence('resources/pics/Poison.png', 'poison', self.height, self.width, self.screen)
                self.evidenceList.append(poison)
                self.add = True


    def display_deter(self):
        roles, role_rects, action_sound = self.deterAction.get_actions()
        action_sound.play()
        for i in range(30):
            self.screen.blit(roles[0], role_rects[0])
            pygame.display.update()
            self.fClock.tick(30)
        #pygame.event.get_blocked(pygame.MOUSEBUTTONUP)
        #mm=2
