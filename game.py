import os
import sys
import pygame

import event_handler
import scene_manager
import time_game
import scenes
import font

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

class Game:
    def __init__(self):
        pygame.init()

        icon = pygame.image.load("Resources/logo.ico")
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode([800,800], pygame.RESIZABLE)

        self.event_handler = event_handler.EventHandler()
        self.scene_manager = scene_manager.SceneManager()
        self.time = time_game.Time()
  
        self.game_scene = scenes.GameScene()
        self.scene_manager.add_scene(self.game_scene)

        self.fps_font = font.Font("Resources/PixeloidSans.ttf",f"FPS: {round(self.time.get_fps())}",[self.screen.get_size()[0]*0.8,self.screen.get_size()[1]*0.1],30)
        self.fps_font.change_position([self.screen.get_size()[0]-self.fps_font.surface.get_rect()[2],0])
    def check_game_events(self):
        if(self.event_handler.check_events("Quit")):
            pygame.quit()
            exit()

        if(key := self.event_handler.check_events("Key down")):
            # F4
            if(key.scancode == 61):
                pygame.quit()
                exit()

        if(video := self.event_handler.check_events("Video Resize")):
            width, height = video.size
            if width < 600:
                width = 600
            if height < 600:
                height = 600
            self.screen = pygame.display.set_mode((width,height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

    def mainloop(self):
        while True:
            self.time.update()

            # update events
            self.fps_font.change_text(f"FPS: {round(self.time.get_fps())}")
            self.fps_font.change_position([self.screen.get_size()[0]-self.fps_font.surface.get_rect()[2],0])
            self.event_handler.update()
            self.check_game_events()
            self.scene_manager.update()

            # draw
            self.screen.fill((0,0,0))
            self.scene_manager.draw()
            self.fps_font.draw(self.screen)
            pygame.display.flip()

if(__name__=="__main__"):
    g = Game()
    g.mainloop()