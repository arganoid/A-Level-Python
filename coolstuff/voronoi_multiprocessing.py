# Need help understanding computer science and programming?
# Arganoid Tuition - https://tutor.arganoid.com/
import sys, random
from multiprocessing import Process, current_process, Queue
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
NUM_POINTS = 100
SCREEN_SIZE = (640, 480)
LINES_PER_PROCESS = 20
NUM_FRAMES = 1
SHOW_LINE_BY_LINE = True
SHOW_FRAME_TIMINGS = True
SAVE_IMAGES = False

WHITE = (255, 255, 255)

random.seed(2)

def lines(points, py_range, Q, w):
    print(f"begin {py_range}")
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

    print(f"done {py_range}")

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
        processes = []
        for py in range(0, SCREEN_SIZE[1], LINES_PER_PROCESS):
            print(f"spawn {py}")
            p = Process(target=lines, args=(points, range(py, min(py+LINES_PER_PROCESS, SCREEN_SIZE[1])), Q, SCREEN_SIZE[0]))
            p.start()
            processes.append(p)

        print("started all")

        count = 0

        def draw():
            global count
            while not Q.empty():    # Return True if the queue is empty, False otherwise. Because of multithreading/multiprocessing semantics, this is not reliable
                try:
                    item = Q.get()
                    for px in range(0, SCREEN_SIZE[0]):
                        pygame.gfxdraw.pixel(screen, px, item[0], item[1][px])

                    if SHOW_LINE_BY_LINE:
                        pygame.display.flip()

                    for event in pygame.event.get():  # User did something
                        if event.type == pygame.QUIT:  # If user clicked close
                            sys.exit()

                    print(f"drawn {item[0]}")

                    count += 1
                except Empty:
                    print("Queue empty")

        # No good - if you try to join a process which has added stuff to a multiprocessing queue, and the stuff has not been consumed, it may deadlock
        # for process in processes:
        #     print("join!")
        #     process.join()
        #     draw()

        while count < SCREEN_SIZE[1]:
            draw()

        print("joined all")

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

