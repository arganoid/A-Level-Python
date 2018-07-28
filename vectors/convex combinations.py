import random
import sys
import pygame

def make_random_convex_combination(polygon):
    # Create random number 0 to 1 for each point's x and y
    combination_factors = []
    for i in range(len(polygon)):
        factor = random.random()
        combination_factors.append(factor)

    return make_convex_combination(polygon,combination_factors)

def make_convex_combination(polygon, combination_factors):
    total = sum(combination_factors)
    combination_x = 0
    combination_y = 0
    for i in range(len(polygon)):
        combination_x += (combination_factors[i] / total) * polygon[i][0]
        combination_y += (combination_factors[i] / total) * polygon[i][1]

    return [int(combination_x), int(combination_y)]


pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

screen_size = (800,600)
screen = pygame.display.set_mode(screen_size)

triangle = [ [400,50], [700,500], [100,500]]
#polygon = [ [100,100], [500,100], [700,300], [500,500], [100,500]]
#polygon = [ [400,50], [700,100], [750,300], [400,500], [100,300], [200,200]]

screen.fill(WHITE)


def draw_polygon(polygon):
    for i in range(0, len(polygon)):
        pos1 = polygon[i]
        pos2 = polygon[(i + 1) % len(polygon)]
        pygame.draw.line(screen, BLACK, pos1, pos2, 1)


def fill_triangle_sequentially():
    draw_polygon(triangle)

    max = 50
    combination_factors = [0,0,0]
    for i1 in range(1,max):
        combination_factors[0] = i1
        for i2 in range(1,max):
            combination_factors[1] = i2
            for i3 in range(1,max):
                combination_factors[2] = i3

                combination_pos = make_convex_combination(triangle,combination_factors)

                r = random.randint(0, 200)
                g = random.randint(0, 200)
                b = random.randint(0, 200)
                pygame.draw.circle(screen, (r, g, b), combination_pos, 3)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # If user clicked close
                        sys.exit()

                pygame.display.flip()

def fill_polygon_randomly():
    polygon = triangle
    draw_polygon(polygon)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                sys.exit()

        combination_pos = make_random_convex_combination(polygon)
        r = random.randint(0, 200)
        g = random.randint(0, 200)
        b = random.randint(0, 200)
        pygame.draw.circle(screen, (r, g, b), combination_pos, 3)

        pygame.display.flip()

#fill_triangle_sequentially()
fill_polygon_randomly()
