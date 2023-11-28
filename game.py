import pygame

import event_handler
import sprite
import scene_manager
import gameobject
import scene
import image
import time_game

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([800,800])
        self.event_handler = event_handler.EventHandler()
        self.scene_manager = scene_manager.SceneManager()
        self.time = time_game.Time()


        self.s = gameobject.GameObject(image.Image([50,50]))
        self.s.scale([64,64])
        self.s.move([64,64])
        self.scene = scene.Scene()
        self.scene.add_object(self.s)
        self.scene_manager.add_scene(self.scene)

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
            print(max(video.size))

    def mainloop(self):
        while True:
            self.time.update()

            # update events
            self.event_handler.update()
            self.check_game_events()
            self.scene_manager.update()

            # draw
            self.screen.fill((0,0,0))
            self.scene_manager.draw()
            pygame.display.flip()

if(__name__=="__main__"):
    g = Game()
    g.mainloop()