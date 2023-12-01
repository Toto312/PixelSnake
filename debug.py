import font
import time_game

class DebugInfo:
    def __init__(self, screen):
        self.screen = screen
        self.fps_font = font.Font("Resources/PixeloidSans.ttf",f"FPS: {round(time_game.Time().get_fps())}",[self.screen.get_size()[0]*0.8,self.screen.get_size()[1]*0.1],30)
        self.fps_font.change_position([self.screen.get_size()[0]-self.fps_font.surface.get_rect()[2],self.screen.get_size()[1]-self.fps_font.surface.get_rect()[3]])
    
    def update(self):
        self.fps_font.change_text(f"FPS: {round(time_game.Time().get_fps())}")
        self.fps_font.change_position([self.screen.get_size()[0]-self.fps_font.surface.get_rect()[2],self.screen.get_size()[1]-self.fps_font.surface.get_rect()[3]])
    
    def draw(self):
        self.fps_font.draw(self.screen)