import pygame

import gameobject
import image
import event_handler

class Pause:
    def __init__(self, scene):
        self.scene = scene

        img_def = image.Image("Resources/pause.png")
        img_def().convert_alpha()
        self.sprite_default = gameobject.GameObject(img_def)
        self.sprite_default.scale([self.sprite_default.image.get_size()[0]*10,self.sprite_default.image.get_size()[1]*10])
        self.sprite_default.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_default.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_default.image.get_size()[1]/2])

        img_play = image.Image("Resources/pause1.png")
        img_play().convert_alpha()
        self.sprite_play = gameobject.GameObject(img_play)
        self.rect_play = pygame.Rect(10,140,450,130)
        self.sprite_play.scale([self.sprite_play.image.get_size()[0]*10,self.sprite_play.image.get_size()[1]*10])
        self.sprite_play.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_play.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_play.image.get_size()[1]/2])
        self.rect_play.move_ip(self.sprite_play.rect[0:2])

        img_restart = image.Image("Resources/pause2.png")
        img_restart().convert_alpha()
        self.sprite_restart = gameobject.GameObject(img_restart)
        self.rect_restart = pygame.Rect(10,280,450,130)
        self.sprite_restart.scale([self.sprite_restart.image.get_size()[0]*10,self.sprite_restart.image.get_size()[1]*10])
        self.sprite_restart.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_restart.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_restart.image.get_size()[1]/2])
        self.rect_restart.move_ip(self.sprite_restart.rect[0:2])

        img_exit = image.Image("Resources/pause3.png")
        img_exit().convert_alpha()
        self.sprite_exit = gameobject.GameObject(img_exit)
        self.rect_exit = pygame.Rect(10,420,450,130)
        self.sprite_exit.scale([self.sprite_exit.image.get_size()[0]*10,self.sprite_exit.image.get_size()[1]*10])
        self.sprite_exit.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_exit.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_exit.image.get_size()[1]/2])
        self.rect_exit.move_ip(self.sprite_exit.rect[0:2])

        self.mode = 0
        
        self.debug = False

    def resize(self):
        self.sprite_default.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_default.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_default.image.get_size()[1]/2])

        self.sprite_play.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_play.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_play.image.get_size()[1]/2])
        self.rect_play.x += self.sprite_play.rect[0] - self.rect_play.x + 10
        self.rect_play.y += self.sprite_play.rect[1] - self.rect_play.y + 140

        self.sprite_restart.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_restart.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_restart.image.get_size()[1]/2])
        self.rect_restart.x += self.sprite_restart.rect[0] - self.rect_restart.x + 10
        self.rect_restart.y += self.sprite_restart.rect[1] - self.rect_restart.y + 280

        self.sprite_exit.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_exit.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_exit.image.get_size()[1]/2])
        self.rect_exit.x += self.sprite_exit.rect[0] - self.rect_exit.x + 10
        self.rect_exit.y += self.sprite_exit.rect[1] - self.rect_exit.y + 420

    def update(self):
        if(key := event_handler.EventHandler().check_events("Mouse button down")):
            if(self.mode == 1):
                self.scene.is_paused = False
            elif(self.mode == 2):
                self.scene.restart()
                self.scene.is_paused = False
            elif(self.mode == 3):
                self.scene.exit()

        if(key := event_handler.EventHandler().check_events("Mouse motion")):
            if(self.rect_play.collidepoint(key.pos)):
                self.mode = 1
            elif(self.rect_restart.collidepoint(key.pos)):
                self.mode = 2
            elif(self.rect_exit.collidepoint(key.pos)):
                self.mode = 3
            else:
                self.mode = 0

    def draw(self, window):
        if(self.mode == 0):
            window.blit(self.sprite_default.image,self.sprite_default.rect[0:2])
        elif(self.mode == 1):
            window.blit(self.sprite_play.image,self.sprite_play.rect[0:2])
        elif(self.mode == 2):
            window.blit(self.sprite_restart.image,self.sprite_restart.rect[0:2])
        elif(self.mode == 3):
            window.blit(self.sprite_exit.image,self.sprite_exit.rect[0:2])
        
        if(self.debug):
            pygame.draw.rect(window,(255,0,0),self.rect_play)
            pygame.draw.rect(window,(255,0,0),self.rect_restart)
            pygame.draw.rect(window,(255,0,0),self.rect_exit)