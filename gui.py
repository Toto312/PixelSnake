import pygame

class Button:
    def __init__(self, position, size):
        self.rect = pygame.Rect(position[0],position[1],size[0],size[1])

    def move(self, position):
        self.rect.move_ip(position)

    def change_position(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]

    def is_colliding(self, position):
        return self.rect.collidepoint(position)