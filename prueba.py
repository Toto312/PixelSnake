import pygame
import sys

class Grid:
    def __init__(self, dimensions, size):
        self.dimensions = dimensions
        self.size = size

        self.offset = [0,0]

        self.max = self.ret_grid(self.size)
        self.max[0] -= 1
        self.max[1] -= 1

    def ret_coord_grid(self, coord):
        return [(coord[0]//self.dimensions[0]) * self.dimensions[0], (coord[1]//self.dimensions[1]) * self.dimensions[1]]
    
    def ret_grid(self,coord):
        return [(coord[0]//self.dimensions[0]), (coord[1]//self.dimensions[1])]

    def ret_coord_world(self,coord):
        return [coord[0] * self.dimensions[0],coord[1] * self.dimensions[1]]

pygame.init()

# Set up display
width, height = 800, 600
grid = Grid([50,50],[800,600])
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Resizable Square")


limit = pygame.Rect(0,0,600,600)
limit.x, limit.y = [(width - limit.width) // 2 ,(height - limit.height) // 2]

# Set up square
square_color = (255, 0, 0)  # Red
square = pygame.Surface([50,50])
square.fill(square_color)
x = 0
y = 0

clock = pygame.time.Clock()

size = pygame.display.get_window_size()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            if(width < 600 or height < 600):
                width = 600
                height = 600
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            # Update square position to stay in the center
            a, b = [(width - size[0]) / 2 ,(height - size[1]) / 2]
            size = pygame.display.get_window_size()
            limit.x += a
            limit.y += b

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 5
    elif(keys[pygame.K_s]):
        y += 5
    elif(keys[pygame.K_a]):
        x -= 5
    elif(keys[pygame.K_d]):
        x += 5

    # Draw everything
    screen.fill((255, 255, 255))  # White background
    pygame.draw.rect(screen,(175,175,175),limit,5)
    screen.blit(square, [grid.ret_coord_grid([x, y])[0] + limit.x,grid.ret_coord_grid([x, y])[1] + limit.y])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()