import pygame
import time

from random import randint
from pygame.locals import *

import pyaudio
import struct
import matplotlib.pyplot as plt
import numpy as np

from OpenGL.GLU import *
from OpenGL.GL import *


# Load the music to pygame player and play it
file = 'niimmuutelowimp.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

# Create empty lists for vertexes for network effect
vertex_list = []
vertex_list2 = []

# Create the nodes as vertices for the network effect
for itema in range(15):
    for itemb in range(8):
        coordinate = (randint(-100, 100), randint(-100, 100), randint (-100, 100))
        vertex_list.append(coordinate)
        coordinate = (randint(-200, 200), randint(-200, 200), randint(-200, 200))
        vertex_list2.append(coordinate)

for item in vertex_list:
    print(item)

# Create empty list for the edges between the nodes of the network effect
edge_list = []

# Create the edges as coordinate pairs for the network effect
for items in range(15):
    for item in range(8):
        pair = (items, item)
        edge_list.append(pair)

# Create the nodes as vertices for the second network effect
vertices_plane = (vertex_list)
vertices_plane2 = (vertex_list2)

# Create a variable for the edges to be used later
edges_plane = (
    edge_list
)

# Create the vertices for cool diamond thingy
vertices_cube = (
    # Tip vertices
    (0, 1, 0),

    # Bottom vertices
    (-0.5, -1, 1),
    (0.5, -1, 1),
    (-1, -1, 0),
    (1, -1, 0),
    (0, -1, -1),

    # Other tip vertices
    (0, -2, 0)
)

# Create the edges for the cool diamond thingy
edges_cube = (
    # Edges from tip
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),

    # Edges on base
    (1, 2),
    (1, 3),
    (3, 5),
    (5, 4),
    (4, 2),

    (1, 5),
    (5, 2),
    (2, 3),
    (3, 4),
    (4, 1),

    (6, 1),
    (6, 2),
    (6, 3),
    (6, 4),
    (6, 5)
)


# Create the vertices for the grid here
# X and Y dimensions of the grid
GRID_X = 200
GRID_Y = 200

# Create a list that includes the grid coordinates / vertices as tuples
vertices_grid = []
for i in range(GRID_X):
    for a in range(GRID_Y):
        temp_str = ()
        temp_str = temp_str + (i, 0, a)
        vertices_grid.append(temp_str)

# Create a list that includes the grid edges / lines as coordinate pairs

# Y-axis lines / edges pair coordinates
edges_grid = []
for i in range (GRID_X * GRID_Y):
    if i % GRID_X == 0:
        edge = (i, i + GRID_X - 1)
        edges_grid.append(edge)

# X-axis lines / edges pair coordinates
for i in range (GRID_X):
    edge = (i, ((GRID_X * GRID_Y) - (GRID_X - i)))

    edges_grid.append(edge)

# Print some grid vertices and edges for debugging
print(edges_grid)
print(vertices_grid)

# Each element / object have their own function that can be called for
# drawing

def Cube():
    glBegin(GL_LINES)
    for edge in edges_cube:
        for vertex in edge:
            glVertex3fv(vertices_cube[vertex])
            glColor3fv((0, 255, 255))
    glEnd()

def plane():
    glBegin(GL_LINES)

    for edge in edges_plane:
        for vertex in edge:
            glVertex3fv(vertices_plane[vertex])
            glColor3fv((255, 0, 0))
    glEnd()

def plane2():
    glBegin(GL_LINES)

    for edge in edges_plane:
        for vertex in edge:
            glVertex3fv(vertices_plane2[vertex])
            glColor3fv((0, 0, 255))
    glEnd()

def grid():
    glBegin(GL_LINES)

    for edge in edges_grid:
        for vertex in edge:
            glVertex3fv(vertices_grid[vertex])
            glColor3fv((255, 0, 0))

    glEnd()

# Here's just a function to produce a semirandom integer
def random_integer(high, low):
    randomizer = randint(high, low)
    return randomizer

# Listener for the microphone and its definitions
CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
)
fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))

ax.set_ylim(-255, 255)
ax.set_xlim(0, CHUNK)
#plt.show(block=False)

# Octagonal tunnel effect is defined here
# octQ = quantity of iterations
# OOXYZ = coordinates for the first iteration
octQ = 200
OOX = 0
OOY = 0
OOZ = 0

octVertices = []

for i in range(octQ):

    vertices_octagon = (
        (OOX, OOY + 11, OOZ),
        (OOX + 8, OOY + 8, OOZ),

        (OOX + 11, OOY, OOZ),
        (OOX + 8, OOY - 8, OOZ),

        (OOX, OOY - 11, OOZ),
        (OOX - 8, OOY - 8, OOZ),

        (OOX - 11, OOY, OOZ),
        (OOX - 8, OOY + 8, OOZ)
    )

    octVertices.append(vertices_octagon)

    i += 1
    OOZ -= 0.05

octVertices = [xx for yy in octVertices for xx in yy]

first_vertex = 0
second_vertex = 1
octEdgeList = []

for verticeList in octVertices:
    for item in verticeList:
        vertexPair = (first_vertex, second_vertex)
        octEdgeList.append(vertexPair)
        first_vertex += 1
        second_vertex += 1

def octagon():
    glBegin(GL_LINES)
    i = 0

    for edge in octEdgeList:

        for vertex in edge:
            while i <= len(octVertices)-1:

                glVertex3fv(octVertices[i])
                glColor3fv((255, 0, 0))
                i += 1

    glEnd()


# Define the duration in seconds for each scene here

SCENE_DURATION_PYRAMID = 29
SCENE_DURATION_TUNNEL = 59
SCENE_DURATION_GRID = 19.5
SCENE_DURATION_NETWORK = 39
SCENE_DURATION_GRID2 = 19
SCENE_DURATION_OCTAGON2 = 58
SCENE_DURATION_NETWORK2 = 41
SCENE_DURATION_CUBE2 = 27

# Main function obviously here
# All the scenes are here as ugly spaghetti
# I will probably not explain the scenes in the main function.
# If I have the time, I will, but i probably won't so glhf reading it.

def main():
    pygame.init()

    pygame.mouse.set_visible(False)

    display = (1920, 1080)
    screen = pygame.display.set_mode(display, DOUBLEBUF | pygame.OPENGLBLIT| pygame.FULLSCREEN)

    # SCENE 1 START HERE Pyramid 1

    gluPerspective(165, (display[0] / display[1]), 0.1, 200)
    glTranslatef(-4, -1, -1.6)
    glRotatef(0, 0, 0, 0)

    time_start = time.time()
    timer = 0
    clearer = 0
    #while timer <= 29: <-- real deal

    while timer <= SCENE_DURATION_PYRAMID:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return

        glTranslatef(0, 0, 0)
        glRotatef(0.5, -0.2, 5, 0)

        timer = int(time.time() - time_start)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        data = stream.read(CHUNK)
        data_int = np.array(struct.unpack(str(2 * CHUNK) + "B", data),
                            dtype="b")[::2] + 0

        line.set_ydata(data_int)

        fig.canvas.draw()
        fig.canvas.flush_events()

        Cube()

        if sum(data_int)/4096 > 1.5:

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            Cube()

        pygame.display.flip()
        pygame.time.wait(30)

    # SCENE 2 Tunnel / Octagon 1
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(178, (display[0]/display[1]), 0, 2)
    glTranslatef(0, 0, -0.2)
    glRotatef(0, 0, 0, 0)

    time_start = time.time()
    timer = 0
    clearer = 0

    while timer <= SCENE_DURATION_TUNNEL:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return


        glRotatef(1, 0, 0.01, 0.1)
        glTranslate(0, 0, 0.02)

        timer = int(time.time() - time_start)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        data = stream.read(CHUNK)
        data_int = np.array(struct.unpack(str(2 * CHUNK) + "B", data),
                            dtype="b")[::2] + 0

        line.set_ydata(data_int)

        fig.canvas.draw()
        fig.canvas.flush_events()

        octagon()

        if sum(data_int)/4096 > 1.5:

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            octagon()


        pygame.display.flip()
        pygame.time.wait(30)

    # SCENE 3 / Grid 1
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(165, (display[0]/display[1]), 0, 2)

    time_start = time.time()
    timer = 0
    glTranslatef(-8, -1, -5)
    glRotatef(0, 0, 0, 0)

    while timer <= SCENE_DURATION_GRID:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return

        glRotatef(0, 0, 0, 0)
        glTranslatef(-0.1, 0, 0)

        timer = int(time.time() - time_start)

        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        grid()


        if random_integer(1, 7) != 1:

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            grid()

        clearer += 1

        grid()

        pygame.display.flip()
        pygame.time.wait(30)

    # SCENE 4 / Network 1
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(165, (display[0]/display[1]), 0, 2)

    time_start = time.time()
    timer = 0
    glTranslatef(0, 0, -5)

    while timer <= SCENE_DURATION_NETWORK:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return

        glRotatef(1, 1, 0, 0)
        glTranslatef(0, 0, 0.5)

        timer = int(time.time() - time_start)

        #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        data = stream.read(CHUNK)
        data_int = np.array(struct.unpack(str(2 * CHUNK) + "B", data),
                            dtype="b")[::2] + 0

        line.set_ydata(data_int)

        fig.canvas.draw()
        fig.canvas.flush_events()

        plane()

        if sum(data_int)/4096 > -1:

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            plane()

        plane()

        pygame.display.flip()
        pygame.time.wait(30)

    time_start = time.time()
    timer = 0

    # SCENE 5 / Grid 2
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(179, (display[0]/display[1]), 0, 100)

    time_start = time.time()
    timer = 0
    glTranslatef(-72, 8, -0.02)
    glRotatef(90.4, 1, 0, 0)

    while timer <= SCENE_DURATION_GRID2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return

        glRotatef(-0.0001, 0.0001, 0, 0)
        glTranslatef(-0.02, 0, 0)

        timer = int(time.time() - time_start)

        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        grid()


        if random_integer(1, 7) != 1:

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            grid()

        clearer += 1
        grid()

        pygame.display.flip()
        pygame.time.wait(30)

    # SCENE 6 / Octagon 2

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(165, (display[0]/display[1]), 0, 2)
    glTranslatef(0, 0, -4)
    glRotatef(0, 0, 0, 0)

    time_start = time.time()
    timer = 0
    clearer = 0
    # while timer <= 29: <-- real deal

    while timer <= SCENE_DURATION_OCTAGON2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return


        glRotatef(2, 0, -0.05, 0.1)
        glTranslate(0, 0, 0.03)

        timer = int(time.time() - time_start)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        data = stream.read(CHUNK)
        data_int = np.array(struct.unpack(str(2 * CHUNK) + "B", data),
                            dtype="b")[::2] + 0

        line.set_ydata(data_int)

        fig.canvas.draw()
        fig.canvas.flush_events()

        octagon()

        if sum(data_int)/4096 > 1.5:

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            octagon()

        pygame.display.flip()
        pygame.time.wait(30)

    # SCENE 7 / Network 2
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(165, (display[0] / display[1]), 0, 2)

    time_start = time.time()
    timer = 0
    glTranslatef(0, 0, -5)

    while timer <= SCENE_DURATION_NETWORK2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return

        glRotatef(1, 1, 0, 0)
        glTranslatef(0, 0, 0.5)

        timer = int(time.time() - time_start)

        # glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        data = stream.read(CHUNK)
        data_int = np.array(struct.unpack(str(2 * CHUNK) + "B", data),
                            dtype="b")[::2] + 0

        line.set_ydata(data_int)

        fig.canvas.draw()
        fig.canvas.flush_events()

        plane()

        if sum(data_int) / 4096 > -1:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            plane()

        plane()

        pygame.display.flip()
        pygame.time.wait(30)

    # SCENE 8 / Pyramid 2
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(135, (display[0]/display[1]), 0, 2)

    glTranslatef(3, -1, -2.3)
    glRotatef(0, 0, 0, 0)

    time_start = time.time()
    timer = 0
    clearer = 0

    while timer <= SCENE_DURATION_CUBE2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return

        glTranslatef(0, 0, 0)
        glRotatef(0.5, -0.2, 5, 0)

        timer = int(time.time() - time_start)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        data = stream.read(CHUNK)
        data_int = np.array(struct.unpack(str(2 * CHUNK) + "B", data),
                            dtype="b")[::2] + 0

        line.set_ydata(data_int)

        fig.canvas.draw()
        fig.canvas.flush_events()

        Cube()

        if sum(data_int)/4096 > 1.5:

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            Cube()

        pygame.display.flip()
        pygame.time.wait(30)

main()