import pygame

def get_text_font_size(font_name, text, size) -> list[int,int]:
    font = Font(font_name,text,[0,0],size)
    return font.surface.get_size()

class Font:
    def __init__(self, font_name: str, text: str, pos: list[int,int], size: int, is_centered = False):
        self.size = size
        self.color = (255,255,255)
        self.text = text

        self.is_bold = False
        self.is_centered = is_centered

        self.font_name = font_name
        self.font = pygame.font.Font(self.font_name, self.size)
        self.font.set_bold(self.is_bold)
        self.surface = self.font.render(text,True,self.color)

        if(self.is_centered):
            self.rect = self.surface.get_rect(center=pos)
        else:
            self.rect = self.surface.get_rect(center=[-self.surface.get_size()[0]/2,-self.surface.get_size()[1]/2])
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

    def rotate(self,angle):
        self.surface = pygame.transform.rotate(self.surface,angle) 
        self.rect = self.surface.get_rect(center=self.rect[0:2])

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