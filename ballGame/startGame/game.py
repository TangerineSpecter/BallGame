import pygame,sys

pygame.init()
screen = pygame.display.set_mode((800,480))
pygame.display.set_caption("pygame小球游戏")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()