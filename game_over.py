import pygame
import math

import gameobject
        
class GameOver:
    def __init__(self):
        #init time
        self.current_time = pygame.time.get_ticks()
        self.open_time = 5000**2
        
        self.sprite = gameobject.GameObject("Resources/game_over.png")
        self.sprite.scale([500,500])
        self.sprite.move([pygame.display.get_surface().get_size()[0]*0.5-self.sprite.image.get_size()[0]/2-self.sprite.rect[0],
                          pygame.display.get_surface().get_size()[1]*0.5-self.sprite.image.get_size()[1]/2-self.sprite.rect[1]])
        self.sprite.image.set_alpha(0)

    def center(self):
        self.sprite.change_position([pygame.display.get_surface().get_size()[0]*0.5-self.sprite.image.get_size()[0]/2-self.sprite.rect[0],
                                     pygame.display.get_surface().get_size()[1]*0.5-self.sprite.image.get_size()[1]/2-self.sprite.rect[1]])

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
        
        self.sprite = gameobject.GameObject("Resources/press_enter.png")
        self.sprite.scale([500,500])
        self.sprite.change_position([pygame.display.get_surface().get_size()[0]*0.5-self.sprite.image.get_size()[0]/2-self.sprite.rect[0]*0.5,
                                     pygame.display.get_surface().get_size()[1]*0.5-self.sprite.image.get_size()[1]/2-self.sprite.rect[1]])
        self.sprite.image.set_alpha(0)

        self.is_active = False

    def center(self):
        self.sprite.change_position([pygame.display.get_surface().get_size()[0]*0.5-self.sprite.image.get_size()[0]/2-self.sprite.rect[0],
                                     pygame.display.get_surface().get_size()[1]*0.5-self.sprite.image.get_size()[1]/2-self.sprite.rect[1]])

    def restart(self):
        self.open_time = pygame.time.get_ticks()+1000

    def update(self,dt):
        if(self.is_active):
            self.current_time=pygame.time.get_ticks()
            pos = (self.current_time//self.periodic_time)/self.periodic_time
            curr_time = (1/2*math.cos(2*pos*math.pi)+1/2)
            self.sprite.image.set_alpha(round(255*curr_time))

    def draw(self,screen):
        screen.blit(self.sprite.image,self.sprite.rect[0:2])