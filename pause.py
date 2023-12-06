import pygame

import gameobject
import image
import event_handler
import scene_manager

class Pause:
    def __init__(self, scene):
        self.scene = scene

        self.images = ["Resources/pause.png","Resources/pause1.png","Resources/pause2.png","Resources/pause3.png"]

        self.button_music = {"on" : "Resources/music_on.png", "off" : "Resources/music_off.png"}

        self.sprite_default = gameobject.GameObject("Resources/pause.png")
        self.sprite_default.scale([self.sprite_default.image.get_size()[0]*10,self.sprite_default.image.get_size()[1]*10])
        self.sprite_default.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_default.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_default.image.get_size()[1]/2])

        self.sprite_play = gameobject.GameObject("Resources/pause1.png")
        self.rect_play = pygame.Rect(10,140,450,130)
        self.sprite_play.scale([self.sprite_play.image.get_size()[0]*10,self.sprite_play.image.get_size()[1]*10])
        self.sprite_play.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_play.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_play.image.get_size()[1]/2])
        self.rect_play.move_ip(self.sprite_play.rect[0:2])

        self.sprite_restart = gameobject.GameObject("Resources/pause2.png")
        self.rect_restart = pygame.Rect(10,280,450,130)
        self.sprite_restart.scale([self.sprite_restart.image.get_size()[0]*10,self.sprite_restart.image.get_size()[1]*10])
        self.sprite_restart.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_restart.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_restart.image.get_size()[1]/2])
        self.rect_restart.move_ip(self.sprite_restart.rect[0:2])

        self.sprite_exit = gameobject.GameObject("Resources/pause3.png")
        self.rect_exit = pygame.Rect(10,420,450,130)
        self.sprite_exit.scale([self.sprite_exit.image.get_size()[0]*10,self.sprite_exit.image.get_size()[1]*10])
        self.sprite_exit.change_position([self.scene.screen.get_size()[0]*0.5-self.sprite_exit.image.get_size()[0]/2,self.scene.screen.get_size()[1]*0.5-self.sprite_exit.image.get_size()[1]/2])
        self.rect_exit.move_ip(self.sprite_exit.rect[0:2])

        self.sprite_music_on = gameobject.GameObject("Resources/music_on.png")
        self.rect_music_on = pygame.Rect(0,0,34*2,29*2)
        self.sprite_music_on.scale([self.sprite_music_on.image.get_size()[0]*2,self.sprite_music_on.image.get_size()[1]*2])
        self.sprite_music_on.change_position([0,self.scene.screen.get_size()[0]-self.sprite_music_on.image.get_size()[1]])
        self.rect_music_on.move_ip(self.sprite_music_on.rect[0:2])    


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

        self.sprite_music_on.change_position([0,self.scene.screen.get_size()[1]-self.sprite_music_on.image.get_size()[1]])
        self.rect_music_on.x += self.sprite_music_on.rect[0] - self.rect_music_on.x
        self.rect_music_on.y += self.sprite_music_on.rect[1] - self.rect_music_on.y

        self.is_music_on = False

    def update(self):
        if(key := event_handler.EventHandler().check_events("Key down")):
            # F1
            if(key.scancode == 58):
                self.debug = not self.debug

        if(key := event_handler.EventHandler().check_events("Mouse button down")):
            if(self.mode == 1):
                self.scene.is_paused = False
            elif(self.mode == 2):
                self.scene.restart()
                self.scene.is_paused = False
            elif(self.mode == 3):
                self.scene.exit()

            if(self.rect_music_on.collidepoint(key.pos)):
                if(pygame.mixer.music.get_busy()):
                    pygame.mixer.music.pause()
                    img_music_off = image.Image("Resources/music_off.png")
                    self.sprite_music_on.image = img_music_off.image
                    self.sprite_music_on.scale([self.sprite_music_on.image.get_size()[0]*2,self.sprite_music_on.image.get_size()[1]*2])
                else:
                    pygame.mixer.music.unpause()
                    img_music_on = image.Image("Resources/music_on.png")
                    self.sprite_music_on.image = img_music_on.image
                    self.sprite_music_on.scale([self.sprite_music_on.image.get_size()[0]*2,self.sprite_music_on.image.get_size()[1]*2])
            
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
        
        window.blit(self.sprite_music_on.image,self.sprite_music_on.rect[0:2])

        if(self.debug):
            pygame.draw.rect(window,(255,0,0),self.rect_play)
            pygame.draw.rect(window,(255,0,0),self.rect_restart)
            pygame.draw.rect(window,(255,0,0),self.rect_exit)
            pygame.draw.rect(window,(255,0,0),self.rect_music_on)