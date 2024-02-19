# Need help understanding computer science and programming?
# Arganoid Tuition - https://tutor.arganoid.com/

# This code generates a voronoi diagram by making use of multiple CPU cores at the same time

import sys, random
from multiprocessing import Process, Queue
from profiler import Profiler
from queue import Empty

# import pygame has been moved to if __name__ == '__main__' - this avoids having the pygame welcome message appear
# for each new process. Moving the other imports to that section does not appear to improve performance

# Extra debug logs for multiprocessing, you can uncomment these lines to see more details when new processes are
# created
# from multiprocessing import log_to_stderr
# import logging
# logger = log_to_stderr(logging.DEBUG)

# Settings
NUM_POINTS = 1000
SCREEN_SIZE = (640, 480)
LINES_PER_PROCESS = 80
NUM_FRAMES = 100
SHOW_LINE_BY_LINE = True
SHOW_FRAME_TIMINGS = True
SAVE_IMAGES = False

WHITE = (255, 255, 255)

random.seed(2)

# The lines function is called on multiple processes. It receives:
# points: a set of points for the voronoi diagram
# py_range: a range object of lines (py = pixel y) that this process should calculate
# Q: a multiprocessing queue to add the results to
# w: window width
def lines(points, py_range, Q, w):
    #print(f"begin {py_range}")
    # sys.stdout.flush()
    for py in py_range:
        result = []
        for px in range(0, w):
            best_dist = 1e999
            for point in points:
                dist_sq = (px - point[0][0]) ** 2 + (py - point[0][1]) ** 2
                if dist_sq < best_dist:
                    nearest_point = point
                    best_dist = dist_sq

            result.append(nearest_point[1])

        Q.put((py, result))

    Q.close() # necessary? Called automatically when current process is garbage collected

    #print(f"done {py_range}")


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

    Q = Queue()

    for i in range(NUM_FRAMES):
        # Spawn processes for calculating the chunks of the voronoi diagram, each process will run the lines function
        # with the given arguments
        for py in range(0, SCREEN_SIZE[1], LINES_PER_PROCESS):
            ##print(f"spawn {py}")
            p = Process(target=lines, args=(points, range(py, min(py+LINES_PER_PROCESS, SCREEN_SIZE[1])), Q, SCREEN_SIZE[0]))
            p.start()

        #print("started all")

        lines_drawn = 0

        def draw():
            global lines_drawn
            # From https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue
            # "empty(): Returns True if the queue is empty, False otherwise. However, because of
            # multithreading/multiprocessing semantics, this is not reliable"
            # Another process could be adding to the queue or removing from the queue at the same time that we ask
            # if the queue is empty. Therefore we can't rely on the answer empty provides. The exception handler below
            # deals with the case where the queue is reported as not empty but there is no item to be found
            while not Q.empty():
                try:
                    item = Q.get()
                    for px in range(0, SCREEN_SIZE[0]):
                        pygame.gfxdraw.pixel(screen, px, item[0], item[1][px])

                    if SHOW_LINE_BY_LINE:
                        pygame.display.flip()

                    for event in pygame.event.get():  # User did something
                        if event.type == pygame.QUIT:  # If user clicked close
                            sys.exit()

                    #print(f"drawn {item[0]}")

                    lines_drawn += 1
                except Empty:
                    print("Queue empty")

        # Keep going until we've drawn all lines
        while lines_drawn < SCREEN_SIZE[1]:
            draw()

        #print("joined all")

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

