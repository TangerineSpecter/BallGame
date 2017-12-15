import pygame, sys

pygame.init()
size = width, height = 800, 480
speed = [1, 1]
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("小球游戏")
ball = pygame.image.load("smallball.png")
# 获取rect对象
ballrect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:#按下键盘
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int (speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
    screen.fill(BLACK)
    # 将小球图形绘制到rect对象位置上
    screen.blit(ball, ballrect)
    pygame.display.update()
    fclock.tick(fps)
