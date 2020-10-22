import pygame
from settings import *
from colors import *


pygame.init()

display = pygame.display.set_mode((WIDTH, HEIGHT))

stop = False

clock = pygame.time.Clock()

while not stop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    pygame.display.flip()

    display.fill(BLACK)

    clock.tick(FPS)
