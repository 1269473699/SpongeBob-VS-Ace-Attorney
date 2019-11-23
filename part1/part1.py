import pygame
from util.DialogBox import DialogBox
from util.Background import Background

class Part1_printer:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.dialog = DialogBox(screen, width, height)
        self.fps = 30
        self.fClock = pygame.time.Clock()
        self.back_g = Background(width, height,
                                 'resources/pics/UnderTheTitle.jpg',
                                 'resources/pics/Desk.jpg', self.screen)

    def display_part1(self):
        while True:
            self.screen.fill((255,255,255))
            self.back_g.display_background()
            self.dialog.print_text('resources/texts/Part1.txt', 1)
            self.fClock.tick(self.fps)
            pygame.display.update()