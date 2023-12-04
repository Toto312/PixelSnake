import pygame

import sprite

class Scene:
    def __init__(self, name: str):
        self.is_active = True
        self.name = name

        self.objects = pygame.sprite.Group()
        
    def resize(self, size):
        pass

    def add_object(self, obj):
        if(isinstance(obj,sprite.Sprite)):
            self.objects.add(obj)
        elif(type(obj) == list and all(isinstance(o,sprite.Sprite) for o in obj)):
            for i in obj:
                self.objects.add(i)

    def draw(self, window):
        self.objects.draw(window)

    def update(self):
        if(self.is_active):
            for obj in self.objects:
                obj.update()