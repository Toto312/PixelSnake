import pygame

import save
import utils

class Volume(metaclass=utils.SingletonMeta):
    def __init__(self):
        if(vol := save.SaveFile().read_value("volume")):
            self.volume = float(vol)
        else:
            self.volume = 1
