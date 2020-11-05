import pygame
import os
import math
import random
from points import *
import formular

os.environ['SDL_VIDEO_CENTERED']='1'

mass1 = 40
mass2 = 40
length1 = 175
length2 = 175

angle1 = math.pi/2
angle2 = math.pi/2
angle_velocity1 = 0
angle_velocity2 = 0
angle_acceleration1 = 0
angle_acceleration2 = 0
Gravity = 4 # system typically doesn't handle realistic gravity well; pendulum becomes unrealistically chaotic and .exe crashes
scatter1 = []
scatter2 = []

lblm1 = str(mass1)
lblm2 = str(mass2)
lblL1 = str(length1)
lblL2 = str(length2)
lblg = str(Gravity / 9.8)

width, height = 1280, 720
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Chaos Pendulum, mass1 = " + lblm1 + ", mass2 = " + lblm2 + ", length1 = " + lblL1 + ", length2 = " + lblL2 + ", Gravity = " + lblg + "g")
fps = 30
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#colors
white = (255, 255 , 255)
black = (0, 0, 0)

starting_point = (int(width/2) , int(height/4) + 100)

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
    pygame.draw.circle(screen, (0, 128.01, 128.01), (int(x2), int(y2)), 15)
    pygame.draw.circle(screen, (20, 200, 30), (int(x1), int(y1)), 15)
    if len(scatter1) > 1:
        pygame.draw.lines(screen, (100, 50, 100), False, scatter1, 1)
    pygame.display.update()

pygame.quit()
