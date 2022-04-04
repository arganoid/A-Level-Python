# Need help understanding computer science and programming?
# Arganoid Tuition - https://tutor.arganoid.com/

import sys, random
from multiprocessing import Process, current_process, Queue
from profiler import Profiler

# import pygame has been moved to if __name__ == '__main__' - this avoids having the pygame welcome message appear
# for each new process. Moving the other imports to that section does not appear to improve performance

# Extra debug logs for multiprocessing, you can uncomment these lines to see more details when new processes are
# created
#from multiprocessing import log_to_stderr
#import logging
#logger = log_to_stderr(logging.INFO)

# Settings
NUM_POINTS = 100
SCREEN_SIZE = (100, 100)
NUM_FRAMES = 1
SHOW_LINE_BY_LINE = True
SHOW_FRAME_TIMINGS = True
SAVE_IMAGES = False

WHITE = (255, 255, 255)

random.seed(2)

def line(points, py, Q, w):
    print(f"begin {py}")
    # sys.stdout.flush()
    result = []
    for px in range(0, w):
        # timings: 720p, 1000 points

        # 1.6s per line
        # nearest_point = sorted(points, key=lambda p: ((px-p[0][0]) ** 2 + (py-p[0][1]) ** 2))[0]

        # 2.6s per line
        # def closer(p1,p2):
        #     return p1 if ((px - p1[0][0]) ** 2 + (py - p1[0][1]) ** 2) < ((px - p2[0][0]) ** 2 + (py - p2[0][1]) ** 2) else p2
        # nearest_point = functools.reduce( closer, points, ((1e9,1e9),) )

        # 1.45s per line
        best_dist = 1e999
        for point in points:
            dist_sq = (px - point[0][0]) ** 2 + (py - point[0][1]) ** 2
            if dist_sq < best_dist:
                nearest_point = point
                best_dist = dist_sq

        result.append(nearest_point[1])

    Q.put((py, result))


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
        for py in range(0, SCREEN_SIZE[1]):
            print(f"spawn {py}")
            p = Process(target=line, args=(points, py, Q, SCREEN_SIZE[0]))
            p.start()
            processes.append(p)

        print("started all")

        def draw():
            while not Q.empty():
                item = Q.get()
                for px in range(0, SCREEN_SIZE[0]):
                    pygame.gfxdraw.pixel(screen, px, item[0], item[1][px])

                if SHOW_LINE_BY_LINE:
                    pygame.display.flip()

                print(f"done {item[0]}")

                for event in pygame.event.get():  # User did something
                    if event.type == pygame.QUIT:  # If user clicked close
                        sys.exit()

        for process in processes:
            print("join!")
            process.join()
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
