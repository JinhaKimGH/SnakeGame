from snake import *
from settings import *
import random


class Fruit:
    def __init__(self):
        self.pos = [random.randint(4, 21) * stg.SNAKE_SPEED, random.randint(3, 22) * stg.SNAKE_SPEED]
        self.eaten = False
        self.image = pygame.image.load(r'Resources\PixelApple.png')
        self.small_img = pygame.transform.scale(self.image, (stg.SNAKE_SIZE, stg.SNAKE_SIZE))

    def draw(self, screen):
        #rect = pygame.Rect(self.pos[0], self.pos[1], stg.SNAKE_SIZE, stg.SNAKE_SIZE)
        #pygame.draw.rect(screen, stg.RED, rect)
        screen.blit(self.small_img, (self.pos[0], self.pos[1]))