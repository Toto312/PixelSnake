import pygame

import sprite

class Scene:
    def __init__(self):
        self.is_active = False

        self.objects = pygame.sprite.Group()
        
    def add_object(self, obj):
        if(isinstance(obj,sprite.Sprite)):
            self.objects.add(obj)

    def draw(self, window):
        self.objects.draw(window)

    def update(self):
        for obj in self.objects:
            obj.update()