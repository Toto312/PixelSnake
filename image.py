import pygame

def get_surface(img: str | list[int,int] | pygame.Surface) -> pygame.Surface:
    if(isinstance(img,str)):
        image = pygame.image.load(img)
    elif(isinstance(img,pygame.Surface)):
        image = img
    elif(isinstance(img[0],int) and isinstance(img[1],int) and isinstance(img[1],int) and len(img)>=2):
        image = pygame.Surface(img[0:2])
        image.fill((255,255,255))
    image.convert_alpha()
    return image