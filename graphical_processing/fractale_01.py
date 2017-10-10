# mandelbrot implementation
# Need pygame to work
# by Olivier Darchy
# 2017

import sys, pygame, math

pygame.init()

FRAME_SIZE = WIDTH, HEIGHT = 700, 480
X_MIN_MAND = -2.5
X_MAX_MAND = 1
Y_MIN_MAND = -1.2
Y_MAX_MAND = 1.2
MAX_ITERATION = 2000
G_MAX = 0xffffff
G_MIN = 0x000000

mapX = lambda x : X_MIN_MAND + x * (X_MAX_MAND - X_MIN_MAND) / WIDTH
mapY = lambda y : Y_MIN_MAND + y * (Y_MAX_MAND - Y_MIN_MAND) / HEIGHT
mapColor = lambda c : int(G_MAX - c * (G_MAX - G_MIN) / MAX_ITERATION)

screen = pygame.display.set_mode(FRAME_SIZE)

def lerp(v0, v1, t) :
    return v0 + t * (v1 - v0)

def mandelbrot(px, py) :
    x0 = mapX(px)
    y0 = mapY(py)
    x = 0.0
    y = 0.0
    for i in range(MAX_ITERATION):
        if x ** 2 + y ** 2 >= 1 << 16 :
            log_zn = math.log(x ** 2 + y ** 2) / 2
            nu = math.log(log_zn / math.log(2)) / math.log(2)
            return i - nu
        xtmp = x ** 2 - y ** 2 + x0
        ytmp = 2 * x * y + y0
        if xtmp == x and ytmp == y :
            return MAX_ITERATION
        x = xtmp
        y = ytmp
    return MAX_ITERATION

once = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if once :
        for pos in range(WIDTH * HEIGHT + 1):
            px = pos % WIDTH
            py = pos // WIDTH
            it = mandelbrot(px, py)
            color1 = mapColor(it)
            color2 = mapColor(it + 1)
            color = int(lerp(color1, color2, it))
            screen.set_at((px, py), color)
        pygame.display.flip()
        once = False
