from snake import *
import random


class Fruit:
    # Initializes an object of the Fruit class
    def __init__(self):
        self.pos = [(random.randint(2, stg.SCREEN_W//stg.SNAKE_SPEED) * stg.SNAKE_SPEED) - stg.SNAKE_SPEED,
                    (random.randint(2, stg.SCREEN_H//stg.SNAKE_SPEED) * stg.SNAKE_SPEED) - stg.SNAKE_SPEED]
        self.eaten = False
        self.image = pygame.image.load(r'Resources\PixelApple.png')
        self.small_img = pygame.transform.scale(self.image, (stg.SNAKE_SIZE, stg.SNAKE_SIZE))

    # Draws the fruit to the screen
    def draw(self, screen):
        screen.blit(self.small_img, (self.pos[0], self.pos[1]))
