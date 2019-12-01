import pygame


class Evidence:
    def __init__(self, path, title, height, width, screen):
        self.surface = pygame.image.load(path).convert_alpha()
        self.surface = pygame.transform.scale(self.surface,
                                              (int(height * 0.5 * 15 * 1.2 / 19), int(height * 0.5 * 15 / 19)))
        self.title = title
        self.rect = self.surface.get_rect()
        self.rect.top = int(0.5 * height)
        self.rect.left = int(0.5 * width - 0.5 * self.rect.width)
        self.screen = screen

    def display_evidence(self):
        self.screen.blit(self.surface, self.rect)


