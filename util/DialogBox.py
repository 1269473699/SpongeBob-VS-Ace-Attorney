import linecache
import pygame
import pygame.freetype


class DialogBox:
    def __init__(self, screen, width, height, top, left):
        self.top = top
        self.left = left
        self.height = height
        self.width = width
        self.screen = screen
        #self.rect = self.surface.get_rect()
        self.fps = 30
        self.fClock = pygame.time.Clock()
        self.f = pygame.freetype.Font('resources/fonts/msyh.ttc', 36)

    '''def print_text(self, path , line_no):
        text = linecache.getline(path, line_no)
        texts = text.split("$")
        role = texts[0]
        dialogue  = texts[1]'''

    def test(self):
        self.surface = pygame.draw.rect(self.screen, (255, 255, 255), (self.left, self.top, self.width, self.height))
        f1rect = self.f.render_to(self.screen, ((self.left+10), self.top+10), "海绵宝宝", fgcolor=(0, 0, 0), size=int(self.height*0.25))
        while True:
            pygame.display.update()
            self.fClock.tick(self.fps)





