import pygame
class Font:
    def __init__(self, font_name: str, text: str, pos: list[int,int], size: int):
        self.size = size
        self.color = (255,255,255)
        self.text = text

        self.is_bold = False
        self.is_centered = True

        self.font_name = font_name
        self.font = pygame.font.Font(self.font_name, self.size)
        self.font.set_bold(self.is_bold)
        self.surface = self.font.render(text,True,self.color)

        if(self.is_centered):
            self.rect = self.surface.get_rect(center=pos)
        else:
            self.rect = self.surface.get_rect()
            self.move(pos)

    def change_position(self,pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def move(self,pos):
        self.rect.x += pos[0]
        self.rect.y += pos[1]

    def scale(self,value,relative=True):
        if(relative):
            self.surface = pygame.transform.scale_by(self.surface, value)
        else:
            self.surface = pygame.transform.scale(self.surface, value)
        self.rect = self.surface.get_rect()

    def change_color(self,color):
        self.color = color
        self.surface = self.font.render(self.text,True,self.color)
        if(self.is_centered):
            self.rect = self.surface.get_rect(center=self.rect[0:2])
        else:
            self.rect = self.surface.get_rect()
        self.font = pygame.font.Font(self.font_name, self.size)

    def change_text(self,text):
        self.text = text
        self.surface = self.font.render(self.text,True,self.color)

    def draw(self,window):
        window.blit(self.surface,self.rect)