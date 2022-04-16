from snake import *
from fruit import *
import pygame
import settings as stg

pygame.init()
pygame.display.init()
pygame.font.init()

run = True

snakehead = Snake()

while run:
    stg.screen.fill(stg.WHITE)
    snakehead.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            snakehead.direction_update()

    pygame.display.update()


pygame.quit()

