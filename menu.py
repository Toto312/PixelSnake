import pygame
import copy

import gui
import sprite
import event_handler
import scene_manager

class MenuButtons:
    def __init__(self, scene):
        self.scene = scene
        self.screen = pygame.display.get_surface()

        self.play_sprite = sprite.Sprite("Resources/play_button.png")
        self.play_sprite1 = sprite.Sprite("Resources/play_button1.png")
        self.options_sprite = sprite.Sprite("Resources/options_button.png")
        self.options_sprite1 = sprite.Sprite("Resources/options_button1.png")
        self.exit_sprite = sprite.Sprite("Resources/exit_button.png")
        self.exit_sprite1 = sprite.Sprite("Resources/exit_button1.png")

        #-----------------------------------PLAY BUTTON------------------------------------------
        self.play_button = {"off" : [copy.copy(self.play_sprite),gui.Button([0,0],[60,13])],
                            "on" : [copy.copy(self.play_sprite1),gui.Button([0,0],[60,13])]}
        
        for image in self.play_button.values():
            image[0].scale([image[0].image.get_size()[0]*5,
                            image[0].image.get_size()[1]*5])
            image[0].change_position([0,self.screen.get_size()[1]*0.35])

            image[1].rect[2] *= 5
            image[1].rect[3] *= 5
            
            image[1].rect[0] = image[0].rect[0]
            image[1].rect[1] += image[0].rect[1] + 10*5

        self.selected_play_sprite = "off"

        #-----------------------------------OPTIONS BUTTON------------------------------------------
        self.options_button = {"off" : [copy.copy(self.options_sprite),gui.Button([0,0],[60,13])],
                            "on" : [copy.copy(self.options_sprite1),gui.Button([0,0],[60,13])]}
        
        for image in self.options_button.values():
            image[0].scale([image[0].image.get_size()[0]*5,
                            image[0].image.get_size()[1]*5])
            image[0].change_position([0,self.screen.get_size()[1]*0.5])
            
            image[1].rect[2] *= 5
            image[1].rect[3] *= 5
            image[1].rect[0] = image[0].rect[0]
            image[1].rect[1] += image[0].rect[1] + 10*5

        self.selected_options_sprite = "off"

        #-----------------------------------EXIT BUTTON------------------------------------------
        self.exit_button = {"off" : [copy.copy(self.exit_sprite),gui.Button([0,0],[60,13])],
                            "on" : [copy.copy(self.exit_sprite1),gui.Button([0,0],[60,13])]}
        
        for image in self.exit_button.values():
            image[0].scale([image[0].image.get_size()[0]*5,
                            image[0].image.get_size()[1]*5])
            image[0].change_position([0,self.screen.get_size()[1]*0.65])

            image[1].rect[2] *= 5
            image[1].rect[3] *= 5
            image[1].rect[0] = image[0].rect[0]
            image[1].rect[1] += image[0].rect[1] + 10*5

        self.selected_exit_sprite = "off"
        self.debug = False

    def resize(self, size):
        for button in self.play_button.values():
            new_sprite = [copy.copy(self.play_sprite),copy.copy(self.play_sprite1)]
            # this size is when the game is in 700,700
            normal_size = [new_sprite[0].image.get_size()[0]*5,
                           new_sprite[0].image.get_size()[1]*5]
            
            if(size[1]==700):
                now_size_multiplier = [5,5]
            else:
                now_size_multiplier = [5*max(size[0]/700*0.65,1),
                                       5*max(size[1]/700*1.25,1)]

            new_sprite[0].scale([new_sprite[0].image.get_size()[0]*now_size_multiplier[0],
                                 new_sprite[0].image.get_size()[1]*now_size_multiplier[1]])
            new_sprite[1].scale([new_sprite[1].image.get_size()[0]*now_size_multiplier[0],
                                 new_sprite[1].image.get_size()[1]*now_size_multiplier[1]])

            new_sprite[0].change_position([0,self.screen.get_size()[1]*0.35])
            new_sprite[1].change_position([0,self.screen.get_size()[1]*0.35])
            self.play_button["on"][0] = new_sprite[1]
            self.play_button["off"][0] = new_sprite[0]

            self.play_button["off"][1].rect[2] = 60 * now_size_multiplier[0]
            self.play_button["off"][1].rect[3] = 13 * now_size_multiplier[1]
            self.play_button["off"][1].rect[1] = self.play_button["off"][0].rect[1] + 10*now_size_multiplier[1]
            
            self.play_button["on"][1].rect[2] = 60 * now_size_multiplier[0]
            self.play_button["on"][1].rect[3] = 13 * now_size_multiplier[1]
            self.play_button["on"][1].rect[1] = self.play_button["off"][0].rect[1] + 10*now_size_multiplier[1]
            
        for button in self.options_button.values():
            new_sprite = [copy.copy(self.options_sprite),copy.copy(self.options_sprite1)]
            # this size is when the game is in 700,700
            normal_size = [new_sprite[0].image.get_size()[0]*5,
                           new_sprite[0].image.get_size()[1]*5]
            
            if(size[1]==700):
                now_size_multiplier = [5,5]
            else:
                now_size_multiplier = [5*max(size[0]/700*0.65,1),
                                       5*max(size[1]/700*1.25,1)]

            new_sprite[0].scale([new_sprite[0].image.get_size()[0]*now_size_multiplier[0],
                                 new_sprite[0].image.get_size()[1]*now_size_multiplier[1]])
            new_sprite[1].scale([new_sprite[1].image.get_size()[0]*now_size_multiplier[0],
                                 new_sprite[1].image.get_size()[1]*now_size_multiplier[1]])

            new_sprite[0].change_position([0,self.screen.get_size()[1]*0.5])
            new_sprite[1].change_position([0,self.screen.get_size()[1]*0.5])
            self.options_button["on"][0] = new_sprite[1]
            self.options_button["off"][0] = new_sprite[0]

            self.options_button["off"][1].rect[2] = 60 * now_size_multiplier[0]
            self.options_button["off"][1].rect[3] = 13 * now_size_multiplier[1]
            self.options_button["off"][1].rect[1] = self.options_button["off"][0].rect[1] + 10*now_size_multiplier[1]
            
            self.options_button["on"][1].rect[2] = 60 * now_size_multiplier[0]
            self.options_button["on"][1].rect[3] = 13 * now_size_multiplier[1]
            self.options_button["on"][1].rect[1] = self.options_button["off"][0].rect[1] + 10*now_size_multiplier[1]

        for button in self.exit_button.values():
            new_sprite = [copy.copy(self.exit_sprite),copy.copy(self.exit_sprite1)]
            # this size is when the game is in 700,700
            normal_size = [new_sprite[0].image.get_size()[0]*5,
                           new_sprite[0].image.get_size()[1]*5]
            
            if(size[1]==700):
                now_size_multiplier = [5,5]
            else:
                now_size_multiplier = [5*max(size[0]/700*0.65,1),
                                       5*max(size[1]/700*1.25,1)]

            new_sprite[0].scale([new_sprite[0].image.get_size()[0]*now_size_multiplier[0],
                                 new_sprite[0].image.get_size()[1]*now_size_multiplier[1]])
            new_sprite[1].scale([new_sprite[1].image.get_size()[0]*now_size_multiplier[0],
                                 new_sprite[1].image.get_size()[1]*now_size_multiplier[1]])

            new_sprite[0].change_position([0,self.screen.get_size()[1]*0.65])
            new_sprite[1].change_position([0,self.screen.get_size()[1]*0.65])
            self.exit_button["on"][0] = new_sprite[1]
            self.exit_button["off"][0] = new_sprite[0]

            self.exit_button["off"][1].rect[2] = 60 * now_size_multiplier[0]
            self.exit_button["off"][1].rect[3] = 13 * now_size_multiplier[1]
            self.exit_button["off"][1].rect[1] = self.exit_button["off"][0].rect[1] + 10*now_size_multiplier[1]
            
            self.exit_button["on"][1].rect[2] = 60 * now_size_multiplier[0]
            self.exit_button["on"][1].rect[3] = 13 * now_size_multiplier[1]
            self.exit_button["on"][1].rect[1] = self.exit_button["off"][0].rect[1] + 10*now_size_multiplier[1]
            
    def update(self):
        if(key := event_handler.EventHandler().check_events("Key down")):
            # F1
            if(key.scancode == 58):
                self.debug = not self.debug

        if(key := event_handler.EventHandler().check_events("Mouse button down")):
            if(self.selected_play_sprite == "on"):
                scene_manager.SceneManager().change_scene("Game")
            elif(self.selected_options_sprite == "on"):
                print("options")
            elif(self.selected_exit_sprite == "on"):
                self.scene.exit()

        if(key := event_handler.EventHandler().check_events("Mouse motion")):
            if(self.play_button["off"][1].is_colliding(key.pos)):
                self.selected_play_sprite = "on"
            else:
                self.selected_play_sprite = "off"

            if(self.options_button["off"][1].is_colliding(key.pos)):
                self.selected_options_sprite = "on"
            else:
                self.selected_options_sprite = "off"

            if(self.exit_button["off"][1].is_colliding(key.pos)):
                self.selected_exit_sprite = "on"
            else:
                self.selected_exit_sprite = "off"

    def draw(self):
        self.screen.blit(self.play_button[self.selected_play_sprite][0].image,
                         self.play_button[self.selected_play_sprite][0].rect[0:2])
        
        self.screen.blit(self.options_button[self.selected_options_sprite][0].image,
                         self.options_button[self.selected_options_sprite][0].rect[0:2])
        
        self.screen.blit(self.exit_button[self.selected_exit_sprite][0].image,
                         self.exit_button[self.selected_exit_sprite][0].rect[0:2])
        
        if(self.debug):
            pygame.draw.rect(self.screen,(255,0,0),self.play_button[self.selected_play_sprite][1].rect)
            pygame.draw.rect(self.screen,(255,0,0),self.options_button[self.selected_options_sprite][1].rect)
            pygame.draw.rect(self.screen,(255,0,0),self.exit_button[self.selected_exit_sprite][1].rect)