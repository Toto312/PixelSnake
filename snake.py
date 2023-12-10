import pygame

import gameobject
import image
import time_game
import scene_manager
import utils
import direction

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
        self.direction = direction.Direction([-1,0])
        self.last_direction = utils.Queue(2)

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
        self.direction = direction.Direction([-1,0])
        self.last_direction = utils.Queue(2)

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

    def change_direction(self, dir):
        self.last_direction.add(self.direction)
        self.direction = direction.Direction(dir,pygame.time.get_ticks())

    def is_colliding(self, rect):
        if(self.real_pos[0]+10>rect.width or (self.real_pos[0]-10<0 and not self.limit.collidepoint(self.real_pos)) or
           self.real_pos[1]+10>rect.height or (self.real_pos[1]-10<0 and not self.limit.collidepoint(self.real_pos))):
            return True
        return False

    def position_collide_with_group(self,position,exception):
        for i in self.snake_body.sprites():
            if(i==exception):
                continue
            if(self.grid.ret_grid(i.rect[0:2])==self.grid.ret_grid(position)):
                return True
        return False

    def update(self):
        if(self.sprite_to_add):
            for i in self.sprite_to_add:
                self.snake_body.add(i)
                del i
            self.sprite_to_add = []
        
        last_directions = self.last_direction.values

        #adding an offset time when changing direction
        if(len(self.last_direction.values)>=1 and
           self.direction.direction[0] == -self.last_direction.last().direction[0] and
           self.direction.direction[1] == -self.last_direction.last().direction[1]):
            self.direction = self.last_direction.last()

        real_pos = [self.real_pos[0]+round(self.speed*self.direction.direction[0]*time_game.Time().dt),
                    self.real_pos[1]+round(self.speed*self.direction.direction[1]*time_game.Time().dt)]
        
        if(len(self.last_direction.values)==2 and
           self.direction.direction[0] == -self.last_direction.values[0].direction[0] and
           self.direction.direction[1] == -self.last_direction.values[0].direction[1] and
           self.position_collide_with_group(real_pos,self.head) and 
           self.direction.diff_time(self.last_direction.values[0])<100):
            
            self.direction = self.last_direction.last()

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
        self.real_pos = [self.real_pos[0]+round(self.speed*self.direction.direction[0]*time_game.Time().dt),
                         self.real_pos[1]+round(self.speed*self.direction.direction[1]*time_game.Time().dt)]

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