import pygame

import utils

class SceneManager(metaclass=utils.SingletonMeta):
    def __init__(self):
        self.scenes = {}
        self.curr_scene = None

    def resize(self, size):
        for i in self.scenes:
            i.resize(size)

    def change_scene(self,name):
        if(not self.scenes.get(name)):
            return -1
        self.curr_scene = self.scenes.get(name)

    def add_scene(self, scene):
        if(len(self.scenes)>0):
            self.curr_scene.is_active = False
        self.scenes.update({scene.name : scene})
        self.curr_scene = scene

    def update(self):
        self.curr_scene.update()
    
    def draw(self):
        self.curr_scene.draw()
