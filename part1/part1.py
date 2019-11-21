import pygame
from util.DialogBox import DialogBox
from util.Background import Background
from util.Button import Button
import sys

class Part1_printer:
    def __init__(self, screen, width, height):
        self.i = 1
        self.screen = screen
        self.fps = 30
        self.fClock = pygame.time.Clock()
        self.back_g = Background(width, height,
                                 'resources/pics/UnderTheTitle.jpg',
                                 'resources/pics/TitleBackgroundV1.jpg', self.screen)
        width1 = int(width*0.7)
        height1 = int(width1/1.2)
        top1 = int(height*0.5+30)
        left1 = 30
        surfaces = [pygame.image.load('resources/pics/DialogButtonR0.png'),
                           pygame.image.load('resources/pics/DialogButtonR0.png'),
                           pygame.image.load('resources/pics/DialogButtonR2.png')]
        sound1 = pygame.mixer.Sound("resources/sounds/DialogClicked.ogg")
        sound2 = pygame.mixer.Sound("resources/sounds/EmbarrassingSilence.ogg")
        self.buttons = []
        button1 = Button(width1, height1, screen, surfaces, top1, left1, sound2, sound1)
        self.buttons.append(button1)
        self.dialog = DialogBox(screen, width, height, self.back_g, self.buttons)


    def display_part1(self):
        while True:
            #self.screen.fill((255, 255, 255))
            #self.back_g.display_background()
            sound = pygame.mixer.Sound("resources/sounds/Speak1.ogg")
            self.dialog.print_text('resources/texts/Part1.txt', self.i, sound)
            flag = True
            flag2 = False
            while True and flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        for button in self.buttons:
                            if button.respond_to_clicking(event):
                                self.i = self.i + 1
                                button.display_button()
                                flag2 = True
                                break
                    elif event.type == pygame.MOUSEBUTTONUP:
                        for button in self.buttons:
                            button.display_button()
                            if button.respond_to_up(event):
                                if flag2:
                                    flag = False
                    pygame.display.update()
