import os
import sys
import pygame
import random

import event_handler
import scene_manager
import time_game
import scenes
import debug

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

class Game:
    def __init__(self):
        pygame.init()

        icon = pygame.image.load("Resources/logo.ico")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("PixelSnake")
        self.screen = pygame.display.set_mode([700,700], pygame.RESIZABLE)

        self.event_handler = event_handler.EventHandler()
        self.event_handler.add_button(event_handler.Button("Menu",pygame.K_ESCAPE))
        self.event_handler.add_button(event_handler.Button("Debug",pygame.K_F1))
        self.scene_manager = scene_manager.SceneManager()
        self.time = time_game.Time()
  
        self.game_scene = scenes.GameScene()
        self.scene_manager.add_scene(self.game_scene)
        
        self.menu_scene = scenes.MenuScene()
        self.scene_manager.add_scene(self.menu_scene)

        self.debug = debug.DebugInfo()
        self.show_fps = time_game.ShowFPS()

        # Music
        self.event_handler.create_event("End music")
        self.music = ["Resources/music/music1.mp3", "Resources/music/music2.mp3", "Resources/music/music3.mp3"]
        self.now_playing = random.choice(self.music)
        pygame.mixer.music.load(self.now_playing)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(self.event_handler.event_types["End music"])

        pygame.mixer.music.set_volume(0)

    def mainloop(self):
        while True:
            self.time.update()

            # update events
            self.show_fps.update()
            self.event_handler.update()
            self.check_game_events()
            self.scene_manager.update()

            # draw
            self.screen.fill((0,0,0))
            self.scene_manager.draw()
            self.show_fps.draw()
            pygame.display.flip()

    def check_game_events(self):
        if(self.event_handler.check_events("Quit")):
            pygame.quit()
            sys.exit()

        if(self.event_handler.is_button_pressed("Debug")):
            self.debug.change_state(not self.debug.is_active)
        if(key := self.event_handler.check_events("Key down")):
            # F4
            if(key.scancode == 61 and self.event_handler.is_control_key_pressed):
                pygame.quit()
                sys.exit()

        if(video := self.event_handler.check_events("Video resize")):
            width, height = video.size
            if(width < 700 or height < 700):
                width = 700
                height = 700
            self.screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
            self.scene_manager.resize([width,height])
            
    def music_manager(self):
        if(self.event_handler.check_events("End music")):
            self.change_music()
            pygame.mixer.music.set_volume(0)

    def change_music(self):
        next = self.music.index(self.now_playing)-1
        self.now_playing = self.music[next]
        pygame.mixer.music.load(self.now_playing)
        pygame.mixer.music.play()

        
if(__name__=="__main__"):
    g = Game()
    g.mainloop()