# Voronoi diagram generator, dividing the world into grid squares to improve performance (only need to search for points
# in nearby grid squares rather than searching all points)
# Notice how default NUM_POINTS is 1000 rather than 100 but it still runs faster than the other version

# This has nothing to do with the A-level syllabus but is cool so I included it anyway
# Requires pygame library

# Need help understanding computer science and programming?
# Arganoid Tuition - https://tutor.arganoid.com/


import sys
import random
import profiler

import pygame
import pygame.gfxdraw

NUM_POINTS = 1000

SHOW_GRID = True
SHOW_POINTS = True

SAVE_IMAGES = False

random.seed(2)

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

pygame.init()

screen_size = (1280,720)
screen = pygame.display.set_mode(screen_size)

screen.fill(WHITE)

cells = []
world_left = -1000
world_right = 3000
world_top = -1000
world_bottom = 2000
cell_size = 30

world_max_dimension = max(world_right - world_left, world_top - world_bottom)

for y in range(world_top, world_bottom, cell_size):
    row = []
    for x in range(world_left, world_right, cell_size):
        cell = []
        row.append(cell)
    cells.append(row)

points = []
for i in range(0, NUM_POINTS):
    pos = [ random.randint(0,screen_size[0]), random.randint(0,screen_size[1]) ]
    col = ( random.randint(0,255), random.randint(0,255), random.randint(0,255) )
    vel = ( random.randrange(-1,1), random.randrange(-1,1) )

    cell_x = (pos[0] - world_left) // cell_size
    cell_y = (pos[1] - world_top) // cell_size

    point = [pos, col, vel, cell_x, cell_y]
    points.append( point )

    cells[cell_y][cell_x].append(point)


image_idx = 0

line_profiler = profiler.Profiler()
frame_profiler = profiler.Profiler()

while True:
    for py in range(0, screen_size[1]):
        for px in range(0, screen_size[0]):
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    sys.exit()

            best_dist_sq = 1e9 ** 2
            px_world_space = (px - world_left)
            py_world_space = (py - world_top)
            cell_x = px_world_space // cell_size
            cell_y = py_world_space // cell_size
            nearest_point = None

            radius = cell_size      # Avoid square/circle problem
            radius_sq = radius ** 2

            cells_fully_visited = []    # actually slower?

            while nearest_point == None and radius <= world_max_dimension:
                x_start = max( (px_world_space - radius) // cell_size, 0 )
                x_end = min( (px_world_space + radius) // cell_size, len(cells[0]))
                y_start = max( (py_world_space - radius) // cell_size, 0 )
                y_end = min( (py_world_space + radius) // cell_size, len(cells))
                cells_range_x = range( x_start, x_end + 1 )
                cells_range_y = range( y_start, y_end + 1)

                for cell_search_y in cells_range_y:
                    for cell_search_x in cells_range_x:
                        cell = cells[cell_search_y][cell_search_x]
                        any_not_visited = False
                        if not cell in cells_fully_visited:
                            for point in cell:
                                dist_sq = (px-point[0][0]) ** 2 + (py-point[0][1]) ** 2
                                if dist_sq > radius_sq:
                                    any_not_visited = True
                                elif dist_sq < best_dist_sq:
                                    nearest_point = point
                                    best_dist_sq = dist_sq
                            if not any_not_visited:
                                cells_fully_visited.append(cell)
                if nearest_point == None:
                    radius += cell_size
                    radius_sq = radius ** 2

            if nearest_point != None:
                pygame.gfxdraw.pixel(screen, px, py, nearest_point[1])
            else:
                pygame.gfxdraw.pixel(screen, px, py, BLACK)

            # if px == 0:
            #     #print("Line: " + str(line_profiler.get_seconds()))
            #     pygame.display.flip()
            #     #line_profiler = profiler.Profiler()

    print("Frame: " + str(frame_profiler.get_seconds()))
    pygame.display.flip()

    if SHOW_GRID:
        for y in range(world_top, world_bottom, cell_size):
            row = []
            for x in range(world_left, world_right, cell_size):
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, cell_size, cell_size), 1)

    if SHOW_POINTS:
        for point in points:
            pygame.draw.circle(screen, RED, point[0], 2)

    frame_profiler = profiler.Profiler()

    if SAVE_IMAGES:
        pygame.image.save(screen, f"img{image_idx:04}.png")
        image_idx += 1

    # Apply velocity to points
    for point in points:
        px, py = point[0][0], point[0][1]
        old_cell_x = (px - world_left) // cell_size
        old_cell_y = (py - world_top) // cell_size
        point[0][0] += point[2][0]
        point[0][1] += point[2][1]
        new_cell_x = (px - world_left) // cell_size
        new_cell_y = (py - world_top) // cell_size
        if new_cell_x != old_cell_x or new_cell_y != old_cell_y:
            cells[old_cell_y][old_cell_x].remove(point)
            cells[new_cell_y][new_cell_x].append(point)
            point[3][0] = new_cell_x
            point[3][1] = new_cell_y
