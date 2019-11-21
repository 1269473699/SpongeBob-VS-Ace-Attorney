import pygame


class Background:
    def __init__(self, width, height, path1, path2, screen):
        self.screen = screen
        self.background_upper = pygame.image.load(path1)
        self.background_lower = pygame.image.load(path2)
        self.background_upper = pygame.transform.scale(self.background_upper, (width, int(0.5 * height)))
        self.background_lower = pygame.transform.scale(self.background_lower, (width, int(0.5 * height)))
        self.background_upper_rect = self.background_upper.get_rect()
        self.background_lower_rect = self.background_lower.get_rect()
        self.background_lower_rect.top = int(0.5 * height)

    def display_background(self):
        self.screen.blit(self.background_upper, self.background_upper_rect)
        self.screen.blit(self.background_lower, self.background_lower_rect)
