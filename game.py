import os
import sys
import pygame

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
        self.scene_manager = scene_manager.SceneManager()
        self.time = time_game.Time()
  
        self.game_scene = scenes.GameScene()
        self.scene_manager.add_scene(self.game_scene)

        self.debug = debug.DebugInfo(self.screen)

    def check_game_events(self):
        if(self.event_handler.check_events("Quit")):
            pygame.quit()
            sys.exit()

        if(key := self.event_handler.check_events("Key down")):
            # F4
            if(key.scancode == 61):
                pygame.quit()
                sys.exit()

        if(video := self.event_handler.check_events("Video resize")):
            width, height = video.size
            if(width < 700 or height < 700):
                width = 700
                height = 700
            self.screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
            self.game_scene.resize([width,height])

    def mainloop(self):
        while True:
            self.time.update()

            # update events
            self.debug.update()
            self.event_handler.update()
            self.check_game_events()
            self.scene_manager.update()

            # draw
            self.screen.fill((0,0,0))
            self.scene_manager.draw()
            self.debug.draw()
            pygame.display.flip()

if(__name__=="__main__"):
    g = Game()
    g.mainloop()