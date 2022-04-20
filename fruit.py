from snake import *
from settings import *
import random

class Fruit:
    def __init__(self):
        self.pos = [random.randint(8, 42) * stg.SNAKE_SPEED, random.randint(6, 44) * stg.SNAKE_SPEED]
        self.eaten = False

    def draw(self, screen):
        rect = pygame.Rect(self.pos[0], self.pos[1], stg.SNAKE_SIZE, stg.SNAKE_SIZE)
        pygame.draw.rect(screen, stg.RED, rect)


