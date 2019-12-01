import pygame
from util.DialogBox import DialogBox
from util.Background import Background
from util.Button import Button, ChangeableButton
from util.Evidence import Evidence
import sys


class Part1_printer:

    def __init__(self, screen, width, height):
        self.i = 1
        self.condition = 0
        self.screen = screen
        self.fps = 30
        self.fClock = pygame.time.Clock()
        self.back_p1 = Background(width, height,
                                 'resources/pics/Lounge.png',
                                 'resources/pics/Background2.jpg', self.screen)
        self.black_bg = Background(width, height,
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
        #backButton.enable(1)
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
        self.evidenceList.append(Evidence('resources/pics/Evidence1.png', 'pictureOfCanteen', height, width, screen))
        self.evidenceList.append(Evidence('resources/pics/Evidence2.png', 'autopsyReport', height, width, screen))
        self.evidenceList.append(Evidence('resources/pics/Evidence3.png', 'pictureOfKitchen', height, width, screen))

        self.dialog_p1 = DialogBox(screen, width, height, self.back_p1, self.buttons, self.evidenceList)
        self.dialog_b = DialogBox(screen, width, height, self.black_bg, self.buttons, self.evidenceList)
        self.back_g = self.black_bg
        self.dialog = self.dialog_b
        self.sound = pygame.mixer.Sound("resources/sounds/Speak1.ogg")

    def display_part1(self):
        pygame.mixer.music.load("resources/music/Memory.mp3")
        pygame.mixer.music.play(-1)
        self.i = 1
        evidence = 0
        while True:

            self.dialog.print_text('resources/texts/Part1.txt', self.i, self.sound)
            flag = True
            flag2 = False
            while True and flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        #for button in self.buttons:
                        if self.buttons[0].respond_to_clicking(event): #威慑
                            None
                        elif self.buttons[1].respond_to_clicking(event): #播放
                            if self.condition == 0:
                                self.i = self.i + 1
                                flag2 = True
                            else:
                                evidence = (evidence + 1) % len(self.evidenceList)
                            if self.i == 11:
                                self.dialog = self.dialog_p1
                                self.back_g = self.back_p1
                                self.sound = pygame.mixer.Sound("resources/sounds/TextCommon.wav")
                                self.back_g.fade_in()
                                pygame.mixer.music.stop()
                                pygame.mixer.music.load("resources/music/Lounge.mp3")
                                pygame.mixer.music.play(-1)
                            if self.i == 12:
                                self.sound = pygame.mixer.Sound("resources/sounds/Speak1.ogg")

                        elif self.buttons[2].respond_to_clicking(event): #后退
                            evidence = (evidence - 1) % len(self.evidenceList)
                        elif self.buttons[3].respond_to_clicking(event): #返回
                            self.buttons[3].enable(0)
                            self.buttons[4].enable(0)
                            self.buttons[5].enable(1)
                            self.buttons[2].enable(0)
                        elif self.buttons[4].respond_to_clicking(event): #指证
                            None
                        elif self.buttons[5].respond_to_clicking(event): #证物袋
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
                #pygame.display.update()
                if self.condition == 1:
                    self.evidenceList[evidence].display_evidence()
                for button in self.buttons:
                        button.display_button()
                pygame.display.update()
