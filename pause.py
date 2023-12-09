import pygame

import sprite
import event_handler
import gui
import scene_manager

class Pause:
    def __init__(self, scene):
        self.scene = scene

        self.initial_position = {"play" : [10,140], "restart" : [10,280], "exit" : [10,420]}
        self.button_size = [450,130]

        # kinda a strange way to make buttons, but i made the pause a single image so ¯\_(ツ)_/¯
        self.buttons = {"default" : [sprite.Sprite("Resources/pause.png"), None],
                       "play" : [sprite.Sprite("Resources/pause1.png"), gui.Button(self.initial_position["play"], self.button_size)],
                       "restart" : [sprite.Sprite("Resources/pause2.png"), gui.Button(self.initial_position["restart"], self.button_size)],
                       "exit" : [sprite.Sprite("Resources/pause3.png"), gui.Button(self.initial_position["exit"], self.button_size)]}

        # init menu buttons
        for name,button in self.buttons.items():
            button[0].scale([button[0].image.get_size()[0]*10,button[0].image.get_size()[1]*10])
            button[0].change_position([self.scene.screen.get_size()[0]*0.5-button[0].image.get_size()[0]/2,
                                   self.scene.screen.get_size()[1]*0.5-button[0].image.get_size()[1]/2])
            if(name != "default"):
                button[1].move(button[0].rect[0:2])

        self.button_music_size = [68,58]
        self.button_music = {"on" : [sprite.Sprite("Resources/music_on.png"), gui.Button([0,0],self.button_music_size)],
                             "off" : [sprite.Sprite("Resources/music_off.png"), gui.Button([0,0],self.button_music_size)]}


        # init music button
        for button in self.button_music.values():
            button[0].scale([button[0].image.get_size()[0]*2,
                             button[0].image.get_size()[1]*2])
            button[0].change_position([0,self.scene.screen.get_size()[0]-button[0].image.get_size()[1]])

            button[1].move(button[0].rect[0:2])

        self.actual_button_selected = None
        self.actual_music_button_selected = "on"

        self.debug = False

    def resize(self):
        for name,button in self.buttons.items():
            button[0].change_position([self.scene.screen.get_size()[0]*0.5 - button[0].image.get_size()[0]/2,
                                       self.scene.screen.get_size()[1]*0.5 - button[0].image.get_size()[1]/2])
            
            # only change the button pos if the sprite isnt the default
            if(name != "default"):
                button[1].move([button[0].rect[0] - button[1].rect[0] + self.initial_position[name][0],
                                button[0].rect[1] - button[1].rect[1] + self.initial_position[name][1]])

        for button in self.button_music.values():
            button[0].change_position([0,self.scene.screen.get_size()[1] - button[0].image.get_size()[1]])
            
            button[1].move([button[0].rect[0] - button[1].rect[0],
                            button[0].rect[1] - button[1].rect[1]])

    def update(self):
        if(key := event_handler.EventHandler().check_events("Key down")):
            # F1
            if(key.scancode == 58):
                self.debug = not self.debug

        if(key := event_handler.EventHandler().check_events("Mouse button down")):
            if(self.actual_button_selected == "play"):
                self.scene.is_menu_opened = False
                self.scene.is_paused = False
            elif(self.actual_button_selected == "restart"):
                self.scene.restart()
                self.scene.is_menu_opened = False
                self.scene.is_paused = True
            elif(self.actual_button_selected == "exit"):
                self.scene.restart()
                self.scene.is_menu_opened = False
                self.scene.is_paused = True
                scene_manager.SceneManager().change_scene("Menu")

            if(self.button_music[self.actual_music_button_selected][1].is_colliding(key.pos)):
                if(self.actual_music_button_selected == "on" and pygame.mixer.music.get_busy()):
                    pygame.mixer.music.pause()
                    self.actual_music_button_selected = "off"

                elif(self.actual_music_button_selected == "off" and not pygame.mixer.music.get_busy()):
                    pygame.mixer.music.unpause()
                    self.actual_music_button_selected = "on"

        if(key := event_handler.EventHandler().check_events("Mouse motion")):
            if(self.buttons["play"][1].is_colliding(key.pos)):
                self.actual_button_selected = "play"

            elif(self.buttons["restart"][1].is_colliding(key.pos)):
                self.actual_button_selected = "restart"

            elif(self.buttons["exit"][1].is_colliding(key.pos)):
                self.actual_button_selected = "exit"

            else:
                self.actual_button_selected = None

    def draw(self, window):
        # if self.actual_button_selected == None, it means that there isnt buttons selected,
        # so it draws the pause without a selected button
        if(self.actual_button_selected == None):
            window.blit(self.buttons["default"][0].image,
                        self.buttons["default"][0].rect[0:2])
        else:
            window.blit(self.buttons[self.actual_button_selected][0].image,
                        self.buttons[self.actual_button_selected][0].rect[0:2])

        # draw button music
        window.blit(self.button_music[self.actual_music_button_selected][0].image,
                    self.button_music[self.actual_music_button_selected][0].rect[0:2])

        if(self.debug):
            for name,i in self.buttons.items():
                if(name != "default"):
                    pygame.draw.rect(window,(255,0,0),i[1].rect)

            pygame.draw.rect(window,(255,0,0),self.button_music[self.actual_music_button_selected][1].rect)