import pygame


class RoleBuilder:

    def __init__(self, role, height):
        self.roles = []
        self.role_rects = []
        strs = []
        if role == "MayaStand":
            strs = ["resources/pics/MayaStand1.gif", "resources/pics/MayaStand2.gif", "resources/pics/MayaStand3.gif"]
        if role =="MayaLower":
            strs = ["resources/pics/MayaLower1.gif", "resources/pics/MayaLower2.gif", "resources/pics/MayaLower3.gif"]
        for i in range(len(strs)):
            self.roles.append(pygame.image.load(strs[i]).convert_alpha())
            self.roles[i] = pygame.transform.scale(self.roles[i], (int(height * 0.5 * 1.5), int(height * 0.5)))
            self.role_rects.append(self.roles[i].get_rect())
            self.role_rects[i].top = 0
            self.role_rects[i].left = 0

    def get_roles(self):
        return self.roles, self.role_rects


