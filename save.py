import os
import json
import pygame

import utils

DEFAULT = {"resolution" : "700x700", "fullscreen" : "false", "volume" : 1,
       "up" : 1073741906, "down" : 1073741905, "left" : 1073741904, "right" : 1073741903,
       "Menu" : pygame.K_ESCAPE, "Debug" : 1073741882, "max score" : 0}

class SaveFile(metaclass=utils.SingletonMeta):
    def __init__(self):
        if(not os.path.isdir("Save")):
            os.mkdir("Save")

        self.save_file = "Save/save.json"

    def does_exist(self):
        path_exist = os.path.exists(self.save_file)
        is_full = True
        if(path_exist):
            file = open(self.save_file,"r")
            if(file.read()==""):
                is_full = False
        return os.path.exists(self.save_file) and is_full

    def write_file(self, values=None):
        with open(self.save_file,"w") as file:
            if(not values):
                content = json.dumps(DEFAULT, indent=4)
            else:
                content = json.dumps(values, indent=4)

            file.write(content)

    def read_file(self):
        if(not os.path.exists(self.save_file)):
            with open(self.save_file,"w") as f:
                pass
            return None
        
        with open(self.save_file,"r") as file:
            buffer = file.read()
            if(buffer==""):
                return None
            converted = json.loads(buffer)

        return converted
    
    def read_value(self, name: str):
        content = self.read_file()
        if(content==None):
            return None
        return content[name]

    def change_value(self, name: str, value: str):
        content = self.read_file()
        if(content==None):
            return
        content[name] = value
        self.write_file(content)
        

if(__name__=="__main__"):
    s = SaveFile()
    s.write_file()
    print(s.read_value("down"))
