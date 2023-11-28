import pygame

import gameobject
import image
import time_game

class Snake:
    def __init__(self):
        self.snake_body = pygame.sprite.Group()

        self.color = (240,70,61)

        head_image = image.Image([50,50])
        head_image().fill(self.color)
        head = gameobject.GameObject(head_image)
        head.move([500,500])

        self.snake_body.add(head)
        self.head = self.snake_body.sprites()[0]
    
        self.direction = (-1,0)
        self.last_direction = [0,0]

    def change_direction(self,direction):
        self.last_direction = self.direction
        self.direction = direction

    def update(self):
        if(self.direction[0] != -self.last_direction[0] and self.direction[1] != -self.last_direction[1]):
            self.direction = self.last_direction

        self.move()

    def move(self):
        self.head.move([0.5*self.direction[0]*time_game.Time().dt,0.5*self.direction[1]*time_game.Time().dt])