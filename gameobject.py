import pygame

import sprite
import image

class GameObject(sprite.Sprite):
    def __init__(self, image: image.Image):
        super().__init__(image)

    def update(self):
        pass