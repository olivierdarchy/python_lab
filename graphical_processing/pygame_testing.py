# pygame: first program
# by Olivier Darchy
# 2017

import sys, pygame
from pygame.locals import *
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
radius = 20
black = 0x000000
blue = 0x0000ff

screen = pygame.display.set_mode(size)

ballpos = 160, 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballpos = ballpos[0] + speed[0], ballpos[1] + speed[1]
    if ballpos[0] - radius < 0 or ballpos[0] + radius > width:
        speed[0] = -speed[0]
    if ballpos[1] - radius < 0 or ballpos[1] + radius > height:
        speed[1] = -speed[1]

    screen.fill(black)
    pygame.draw.circle(screen, blue, ballpos, radius, 0)
    pygame.display.flip()
    pygame.time.delay(50)
