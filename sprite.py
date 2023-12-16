import pygame

import image

class Sprite(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        
        self.image_filename = img

        self.image = image.get_surface(img)
        self.rect = self.image.get_rect()

    def scale(self, size: list[int,int]):
        self.image = pygame.transform.scale(self.image,size)
        
        # make the position of the sprite the same as before scaling
        last_rect = self.rect
        self.rect = self.image.get_rect()
        self.change_position(last_rect[0:2])

    def change_position(self, position: list[int,int]):
        self.rect.x = position[0]
        self.rect.y = position[1]

    def move(self, position: list[int,int]):
        self.rect.x += position[0]
        self.rect.y += position[1]