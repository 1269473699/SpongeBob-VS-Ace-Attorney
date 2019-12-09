import pygame
import sys


class QuestionBuilder:
    def __init__(self, height, width, screen):
        self.sound = pygame.mixer.Sound('resources/pics/OnChoose.ogg')
        self.height = int(0.5 * height)
        self.width = width
        self.surfaces = [pygame.image.load('resources/pics/Question1.jpg'),pygame.image.load('resources/pics/Question2.png')]
        for i in range(len(self.surfaces)):
            self.surfaces[i] = pygame.transform.scale(self.surfaces[i], (width, self.height))
        self.rect = self.surfaces[0].get_rect()
        self.rect.top = self.height
        self.screen = screen
        self.destination = [[38, 66, 52], [571, 544, 559]] #二维列表，每个问题的三个选项的返回值（要跳转到的行数）

    def display_question(self, i):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if int(self.width * 80 / 960) <= event.pos[0] <= int(self.width * 880 / 960):
                        if int(self.height + self.height * 75 / 640) <= event.pos[1] <= int(self.height + self.height * 195 / 640):
                            self.sound.play()
                            return self.destination[i][0]
                        elif int(self.height + self.height * 245 / 640) <= event.pos[1] <= int(self.height + self.height * 365 / 640):
                            self.sound.play()
                            return self.destination[i][1]
                        elif int(self.height + self.height * 415 / 640) <= event.pos[1] <= int(self.height + self.height * 535 / 640):
                            self.sound.play()
                            return self.destination[i][2]

            self.screen.blit(self.surfaces[i], self.rect)
            pygame.display.update()




