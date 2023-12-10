import pygame

class Direction:
    def __init__(self, direction, time = pygame.time.get_ticks()):
        self.direction = direction
        self.time = time

    def diff_time(self, direction) -> int:
        return abs(self.time-direction.time)
    
