import pygame

import sprite
import image

class GameObject(sprite.Sprite):
    def __init__(self, image):
        super().__init__(image)

    def update(self):
        pass

    def on_collision(self, obj):
        pass