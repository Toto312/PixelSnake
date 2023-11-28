import pygame

import gameobject
import image
import time_game

class Snake:
    def __init__(self, scene):
        self.scene = scene
        self.snake_body = pygame.sprite.Group()

        self.color = (240,70,61)
        self.real_pos = [500,500]
        self.speed = 0.3

        head_image = image.Image([50,50])
        head_image().fill(self.color)
        head = gameobject.GameObject(head_image)
        head.move(self.real_pos)

        self.snake_body.add(head)
        self.head = self.snake_body.sprites()[0]
    
        self.direction = (-1,0)
        self.last_direction = [0,0]

    def change_direction(self,direction):
        self.last_direction = self.direction
        self.direction = direction

    def is_colliding(self):
        if(self.real_pos[0]+self.head.rect[2]+1>=self.scene.limit.width or self.real_pos[0]-1<=0 or
           self.real_pos[0]+self.head.rect[3]+1>=self.scene.limit.height or self.real_pos[1]-1<=0):
            return True

    def update(self):
        if(self.direction[0] == -self.last_direction[0] and self.direction[1] == -self.last_direction[1]):
            self.direction = self.last_direction

        if(not self.is_colliding()):
            self.move()

    def move(self):
        self.real_pos = [self.real_pos[0]+round(self.speed*self.direction[0]*time_game.Time().dt),self.real_pos[1]+round(self.speed*self.direction[1]*time_game.Time().dt)]

        self.head.change_position(self.scene.grid.ret_coord_grid(self.real_pos))