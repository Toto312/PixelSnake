import pygame

class Window:
    def __init__(self, size: tuple[int,int] = (800,800)):
        self.size = size

        if(not pygame.display.get_init() or not pygame.get_init()):
            print("Error \"Window\" class: Initialize display")
            return
        else:
            self.screen = pygame.display.get_active()

if(__name__=="__main__"):
    w = Window()