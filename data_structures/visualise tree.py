import math
import sys

import data_structures.binary_search_tree as binary_search_tree
import pygame

my_tree = binary_search_tree.generate_test_tree()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

screen_size = (1250,650)
screen = pygame.display.set_mode(screen_size)
antiAlias = True

pygame.init()

font = pygame.font.Font(None, 30)

screen.fill(WHITE)

# Title
textSurface = font.render(my_tree.__class__.__name__, antiAlias, BLACK)
screen.blit(textSurface, [int((screen_size[0] - textSurface.get_width()) / 2), 0])


def visit_func(value, path):
    # path is the series of left and right moves we've made to get to this point in the tree, eg 'LLRLR'
    x = screen_size[0] / 2
    y = 80
    prev_x = x
    prev_y = y
    depth = 0
    for c in path:
        prev_x = x
        prev_y = y
        y += 80
        depth += 1
        if c == 'L':
            #x -= screen_size[0] * 0.5 * (1/(depth+1))
            #x -= 100 / depth if len(path) > 0 else 200
            x -= 300 / math.pow(depth, 0.9)
        else:
            #x += screen_size[0] * 0.5 * (1 / (depth + 1))
            x += 300 / math.pow(depth, 0.9)

    if depth > 0:
        pygame.draw.line(screen, BLACK, [int(prev_x), int(prev_y)], [int(x), int(y)], )

    pygame.draw.circle(screen, BLACK, [int(x), int(y)], 6 )

    textSurface = font.render(str(value), antiAlias, BLACK)
    screen.blit(textSurface, [int(x-textSurface.get_width()/2), int(y-30)])

my_tree.traverse_in_order_advanced(visit_func)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            sys.exit()
