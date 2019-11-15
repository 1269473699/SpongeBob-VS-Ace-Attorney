import linecache
import pygame
import pygame.freetype


class DialogBox:
    def __init__(self, screen, width, height):
        '''self.top = top
        self.left = left'''
        self.height = height
        self.width = width
        self.screen = screen
        #self.rect = self.surface.get_rect()
        self.fps = 30
        self.fClock = pygame.time.Clock()
        self.f = pygame.freetype.Font('resources/fonts/msyh.ttc', 36)
        self.dialog_sayer = pygame.image.load('resources/pics/DialogBox_sayer.png').convert_alpha()
        self.dialog_sayer = pygame.transform.scale(self.dialog_sayer, (int(width * 0.25), int(0.125 * 0.35 * height)))
        self.dialog_text = pygame.image.load('resources/pics/DialogBox_text.png').convert_alpha()
        self.dialog_text = pygame.transform.scale(self.dialog_text, (width, int(0.125 * height)))
        self.dialog_sayer_rect = self.dialog_sayer.get_rect()
        self.dialog_text_rect = self.dialog_text.get_rect()
        self.dialog_text_rect.top = int(3 * height / 8)
        self.dialog_sayer_rect.top = self.dialog_text_rect.top - self.dialog_sayer_rect.height

    def print_text(self, path , line_no):
        '''text = linecache.getline(path, line_no)
        texts = text.split("$")
        role = texts[0]
        dialogue  = texts[1]'''
        self.screen.blit(self.dialog_text, self.dialog_text_rect)
        self.screen.blit(self.dialog_sayer, self.dialog_sayer_rect)

    '''def test(self):
        self.surface = pygame.draw.rect(self.screen, (255, 255, 255), (self.left, self.top, self.width, self.height))
        f1rect = self.f.render_to(self.screen, ((self.left+10), self.top+10), "海绵宝宝", fgcolor=(0, 0, 0), size=int(self.height*0.25))
        while True:
            pygame.display.update()
            self.fClock.tick(self.fps)'''





