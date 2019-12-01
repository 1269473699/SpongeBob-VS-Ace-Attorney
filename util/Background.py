import pygame

class Background:
    def __init__(self, width, height, path1, path2, screen):
        self.fps = 30
        self.fClock = pygame.time.Clock()
        self.screen = screen
        self.background_upper = pygame.image.load(path1).convert()
        self.background_lower = pygame.image.load(path2)
        self.background_upper = pygame.transform.scale(self.background_upper, (width, int(0.5 * height)))
        self.background_lower = pygame.transform.scale(self.background_lower, (width, int(0.5 * height)))
        self.background_upper_rect = self.background_upper.get_rect()
        self.background_lower_rect = self.background_lower.get_rect()
        self.background_lower_rect.top = int(0.5 * height)

    def display_background(self, i):
        if i == 0:
            self.screen.blit(self.background_upper, self.background_upper_rect)
            self.screen.blit(self.background_lower, self.background_lower_rect)
        elif i == 1:
            self.screen.blit(self.background_lower, self.background_lower_rect)
        else:
            self.screen.blit(self.background_upper, self.background_upper_rect)

    def fade_in(self):
        for i in range(0, 256, 6):
            self.background_upper.set_alpha(i)
            self.screen.blit(self.background_upper, self.background_upper_rect)
            pygame.display.update()
            self.fClock.tick(self.fps)

