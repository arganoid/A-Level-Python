# This has nothing to do with the A-level syllabus (except perhaps for recursion) but is cool so I included it anyway
# Requires pygame library

# http://www.pygame.org/docs/ref/gfxdraw.html

# The Mandelbrot set is the set of complex numbers c for which the function f c ( z ) = z^2 + c
# does not diverge when iterated from z = 0, i.e., for which the sequence f c ( 0 ),  f c ( f c ( 0 ) ), etc.,
# remains bounded in absolute value.

import sys

import pygame
import pygame.gfxdraw

max_iterations = 60
threshold = 1000

# The 'f' recursive function is used to decide the colour of each pixel in the Mandelbrot set
# Here I also illustrate Python's 'type hinting' system. For each variable/parameter you can specify the type that
# variable is intended to be. The same can be done for function return types. Python does not enforce these type hints,
# but IDEs such as Pycharm use them to indicate possible errors to the programmer.
def f(z: complex, c: complex, iterations:int = 0) -> int:
    result = z*z + c
    if abs(result) > threshold:
        return iterations
    else:
        if iterations == max_iterations:
            return 0
        else:
            return f(result, c, iterations+1)

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

pygame.init()

screen_size = (1280,720)
screen = pygame.display.set_mode(screen_size)


screen.fill(WHITE)
scale = 0.3
offsetX = -2.5
offsetY = -1.0
aspect = screen_size[0] / screen_size[1]

cols = []
for i in range(0,max_iterations+1):
    c = (i / max_iterations) * 255
    cols.append( (c,c,c) )

while True:
    screen.fill(WHITE)
    for py in range(0, screen_size[1]):
        for px in range(0, screen_size[0]):
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    sys.exit()
            x = (px / screen_size[0] / scale) + offsetX
            y = (py / screen_size[1] / scale / aspect) + offsetY
            result = f(0, complex(x, y))
            pygame.gfxdraw.pixel(screen, px, py, cols[result])
            if px == 0:
                pygame.display.flip()

    pygame.display.flip()

    kp = False
    while not kp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_MINUS:
                    scale *= 0.8
                    kp = True
                elif event.key == pygame.K_EQUALS:
                    scale *= 1.2
                    kp = True
                elif event.key == pygame.K_LEFT:
                    offsetX -= 0.1 / scale
                    kp = True
                elif event.key == pygame.K_RIGHT:
                    offsetX += 0.1 / scale
                    kp = True
                elif event.key == pygame.K_UP:
                    offsetY -= 0.1 / scale
                    kp = True
                elif event.key == pygame.K_DOWN:
                    offsetY += 0.1 / scale
                    kp = True
                elif event.key == pygame.K_1:
                    max_iterations -= 1
                    kp = True
                elif event.key == pygame.K_2:
                    max_iterations += 1
                    kp = True
                elif event.key == pygame.K_3:
                    threshold *= 0.75
                    kp = True
                elif event.key == pygame.K_4:
                    threshold *= 1.25
                    kp = True
