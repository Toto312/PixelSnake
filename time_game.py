import pygame

import utils
import font
import debug

class Time(metaclass = utils.SingletonMeta):
    def __init__(self):
        self.clock = pygame.time.Clock()
    
        self.fps = 60
        self.dt = 0

    def update(self):
        self.dt = self.clock.tick(self.fps)

    def get_fps(self):
        return self.clock.get_fps()
    
class ShowFPS:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.fps_font = font.Font("Resources/PixeloidSans.ttf",f"FPS: {round(Time().get_fps())}",[self.screen.get_size()[0]*0.8,self.screen.get_size()[1]*0.1],30)
        self.fps_font.change_position([self.screen.get_size()[0]-self.fps_font.surface.get_rect()[2],self.screen.get_size()[1]-self.fps_font.surface.get_rect()[3]])

    def update(self):
        if(debug.DebugInfo().is_active):
            self.fps_font.change_text(f"FPS: {round(Time().get_fps())}")
            self.fps_font.change_position([self.screen.get_size()[0]-self.fps_font.surface.get_rect()[2],self.screen.get_size()[1]-self.fps_font.surface.get_rect()[3]])
    
    def draw(self):
        if(debug.DebugInfo().is_active):
            self.fps_font.draw(self.screen)