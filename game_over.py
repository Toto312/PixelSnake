import pygame
import math

import image
import gameobject
        
class GameOver:
    def __init__(self):
        #init time
        self.current_time = pygame.time.get_ticks()
        self.open_time = 5000**2
        
        img = image.Image("game_over.png")
        img().convert_alpha()
        self.sprite = gameobject.GameObject(img)
        self.sprite.scale([500,500])
        self.sprite.move([400-(self.sprite.image.get_size()[0]/2+self.sprite.rect[0]),400-(self.sprite.image.get_size()[1]/2+self.sprite.rect[1])])
        self.sprite.image.set_alpha(0)

    def restart(self):
        self.open_time = pygame.time.get_ticks()+500**2

    def update(self,dt):
        if(self.current_time+pygame.time.get_ticks()<self.open_time):
            self.current_time+=pygame.time.get_ticks()
            curr_loc = (self.current_time/self.open_time)
            self.sprite.image.set_alpha(round(255*curr_loc))

    def draw(self,screen):
        screen.blit(self.sprite.image,self.sprite.rect[0:2])

class PressEnter:
    def __init__(self):
        #init time
        self.current_time = pygame.time.get_ticks()
        self.periodic_time = 50
        
        img = image.Image("press_enter.png")
        img().convert_alpha()
        self.sprite = gameobject.GameObject(img)
        self.sprite.scale([500,500])
        self.sprite.move([400-(self.sprite.image.get_size()[0]/2+self.sprite.rect[0]),400-(self.sprite.image.get_size()[1]/2+self.sprite.rect[1])])
        self.sprite.image.set_alpha(0)

        self.is_active = False

    def restart(self):
        self.open_time = pygame.time.get_ticks()+1000

    def update(self,dt):
        if(self.is_active):
            self.current_time=pygame.time.get_ticks()
            pos = (self.current_time//self.periodic_time)/self.periodic_time
            curr_time = (1/2*math.cos(2*pos*math.pi)+1/2)
            print(curr_time)
            self.sprite.image.set_alpha(round(255*curr_time))

    def draw(self,screen):
        screen.blit(self.sprite.image,self.sprite.rect[0:2])