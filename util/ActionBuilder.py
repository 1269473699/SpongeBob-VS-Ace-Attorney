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

        elif action == "testimony":
            strs = ["resources/pics/Testimony1.png",
                    "resources/pics/Testimony2.png","resources/pics/Testimony3.png",
                    "resources/pics/Testimony4.png", "resources/pics/Testimony5.png",
                    "resources/pics/Testimony6.png",
                    "resources/pics/Testimony6.png","resources/pics/Testimony6.png"]
            self.action_sound = pygame.mixer.Sound("resources/sounds/Testimony.ogg")
            for i in range(len(strs)):
                self.roles.append(pygame.image.load(strs[i]).convert_alpha())
                self.roles[i] = pygame.transform.scale(self.roles[i], (int(0.825*height*0.5), int(0.182812*0.5*height)))
                self.role_rects.append(self.roles[i].get_rect())
                self.role_rects[i].top = int(0.125*height)
                self.role_rects[i].left = int(0.15*height)

        elif action == "cross":
            strs = ["resources/pics/cross1.png",
                    "resources/pics/cross2.png","resources/pics/cross3.png",
                    "resources/pics/cross4.png", "resources/pics/cross5.png",
                    "resources/pics/cross6.png",
                    "resources/pics/cross6.png","resources/pics/cross6.png"]
            self.action_sound = pygame.mixer.Sound("resources/sounds/Testimony.ogg")
            for i in range(len(strs)):
                self.roles.append(pygame.image.load(strs[i]).convert_alpha())
                self.roles[i] = pygame.transform.scale(self.roles[i], (int(0.825*height*0.5), int(0.182812*0.5*height)))
                self.role_rects.append(self.roles[i].get_rect())
                self.role_rects[i].top = int(0.125*height)
                self.role_rects[i].left = int(0.15*height)

        elif action == "PhoenixObjection":
            strs = ["resources/pics/Objection.png"]
            self.action_sound = pygame.mixer.Sound("resources/sounds/PhoenixObjection.ogg")
            for i in range(len(strs)):
                self.roles.append(pygame.image.load(strs[i]).convert_alpha())
                self.roles[i] = pygame.transform.scale(self.roles[i], (int(height * 0.25 * 1.5), int(height * 0.25)))
                self.role_rects.append(self.roles[i].get_rect())
                self.role_rects[i].top = 0
                self.role_rects[i].left = 0

        elif action == "EdgeworthObjection":
            strs = ["resources/pics/Objection.png"]
            self.action_sound = pygame.mixer.Sound("resources/sounds/EdgeworthObjection.ogg")
            for i in range(len(strs)):
                self.roles.append(pygame.image.load(strs[i]).convert_alpha())
                self.roles[i] = pygame.transform.scale(self.roles[i], (int(height * 0.25 * 1.5), int(height * 0.25)))
                self.role_rects.append(self.roles[i].get_rect())
                self.role_rects[i].top = 0
                self.role_rects[i].left = int(height*0.5-height * 0.25 * 1.5)

        elif action == "PhoenixDeter":
            strs = ["resources/pics/Deter.png"]
            self.action_sound = pygame.mixer.Sound("resources/sounds/PhoenixHoldIt.ogg")
            for i in range(len(strs)):
                self.roles.append(pygame.image.load(strs[i]).convert_alpha())
                self.roles[i] = pygame.transform.scale(self.roles[i], (int(height * 0.25 * 1.5), int(height * 0.25)))
                self.role_rects.append(self.roles[i].get_rect())
                self.role_rects[i].top = 0
                self.role_rects[i].left = 0

    def get_actions(self):
        return self.roles, self.role_rects, self.action_sound




