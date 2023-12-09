import pygame

import gameobject
import image
import time_game
import scene_manager

class Snake:
    def __init__(self, grid, limit, pos):
        self.grid = grid
        self.limit = limit

        self.color = (240,70,61)
        self.speed = 0.28
        self.initial_pos = pos

        self.real_pos = self.grid.ret_coord_grid(pos)
        self.snake_body = pygame.sprite.Group()

        self.surface = image.get_surface([46,46])
        self.surface.fill(self.color)
        head = gameobject.GameObject(self.surface)
        head.move(self.real_pos)

        self.snake_body.add(head)
        self.head = self.snake_body.sprites()[0]
    
        # first value is time in milliseconds, the second value is the coord
        self.direction = [-1,0]
        self.last_direction = [-1,0]

        self.sprite_to_add = []
        self.collided_itself = False

    def restart(self):
        self.snake_body.empty()

        self.real_pos = self.grid.ret_coord_grid(self.initial_pos)

        self.surface = image.get_surface([46,46])
        self.surface.fill(self.color)
        self.head = gameobject.GameObject(self.surface)
        self.head.change_position(self.real_pos)
        self.snake_body.add(self.head)

        # first value is time in milliseconds, the second value is the coord
        self.direction = [-1,0]
        self.last_direction = [0,0]

    def increment_body(self,times=1):
        sprites = gameobject.GameObject(self.surface)
        pos = self.snake_body.sprites()[-1].rect[0:2]
        sprites.change_position(pos)

        for i in range(times):
            self.sprite_to_add.append(sprites)

    def change_position(self, pos):
        for i in self.snake_body.sprites():
            i.change_position(pos)

        self.real_pos = self.snake_body.sprites()[0].rect[0:2]

    def change_direction(self, direction):
        self.last_direction = self.direction
        self.direction = direction

    def is_colliding(self, rect):
        if(self.real_pos[0]+10>rect.width or (self.real_pos[0]-10<0 and not self.limit.collidepoint(self.real_pos)) or
           self.real_pos[1]+10>rect.height or (self.real_pos[1]-10<0 and not self.limit.collidepoint(self.real_pos))):
            return True
        return False

    def check_colliding_itself(self):
        for i in range(len(self.snake_body.sprites())-1):
            i+=1
            
            if(self.is_colliding(self.snake_body.sprites()[i].rect)):
                self.collided_itself = True

    def update(self):
        if(self.sprite_to_add):
            for i in self.sprite_to_add:
                self.snake_body.add(i)
                del i
            self.sprite_to_add = []

        #adding an offset time when changing direction
        if((self.direction[0] == -self.last_direction[0] and self.direction[1] == -self.last_direction[1])):
            self.direction = self.last_direction

        if(not self.is_colliding(self.limit) and not self.collided_itself):
            self.move()
        else:
            scene_manager.SceneManager().curr_scene.it_died()

    def draw(self,window,offset=[0,0]):
        for i in self.snake_body.sprites():
            #the +2 its because the snake touches the topleft since its size is 46 instead of 50 (for aesthetic purposes)
            window.blit(i.image,(i.rect[0]+offset[0]+2,i.rect[1]+offset[1]+2))

    def move(self):
        last_pos = self.head.rect[0:2]
        self.real_pos = [self.real_pos[0]+round(self.speed*self.direction[0]*time_game.Time().dt),
                         self.real_pos[1]+round(self.speed*self.direction[1]*time_game.Time().dt)]

        self.head.change_position(self.grid.ret_coord_grid(self.real_pos))
        
        if(self.head.rect[0:2]!= last_pos):
            for i in range(len(self.snake_body.sprites())-1):
                i+=1
                
                actual_pos = self.snake_body.sprites()[i].rect[0:2]
                
                #check collision (i know this doesnt make sense but is the only way it works rn)
                if(self.head.rect[0:2]==actual_pos):
                    self.collided_itself = True

                self.snake_body.sprites()[i].change_position(last_pos)
                last_pos = actual_pos[:]