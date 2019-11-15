import pygame


class Button:
    i = 0
    sound_control = 0
    def __init__(self, width, height, screen, surfaces, top, left, hovered_sound, clicked_sound):  # surfaces是surface列表,i=0表示不按键，i=1表示悬浮，i=2表示点击
        self.surfaces = surfaces
        self.screen = screen
        for i in range(len(surfaces)):
            self.surfaces[i] = pygame.transform.scale(self.surfaces[i], (width, height))
        self.button_rect = self.surfaces[0].get_rect()
        self.button_rect.top = top
        self.button_rect.left = left
        self.hovered_sound = hovered_sound
        self.clicked_sound = clicked_sound

    def display_button(self):
        self.screen.blit(self.surfaces[self.i], self.button_rect)

    def respond_to_clicking(self, event):
        if event.pos[0] > self.button_rect.left and event.pos[0] < self.button_rect.left + self.button_rect.width and event.pos[1] > self.button_rect.top and event.pos[1] < self.button_rect.top + self.button_rect.height:
            self.i = 2
            self.clicked_sound.play()
            return True
        return False

    def respond_to_hovering(self, event):
        if event.buttons[0] == 0:
            if event.pos[0] > self.button_rect.left and event.pos[0] < self.button_rect.left + self.button_rect.width and event.pos[1] > self.button_rect.top and event.pos[1] < self.button_rect.top + self.button_rect.height:
                self.i = 1
                if self.sound_control == 0:
                    self.hovered_sound.play()
                self.sound_control = 1

            else:
                self.i = 0
                self.sound_control = 0

