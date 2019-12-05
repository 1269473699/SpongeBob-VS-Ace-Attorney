import pygame


class ActionBuilder:

    def __init__(self, action, height):
        self.roles = []
        self.role_rects = []
        strs = []
        if action == "hammer":
            strs = ["resources/pics/Hammer.png",
                    "resources/pics/Hammer.png","resources/pics/Hammer.png",
                    "resources/pics/Hammer1.png", "resources/pics/Hammer2.png"]
            self.action_sound = pygame.mixer.Sound("resources/sounds/Hammer.ogg")

        for i in range(len(strs)):
            self.roles.append(pygame.image.load(strs[i]).convert_alpha())
            self.roles[i] = pygame.transform.scale(self.roles[i], (int(height * 0.5 * 1.5), int(height * 0.5)))
            self.role_rects.append(self.roles[i].get_rect())
            self.role_rects[i].top = 0
            self.role_rects[i].left = 0

    def get_actions(self):
        return self.roles, self.role_rects, self.action_sound


