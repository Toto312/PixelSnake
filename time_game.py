import pygame

import utils

class Time(metaclass = utils.SingletonMeta):
    def __init__(self):
        self.clock = pygame.time.Clock()
    
        self.fps = 30
        self.dt = 0

    def update(self):
        self.dt = self.clock.tick(self.fps)

    def get_fps(self):
        return self.clock.get_fps()