import pygame, sys

pygame.init()
scrInfo = pygame.display.Info()
print(scrInfo)
size = width, height = 800, 480
##size = width, height = scrInfo.current_w, scrInfo.current_h
speed = [1, 1] ##小球速度
BLACK = 0, 0, 0 ##背景颜色
FullWin = pygame.FULLSCREEN #(全屏)
Window = pygame.RESIZABLE #(窗口化)
screen = pygame.display.set_mode(size,Window)
pygame.display.set_caption("小球游戏")
ball = pygame.image.load("smallball.png")
# 获取rect对象
ballrect = ball.get_rect()
fps = 24
fclock = pygame.time.Clock()
still = False
bgcolor = pygame.Color("black")

def RGBChannel(a):
    return 0 if a<0 else (255 if a>255 else int(a))

while True:
    revent = pygame.event.Event(pygame.KEYDOWN,{"unicode":233,"key":pygame.K_RIGHT,"mod":pygame.K_RIGHT})
    levent = pygame.event.Event(pygame.KEYDOWN,{"unicode":233,"key":pygame.K_LEFT,"mod":pygame.K_LEFT})
    if speed[0] < 10:
        pygame.event.post(revent)
    if speed[0] > 10:
        pygame.event.post(levent)
    print(speed[0])
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
            elif event.key == pygame.K_ESCAPE:#退出操作
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size,Window)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
    if pygame.display.get_active() and not still:
        ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
        if ballrect.right > width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = - speed[1]
    bgcolor.r = RGBChannel(ballrect.left*255/width)
    bgcolor.g = RGBChannel(ballrect.top*255/height)
    bgcolor.b = RGBChannel(min(speed[0],speed[1])*255/max(speed[0],speed[1],1))

    screen.fill(bgcolor)
    # 将小球图形绘制到rect对象位置上
    screen.blit(ball, ballrect)
    pygame.display.update()
    fclock.tick(fps)
