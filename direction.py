import pygame

class Direction:
    def __init__(self, direction, time):
        self.direction = direction
        self.time = time

    def diff_time(self, direction) -> int:
        return (self.time-direction.time)
    
