# This code generates a voronoi diagram by making use of multiple CPU cores at the same time
# Unlike voronoi_multiprocessing.py, where worker functions must add their results to a multiprocessing queue, this
# one uses a multiprocessing pool, which represents a group of processes which the work is automatically spread
# between. The pool.map function is used to initiate the work and returns a list of results.
# Unlike the other one, in this we only proceed to drawing once all results have been calculated

# Need help understanding computer science and programming?
# Arganoid Tuition - https://tutor.arganoid.com/

import sys, random
from multiprocessing import Pool
from profiler import Profiler

# import pygame has been moved to if __name__ == '__main__' - this avoids having the pygame welcome message appear
# for each new process. Moving the other imports to that section does not appear to improve performance

# Extra debug logs for multiprocessing, you can uncomment these lines to see more details when new processes are
# created
# from multiprocessing import log_to_stderr
# import logging
# logger = log_to_stderr(logging.DEBUG)

# Settings
NUM_POINTS = 100
SCREEN_SIZE = (640, 480)
NUM_PROCESSES = 8
LINES_PER_PROCESS = 20
NUM_FRAMES = 100
SHOW_LINE_BY_LINE = True
SHOW_FRAME_TIMINGS = True
SAVE_IMAGES = False

WHITE = (255, 255, 255)

random.seed(2)

def lines(args):
    py_range = args[0]
    points = args[1]
    results = []
    for py in py_range:
        line = []
        for px in range(0, SCREEN_SIZE[0]):
            best_dist = 1e999
            for point in points:
                dist_sq = (px - point[0][0]) ** 2 + (py - point[0][1]) ** 2
                if dist_sq < best_dist:
                    nearest_point = point
                    best_dist = dist_sq
            line.append(nearest_point[1])
        results.append(line)

    return (py_range, results)


if __name__ == '__main__':
    import pygame
    import pygame.gfxdraw

    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)

    screen.fill(WHITE)

    points = []
    for i in range(0, NUM_POINTS):
        pos = [random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1])]
        col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        vel = (random.randrange(-1, 1), random.randrange(-1, 1))
        points.append((pos, col, vel))

    image_idx = 0

    frame_profiler = Profiler()

    for i in range(NUM_FRAMES):
        with Pool(processes=NUM_PROCESSES) as pool:
            all_lines = [(range(py, min(py+LINES_PER_PROCESS, SCREEN_SIZE[1])), points)
                         for py in range(0, SCREEN_SIZE[1], LINES_PER_PROCESS)]
            results = pool.map(lines, all_lines)

        #print("done all")

        lines_drawn = 0

        for item in results:
            py = item[0][0]     # 1st line of range
            for line in item[1]:
                for px in range(0, SCREEN_SIZE[0]):
                    pygame.gfxdraw.pixel(screen, px, py, line[px])

                if SHOW_LINE_BY_LINE:
                    pygame.display.flip()

                for event in pygame.event.get():  # User did something
                    if event.type == pygame.QUIT:  # If user clicked close
                        sys.exit()

                py += 1

            #print(f"drawn {item[0]}")

        pygame.display.flip()

        if SHOW_FRAME_TIMINGS:
            print("Frame: " + str(frame_profiler.get_seconds()))
            frame_profiler = Profiler()

        if SAVE_IMAGES:
            pygame.image.save(screen, f"img{image_idx:04}.png")
            image_idx += 1

        # Apply velocity to points
        for point in points:
            point[0][0] += point[2][0]
            point[0][1] += point[2][1]
