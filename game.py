import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([800,800])

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    exit()
            
            self.screen.fill((0,0,0))

            pygame.display.flip()

if(__name__=="__main__"):
    g = Game()
    g.mainloop()