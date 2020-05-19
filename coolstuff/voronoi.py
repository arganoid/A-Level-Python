# This has nothing to do with the A-level syllabus but is cool so I included it anyway
# Requires pygame library

# Need help understanding computer science and programming?
# Arganoid Tuition - https://tutor.arganoid.com/

import sys
import random
import profiler

import pygame
import pygame.gfxdraw

NUM_POINTS = 100

SAVE_IMAGES = False

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

pygame.init()

screen_size = (1280,720)
screen = pygame.display.set_mode(screen_size)

screen.fill(WHITE)

points = []
for i in range(0, NUM_POINTS):
    pos = [ random.randint(0,screen_size[0]), random.randint(0,screen_size[1]) ]
    col = ( random.randint(0,255), random.randint(0,255), random.randint(0,255) )
    vel = ( random.randrange(-1,1), random.randrange(-1,1) )
    points.append( (pos, col, vel) )

image_idx = 0

line_profiler = profiler.Profiler()
frame_profiler = profiler.Profiler()

while True:
    for py in range(0, screen_size[1]):
        for px in range(0, screen_size[0]):

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    sys.exit()

            # timings: 720p, 1000 points

            # 1.6s per line
            # nearest_point = sorted(points, key=lambda p: ((px-p[0][0]) ** 2 + (py-p[0][1]) ** 2))[0]

            # 2.6s per line
            # def closer(p1,p2):
            #     return p1 if ((px - p1[0][0]) ** 2 + (py - p1[0][1]) ** 2) < ((px - p2[0][0]) ** 2 + (py - p2[0][1]) ** 2) else p2
            # nearest_point = functools.reduce( closer, points, ((1e9,1e9),) )

            # 1.45s per line
            best_dist = 1e9
            for point in points:
                dist = (px-point[0][0]) ** 2 + (py-point[0][1]) ** 2
                if dist < best_dist:
                    nearest_point = point
                    best_dist = dist

            pygame.gfxdraw.pixel(screen, px, py, nearest_point[1])

            if px == 0:
                pygame.display.flip()
            #     print("Line: " + str(line_profiler.get_seconds()))
            #     line_profiler = profiler.Profiler()

    print("Frame: " + str(frame_profiler.get_seconds()))
    pygame.display.flip()
    frame_profiler = profiler.Profiler()

    if SAVE_IMAGES:
        pygame.image.save(screen, f"img{image_idx:04}.png" )
        image_idx += 1

    # Apply velocity to points
    for point in points:
        point[0][0] += point[2][0]
        point[0][1] += point[2][1]
