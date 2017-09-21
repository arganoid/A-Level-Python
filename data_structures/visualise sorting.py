import random
import sys
import time

import pygame
import data_structures.sorting as sorting

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

def get_text_surfaces(list):
    textSurfaces = []
    for i in range(0, len(list)):
        textSurface = font.render(str(list[i]), False, BLACK)
        textSurfaces.append(textSurface)
    return textSurfaces

def get_positions(list, textSurfaces):
    positions = []
    x = 100
    y = 10
    for i in range(0, len(list)):
        positions.append((x,y))
        y += textSurfaces[i].get_height() + 5
        if y > screen_size[1]:
            y -= screen_size[1]
            x += 50
    return positions

def pygame_display_list(list, current_index, positions_override = None):

    textSurfaces = get_text_surfaces(list)
    positions = positions_override if positions_override != None else get_positions(list, textSurfaces)

    screen.fill(WHITE)

    for i in range(0,len(list)):
        x = positions[i][0]
        y = positions[i][1]
        textSurface = textSurfaces[i]

        screen.blit(textSurface, [int(x - textSurface.get_width() / 2), int(y)])

        if i == current_index:
            pygame.draw.rect(screen, BLUE, pygame.rect.Rect(x - 40, y, 20, textSurface.get_height() * 1))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            sys.exit()

    time.sleep(1)

def lerp( pos0, pos1, t ):
    x = (pos1[0] - pos0[0]) * t + pos0[0]
    y = (pos1[1] - pos0[1]) * t + pos0[1]
    return (x,y)


def swap_animation(list, swap1, swap2):

    textSurfaces = get_text_surfaces(list)
    positions = get_positions(list, textSurfaces)

    swap_progress = 0

    clock.tick(60)

    while swap_progress < 1:
        delta_time = clock.tick(60) / 1000

        swap_progress += delta_time * 1


        screen.fill(WHITE)

        for i in range(0,len(list)):
            x = positions[i][0]
            y = positions[i][1]
            textSurface = textSurfaces[i]

            if (i == swap1 or i == swap2) and swap1 != swap2:
                if i == swap1:
                    pos = lerp(positions[swap1], positions[swap2], swap_progress)
                else:
                    pos = lerp(positions[swap2], positions[swap1], swap_progress)
                x = pos[0]
                y = pos[1]

            screen.blit(textSurface, [int(x - textSurface.get_width() / 2), int(y)])

            #if i == current_index:
            #    pygame.draw.rect(screen, BLUE, pygame.rect.Rect(x - 40, y, 20, textSurface.get_height() * 2))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                sys.exit()


def test():
    if True:
        my_list = [5,1,2,9,8,6,4,3,5,0,7,3,1,4]
    else:
        my_list = []
        for i in range(0,100):
            my_list.append(random.randint(0,9))
    #sorting.bubble_sort(my_list, pygame_display_list, swap_animation)
    #sorting.insertion_sort(my_list, pygame_display_list, swap_animation)
    sorting.merge_sort(my_list,0,len(my_list)-1, pygame_display_list)
    #sorting.quick_sort(my_list, 0, len(my_list) - 1, pygame_display_list, swap_animation)
    time.sleep(3)

test()
