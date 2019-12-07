import pygame


class HealthBuilder:
    def __init__(self, height, width, screen):
        self.hp = 3
        self.screen = screen
        self.surfaces = [pygame.image.load("resources/pics/Health0.png").convert_alpha(),
                         pygame.image.load("resources/pics/Health1.png").convert_alpha(),
                         pygame.image.load("resources/pics/Health2.png").convert_alpha(),
                         pygame.image.load("resources/pics/Health3.png").convert_alpha()]
        for i in range(len(self.surfaces)):
            self.surfaces[i] = pygame.transform.scale(self.surfaces[i], (int(0.15 * width), int(0.05 * width)))
        self.rect = self.surfaces[0].get_rect()
        self.rect.left = int(0.83 * width)
        self.rect.top = int((0.5 + 0.03 * 0.5) * height)

    def display_health(self):
        self.screen.blit(self.surfaces[self.hp], self.rect)

    def damaged(self):
        self.hp = self.hp - 1

    def refresh(self):
        self.hp = 3
