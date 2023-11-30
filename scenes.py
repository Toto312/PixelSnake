import pygame

import scene
import snake
import grid
import event_handler
import apple
import gameobject
import image

class GameScene(scene.Scene):
    def __init__(self):
        super().__init__("Game")

        self.screen = pygame.display.get_surface()
        self.event_handler = event_handler.EventHandler()
        self.grid = grid.Grid([50,50],[800,800])
        self.limit = pygame.Rect(0,0,self.screen.get_width(),self.screen.get_height())

        self.snake = snake.Snake(self)
        self.apple = apple.Apple(self)
        self.add_object(self.apple)

        self.apple.relocate_position(self.snake.snake_body.sprites())
        
        self.score = 0
        self.is_paused = False

        #im = image.Image([5,5])
        #im().fill((255,255,255))
        #self.rel_pos = gameobject.GameObject(im)
        #self.rel_pos.change_position(self.snake.real_pos)

    def check_events(self):
        if(button := self.event_handler.check_events("Key down")):
            if(button.key == pygame.K_p):
                self.is_paused = not self.is_paused


    def check_events_movement(self):
        if(button := self.event_handler.check_events("Key down")):
            if(button.key == pygame.K_w):
                self.snake.change_direction([0,-1])
            elif(button.key == pygame.K_s):
                self.snake.change_direction([0,1])
            elif(button.key == pygame.K_a):
                self.snake.change_direction([-1,0])
            elif(button.key == pygame.K_d):
                self.snake.change_direction([1,0])

    def check_collision(self):
        if(self.apple.rect.colliderect(self.snake.head)):
            self.snake.increment_body()
            self.apple.relocate_position(self.snake.snake_body.sprites())
            self.score += 1

    def add_score(self):
        self.score += 1

    def update(self):
        #self.rel_pos.change_position(self.snake.real_pos)
        self.check_events()
        if(not self.is_paused):
            self.check_events_movement()
            self.snake.update()
            self.check_collision()

    def draw(self, window):
        self.objects.draw(window)
        self.snake.snake_body.draw(window)
        #window.blit(self.rel_pos.image,self.rel_pos.rect[0:2])