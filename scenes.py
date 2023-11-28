import pygame

import scene
import snake
import grid
import event_handler

class GameScene(scene.Scene):
    def __init__(self):
        super().__init__("Game")

        self.screen = pygame.display.get_surface()

        self.grid = grid.Grid([50,50])

        self.snake = snake.Snake(self)
        self.add_object(self.snake.snake_body.sprites())

        self.event_handler = event_handler.EventHandler()

        self.limit = pygame.Rect(0,0,self.screen.get_width(),self.screen.get_height())

    def check_events(self):
        if(button := self.event_handler.check_events("Key down")):
            if(button.key == pygame.K_w):
                self.snake.change_direction([0,-1])
            elif(button.key == pygame.K_s):
                self.snake.change_direction([0,1])
            elif(button.key == pygame.K_a):
                self.snake.change_direction([-1,0])
            elif(button.key == pygame.K_d):
                self.snake.change_direction([1,0])

    def is_colliding(self, rect):
        return self.limit.colliderect(rect)

    def update(self):
        self.check_events()

        self.snake.update()

    def draw(self, window):
        self.objects.draw(window)