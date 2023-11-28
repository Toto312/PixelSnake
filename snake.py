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

        self.surface = image.Image([45,45])
        self.surface().fill(self.color)
        head = gameobject.GameObject(self.surface)
        head.move(self.real_pos)

        self.snake_body.add(head)
        self.head = self.snake_body.sprites()[0]
    
        self.direction = (-1,0)
        self.last_direction = [0,0]

        self.sprite_to_add = None

    def increment_body(self):
        sprites = gameobject.GameObject(self.surface)
        pos = self.snake_body.sprites()[-1].rect[0:2]
        sprites.change_position(pos)

        self.sprite_to_add = sprites

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

        if(self.sprite_to_add and not pygame.sprite.spritecollideany(self.sprite_to_add,self.snake_body)):
            print(pygame.sprite.spritecollideany(self.sprite_to_add,self.snake_body))
            self.snake_body.add(self.sprite_to_add)
            self.scene.add_object(self.sprite_to_add)
            self.sprite_to_add = None

    def move(self):
        last_pos = self.head.rect[0:2]
        self.real_pos = [self.real_pos[0]+round(self.speed*self.direction[0]*time_game.Time().dt),self.real_pos[1]+round(self.speed*self.direction[1]*time_game.Time().dt)]

        self.head.change_position(self.scene.grid.ret_coord_grid(self.real_pos))
        
        if(self.head.rect[0:2]!= last_pos):
            for i in range(len(self.snake_body.sprites())-1):
                i+=1

                actual_pos = self.snake_body.sprites()[i].rect[0:2]
                self.snake_body.sprites()[i].change_position(last_pos)
                last_pos = actual_pos[:]