import math
import sys
import random

import data_structures.graph as graph
import pygame


def get_distance(x1, y1, x2, y2):
    difference_x = x2 - x1
    difference_y = y2 - y1
    return math.sqrt(difference_x * difference_x + difference_y * difference_y)


my_graph = graph.GetTestGraph()


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

screen_size = (1250,650)
screen = pygame.display.set_mode(screen_size)

node_positions = {}
for node in my_graph.adjacency_list:
    node_positions[node] = [random.randint(20,screen_size[0]-20), random.randint(20,screen_size[1]-20)]

pygame.init()

font = pygame.font.Font(None, 30)

dragging_node = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            sys.exit()

    screen.fill(WHITE)

    if dragging_node == None:
        if pygame.mouse.get_pressed()[0]:
            nearest_distance = 1e9
            nearest_node = None
            mouse_pos = pygame.mouse.get_pos()
            for node in my_graph.adjacency_list:
                node_pos = node_positions[node]
                distance = get_distance(node_pos[0], node_pos[1], mouse_pos[0], mouse_pos[1])
                if distance < nearest_distance:
                    nearest_node = node
                    nearest_distance = distance
            dragging_node = nearest_node
    else:
        if pygame.mouse.get_pressed()[0]:
            node_positions[dragging_node] = pygame.mouse.get_pos()
        else:
            dragging_node = None



    for node in my_graph.adjacency_list:

        node_adjacency_list = my_graph.adjacency_list[node]
        for adjacent_node in node_adjacency_list:
            pygame.draw.line(screen, BLACK, node_positions[node], node_positions[adjacent_node], 1)

        pygame.draw.circle(screen, BLACK, node_positions[node], 30, 1 )

        textSurface = font.render(str(node), False, BLACK)
        #screen.blit(textSurface, node_positions[node])
        x = node_positions[node][0]
        y = node_positions[node][1]
        screen.blit(textSurface, [int(x - textSurface.get_width() / 2), int(y - textSurface.get_height() / 2)])

    pygame.display.flip()




