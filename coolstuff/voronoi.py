# This has nothing to do with the A-level syllabus but is cool so I included it anyway
# Requires pygame library

# Need help understanding computer science and programming?
# Arganoid Tuition - https://tutor.arganoid.com/

import sys
import random
import profiler

import pygame
import pygame.gfxdraw

# Settings
NUM_POINTS = 100
SCREEN_SIZE = (640, 480)
SHOW_LINE_BY_LINE = True
SHOW_LINE_TIMINGS = False
SHOW_FRAME_TIMINGS = True
SAVE_IMAGES = False

WHITE = (255, 255, 255)

random.seed(2)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

screen.fill(WHITE)

points = []
for i in range(0, NUM_POINTS):
    pos = [random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1])]
    col = ( random.randint(0,255), random.randint(0,255), random.randint(0,255) )
    vel = ( random.randrange(-1,1), random.randrange(-1,1) )
    points.append( (pos, col, vel) )

image_idx = 0

line_profiler = profiler.Profiler()
frame_profiler = profiler.Profiler()

while True:
    for py in range(0, SCREEN_SIZE[1]):
        for px in range(0, SCREEN_SIZE[0]):

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
                if SHOW_LINE_BY_LINE:
                    pygame.display.flip()
                if SHOW_LINE_TIMINGS:
                    print("Line: " + str(line_profiler.get_seconds()))
                    line_profiler = profiler.Profiler()

    pygame.display.flip()

    if SHOW_FRAME_TIMINGS:
        print("Frame: " + str(frame_profiler.get_seconds()))
        frame_profiler = profiler.Profiler()

    if SAVE_IMAGES:
        pygame.image.save(screen, f"img{image_idx:04}.png" )
        image_idx += 1

    # Apply velocity to points
    for point in points:
        point[0][0] += point[2][0]
        point[0][1] += point[2][1]
