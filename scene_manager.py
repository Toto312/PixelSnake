import pygame

class Scene:
    def __init__(self,name):
        self.name = name
    def update(self):
        pass
    def draw(self):
        pass

class SceneManager:
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
        if(len(self.scenes)==0 or self.curr_scene_index<0 or self.curr_scene_index>=len(self.scenes)):
            return
        self.scenes[self.curr_scene_index].update()
    
    def draw(self):
        if(len(self.scenes)==0 or self.curr_scene_index<0 or self.curr_scene_index>=len(self.scenes)):
            return

        self.scenes[self.curr_scene_index].draw()

if (__name__=="__main__"):
    sm = SceneManager()
    s = Scene("Hola")
    s1 = Scene("Chau")
    sm.add_scene(s)
    sm.add_scene(s1)
    sm.change_scene("si")
    print(sm.curr_scene.name)