import pygame

import utils
import image

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image: image.Image):
        super().__init__()

        self.image = image()
        self.rect = self.image.get_rect(center=[round(self.image.get_size()[0]/2),round(self.image.get_size()[1]/2)])
    
    def scale(self, size: list[int,int]):
        self.image = pygame.transform.scale(self.image,size)
        
        # make the position of the sprite the same as before scaling
        last_rect = self.rect
        self.rect = self.image.get_rect(center=[0,0])
        self.change_position(last_rect[0:2])

    def change_position(self, position: list[int,int]):
        self.rect.x = position[0]
        self.rect.y = position[1]

    def move(self, position: list[int,int]):
        self.rect.x += position[0]
        self.rect.y += position[1]