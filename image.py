import pygame
class Image:
    def __init__(self, *args):
        if(isinstance(args[0],str)):
            self.image = pygame.image.load(args[0])
        elif(isinstance(args[0],pygame.Surface)):
            self.image = args[0]
        elif(isinstance(args[0][0],int) and isinstance(args[0][1],int) and isinstance(args[0][1],int) and len(args[0])>=2):
            self.image = pygame.Surface(args[0][0:2])
            self.image.fill((255,255,255))
    def __call__(self):
        return self.image