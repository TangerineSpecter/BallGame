import pygame,sys

pygame.init()
size = width,height = 800,480
speed = [1,1]
BLACK = 0,0,0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame小球游戏")
ball = pygame.image.load("smallball.png")
#获取rect对象
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
    screen.fill(BLACK)
    # 将小球图形绘制到rect对象位置上
    screen.blit(ball,ballrect)
    pygame.display.update()