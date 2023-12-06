import random

import gameobject
import image
import snake

class Apple(gameobject.GameObject):
    def __init__(self, scene):
        self.color = (58,224,189)
        img = image.Image([46,46])
        img().fill(self.color)
        super().__init__(img)

        self.scene = scene

        self.change_position(self.scene.grid.ret_coord_grid([random.randint(0,self.scene.grid.max[0]),random.randint(0,self.scene.grid.max[1])]))

    def on_collision(self, obj):
        if(isinstance(obj,snake.Snake)):
            obj.increment_body()
            self.relocate_position(obj.snake_body)
            self.scene.add_score()

    def relocate_position(self, sprites):
        pos = [i.rect[0:2] for i in sprites]
        not_posibilities = [self.rect[0:2]] + pos

        choosed = [0,0]

        for i in range(20):
            rand = [random.randint(0,self.scene.grid.max[0]),random.randint(0,self.scene.grid.max[0])]
            if(self.scene.grid.ret_coord_world(rand) not in not_posibilities):
                choosed = self.scene.grid.ret_coord_world(rand)
                break

        self.change_position(choosed)