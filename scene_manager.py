import pygame

class SceneManager:
    def __init__(self):
        self.window = pygame.display.get_surface()
        self.scenes = []
        self.curr_scene_index = 0

    def resize(self, size):
        for i in self.scenes:
            i.resize(size)

    def add_scene(self, scene):
        self.scenes.append(scene)
        self.scenes[self.curr_scene_index].is_active = False
        self.curr_scene_index = len(self.scenes)-1

    def update(self):
        if(len(self.scenes)==0 or self.curr_scene_index<0 or self.curr_scene_index>=len(self.scenes)):
            return
        self.scenes[self.curr_scene_index].update()
    
    def draw(self):
        if(len(self.scenes)==0 or self.curr_scene_index<0 or self.curr_scene_index>=len(self.scenes)):
            return

        self.scenes[self.curr_scene_index].draw(self.window)