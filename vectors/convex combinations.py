import random
import sys
import time

import pygame

# 0.4  0.1 0.1 0.4

def make_random_convex_combination(polygon):
    # Create random number 0 to 1 for each point's x and y
    combination_factors = []
    total = 0
    for i in range(len(polygon)):
        factor = random.random()
        combination_factors.append(factor)
        total += factor

    return make_convex_combination(polygon,combination_factors, total)


def make_convex_combination(polygon, combination_factors, total=1):

    combination_x = 0
    combination_y = 0
    for i in range(len(polygon)):
        combination_x += (combination_factors[i] / total) * polygon[i][0]
        combination_y += (combination_factors[i] / total) * polygon[i][1]

    return [int(combination_x), int(combination_y)]


pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

screen_size = (800,600)
screen = pygame.display.set_mode(screen_size)

font = pygame.font.Font(None, 50)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#polygon = [ [400,50], [700,100], [750,300], [400,500], [100,300], [200,200]]
#polygon = [ [100,100], [500,100], [700,300], [500,500], [100,500]]
polygon = [ [400,50], [700,500], [100,500]]

screen.fill(WHITE)

for i in range(0, len(polygon)):
    pos1 = polygon[i]
    pos2 = polygon[(i + 1) % len(polygon)]
    pygame.draw.line(screen, BLACK, pos1, pos2, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            sys.exit()

    combination_factors = [0,0,0]
    for i1 in range(1,101):
        combination_factors[0] = i1 * 0.01
        for i2 in range(1,101):
            combination_factors[1] = i2 * 0.01
            for i3 in range(1, 101):
                combination_factors[2] = i2 * 0.01
                total = sum(combination_factors)
                for i in range(len(combination_factors)):
                    combination_factors[i] /= total
                combination_pos = make_convex_combination(polygon,combination_factors, total)

                r = random.randint(0, 200)
                g = random.randint(0, 200)
                b = random.randint(0, 200)
                pygame.draw.circle(screen, (r, g, b), combination_pos, 3)

                pygame.display.flip()

    #combination_pos = make_random_convex_combination(polygon)
    # r = random.randint(0, 200)
    # g = random.randint(0, 200)
    # b = random.randint(0, 200)
    # pygame.draw.circle(screen, (r, g, b), combination_pos, 3)
    #
    # pygame.display.flip()




