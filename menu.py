import pygame

import gameobject
import image
import event_handler

class Menu:
    def __init__(self):
        img_def = image.Image("men.png")
        img_def().convert_alpha()
        self.sprite_default = gameobject.GameObject(img_def)
        self.sprite_default.scale([600,600])
        self.sprite_default.change_position([100,100])

        img_play = image.Image("men1.png")
        img_play().convert_alpha()
        self.sprite_play = gameobject.GameObject(img_play)
        self.sprite_play.scale([600,600])
        self.sprite_play.change_position([100,100])

        img_restart = image.Image("men2.png")
        img_restart().convert_alpha()
        self.sprite_restart = gameobject.GameObject(img_restart)
        self.sprite_restart.scale([600,600])
        self.sprite_restart.change_position([100,100])

        img_exit = image.Image("men3.png")
        img_exit().convert_alpha()
        self.sprite_exit = gameobject.GameObject(img_exit)
        self.sprite_exit.scale([600,600])
        self.sprite_exit.change_position([100,100])

        self.rect_play = pygame.Rect(194,269,410,119)
        self.rect_restart = pygame.Rect(194,400,394,119)
        self.rect_exit = pygame.Rect(194,531,410,119)

        self.mode = 0
    def update(self):
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
        #pygame.draw.rect()
        if(self.mode == 0):
            window.blit(self.sprite_default.image,self.sprite_default.rect[0:2])
        elif(self.mode == 1):
            window.blit(self.sprite_play.image,self.sprite_play.rect[0:2])
        elif(self.mode == 2):
            window.blit(self.sprite_restart.image,self.sprite_restart.rect[0:2])
        elif(self.mode == 3):
            window.blit(self.sprite_exit.image,self.sprite_exit.rect[0:2])




