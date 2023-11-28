import scene
import snake

class GameScene(scene.Scene):
    def __init__(self):
        super().__init__("Game")

        self.snake = snake.Snake()
        self.add_object(self.snake.snake_body.sprites())

    def update(self):
        self.snake.update()

    def draw(self, window):
        self.objects.draw(window)