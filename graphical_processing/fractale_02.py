# Julia 's set
# Need pygame to work
# by Olivier Darchy
# 2017

import sys, pygame, threading, time

ZOOM = 300
SC_LEFT = -1
SC_RIGHT = 1
SC_DOWN = -1.2
SC_TOP = 1.2
IT_MAX = 400
C = (0.285, 0.01)

width = int((SC_RIGHT - SC_LEFT) * ZOOM)
height = int((SC_TOP - SC_DOWN) * ZOOM)
eval_z = lambda x, y : ((x / ZOOM + SC_LEFT), (y / ZOOM + SC_DOWN))

pygame.init()
screen = pygame.display.set_mode((width, height))

class Drawer(threading.Thread) :
    def __init__(self, x_range, y_range) :
        threading.Thread.__init__(self)
        self.x_range, self.y_range = x_range, y_range

    def run(self) :
        t0 = time.time()
        draw(self.x_range, self.y_range)
        print("delay : {} s".format(time.time() - t0))


def compute(x, y, c) :
    z = eval_z(x, y)
    for i in range(IT_MAX) :
        z = z[0] ** 2 - z[1] ** 2 + c[0] , 2 * z[0] * z[1] + c[1]
        if (z[0] ** 2 + z[1] ** 2 >= 4) :
            return i
    return IT_MAX

def draw(x_range, y_range) :
    for x in range(x_range[0], x_range[1]) :
        for y in range(y_range[0], y_range[1]) :
            it = compute(x, y, C)
            val = it * 255 // IT_MAX
            color = pygame.Color(0, val % 50, val, 0)
            screen.set_at((x, y), color)

once = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if once :
        thread1 = Drawer((0, width), (0, height // 2))
        thread2 = Drawer((0, width), (height // 2, height))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        pygame.display.flip()
        once = False
