import pygame

import gameobject
import image
import time_game
import scene_manager
import utils
import direction
import sprite
import debug

class Snake:
    def __init__(self, grid, limit, pos, is_playing=True):
        self.grid = grid
        self.limit = limit

        self.is_playing = is_playing

        self.color = (240,70,61)
        self.speed = 0.20
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
        self.direction = direction.Direction([-1,0],pygame.time.get_ticks())
        self.last_direction = utils.Queue(2)
        self.last_direction.add(direction.Direction([-1,0],1000))

        self.sprite_to_add = []
        self.collided_itself = False

        self.pos = sprite.Sprite([20,20])
        self.pos.image.fill((0,255,0))
        self.pos.change_position(self.real_pos)

    def restart(self):
        self.snake_body.empty()

        self.real_pos = self.grid.ret_coord_grid(self.initial_pos)

        self.surface = image.get_surface([46,46])
        self.surface.fill(self.color)
        self.head = gameobject.GameObject(self.surface)
        self.head.change_position(self.real_pos)
        self.snake_body.add(self.head)

        # first value is time in milliseconds, the second value is the coord
        self.direction = direction.Direction([-1,0],pygame.time.get_ticks())
        self.last_direction = utils.Queue(2)
        self.last_direction.add(direction.Direction([-1,0],pygame.time.get_ticks()))

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
        
        if(not (dir[0] == -self.direction.direction[0] and dir[1] == -self.direction.direction[1]) and
           pygame.time.get_ticks()-self.last_direction.last().time>8*time_game.Time().dt):
            self.direction = direction.Direction(dir,pygame.time.get_ticks())

    def is_colliding(self, rect):
        if(not self.is_playing):
            if(self.real_pos[0]+20>rect.width or self.real_pos[0]-8<rect.x or
               self.real_pos[1]+20>rect.height or self.real_pos[1]-8<rect.y):
                return True
            return False

        if(self.real_pos[0]>rect.width or self.real_pos[0]<0 or
           self.real_pos[1]>rect.height or self.real_pos[1]<0):
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
        if(self.direction.direction[0] == -self.last_direction.last().direction[0] and
           self.direction.direction[1] == -self.last_direction.last().direction[1]):
            self.direction = self.last_direction.last()

        self.pos.change_position(self.real_pos)

        if(not self.is_colliding(self.limit) and not self.collided_itself):
            self.move()
        else:
            scene_manager.SceneManager().curr_scene.it_died()


    def draw(self,window,offset=[0,0]):
        for i in self.snake_body.sprites():
            #the +2 its because the snake touches the topleft since its size is 46 instead of 50 (for aesthetic purposes)
            window.blit(i.image,(i.rect[0]+offset[0]+4,i.rect[1]+offset[1]+4))
        
        if(debug.DebugInfo().is_active):
            #center sprite
            window.blit(self.pos.image,[self.pos.rect[0]-self.pos.rect[2]/2+offset[0]+4,self.pos.rect[1]-self.pos.rect[3]/2+offset[1]+4])

    def move(self):
        last_pos = self.head.rect[0:2]
        self.real_pos = [self.real_pos[0]+round(self.speed*self.direction.direction[0]*time_game.Time().dt),
                         self.real_pos[1]+round(self.speed*self.direction.direction[1]*time_game.Time().dt)]

        if(not self.is_playing):
            self.head.change_position(self.grid.ret_coord_grid(self.real_pos))
        else:
            self.head.rect[0] = max(min(self.grid.ret_coord_grid(self.real_pos)[0],self.grid.ret_coord_world(self.grid.max)[0]),0)
            self.head.rect[1] = max(min(self.grid.ret_coord_grid(self.real_pos)[1],self.grid.ret_coord_world(self.grid.max)[1]),0)

        if(self.head.rect[0:2]!= last_pos):
            self.real_pos = [self.head.rect[0]+self.head.rect[2]/2,
                             self.head.rect[1]+self.head.rect[3]/2]
            for i in range(len(self.snake_body.sprites())-1):
                i+=1
                
                actual_pos = self.snake_body.sprites()[i].rect[0:2]
                
                #check collision (i know this doesnt make sense but is the only way it works rn)
                if(self.head.rect[0:2]==actual_pos):
                    self.collided_itself = True

                self.snake_body.sprites()[i].change_position(last_pos)
                last_pos = actual_pos[:]