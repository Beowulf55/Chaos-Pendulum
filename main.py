import pygame
import os
import math
import random
from points import *
import formular

os.environ['SDL_VIDEO_CENTERED']='1'

width, height = 1024, 768
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Chaos Pendulum")
fps = 30
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#colors
white = (255, 255 , 255)
black = (0, 0, 0)

mass1 = 50
mass2 = 50
length1 = 200
length2 = 200

angle1 = math.pi/2
angle2 = math.pi/2
angle_velocity1 = 0
angle_velocity2 = 0
angle_acceleration1 = 0
angle_acceleration2 = 0
Gravity = 3
scatter1 = []
scatter2 = []


starting_point = (int(width/2) , int(height/4))

x_offset = starting_point[0]
y_offset = starting_point[1]

run = True

while run:
    clock.tick(fps)

    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # calculate the acceleration
    angle_acceleration1 = formular.FirstAcceleration(angle1, angle2, mass1, mass2, length1, length2, Gravity, angle_velocity1, angle_velocity2)
    angle_acceleration2 = formular.SecondAcceleration(angle1, angle2, mass1, mass2, length1, length2, Gravity, angle_velocity1, angle_velocity2)

    x1 = float((length1) * math.sin(angle1) + x_offset)
    y1 = float((length1) * math.cos(angle1) + y_offset)

    x2 = float(x1 + length2 * math.sin(angle2))
    y2 = float(y1 + length2 * math.cos(angle2))

    #time evolution of angle and angular velocity
    angle_velocity1 += angle_acceleration1
    angle_velocity2 += angle_acceleration2
    angle1 += angle_velocity1
    angle2 += angle_velocity2

    #scatter1.append((x1, y1))
    #scatter2.append((x2, y2))
    #these scatters typically bog the built-in rendering engine down, leaving them disabled improves performance

    for point in scatter2:
        random_color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        plot = Points(point[0], point[1], screen, white, scatter2)
        plot.draw()

    pygame.draw.line(screen, white, starting_point, (x1, y1), 6)


    pygame.draw.line(screen, white, (x1, y1), (x2, y2), 1)
    pygame.draw.circle(screen, white, (int(x2), int(y2)), 15)
    pygame.draw.circle(screen, (20, 200, 30), (int(x1), int(y1)), 15)
    if len(scatter1) > 1:
        pygame.draw.lines(screen, (100, 50, 100), False, scatter1, 1)
    pygame.display.update()

pygame.quit()
