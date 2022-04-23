import settings as stg
import pygame
import random

class Snake:
    def __init__(self, x=stg.SCREEN_W//stg.SNAKE_SPEED, y=stg.SCREEN_H//stg.SNAKE_SPEED):
        self.position = [x, y]
        self.direction = None
        self.body = [[x, y]]
        self.length = 1
        self.just_ate = False
        self.head_img = pygame.transform.scale(pygame.image.load(r'Resources\snakehead.png'), (stg.SNAKE_SIZE,
                                                                                               stg.SNAKE_SIZE))
        self.last_dir = "DOWN"

    def update(self, screen):
        self.direction_update()
        self.draw(screen)

    def draw(self, screen):
        first = True

        for pos in self.body:
            if first:
                screen.blit(self.head_img, (pos[0], pos[1]))
                first = False

            else:
                rect = pygame.Rect(pos[0], pos[1], stg.SNAKE_SIZE, stg.SNAKE_SIZE)
                pygame.draw.rect(screen, stg.snake_skin, rect)

    def move(self, foodPos):
        if self.direction == "RIGHT":
            self.position[0] = self.position[0] + stg.SNAKE_SPEED
        elif self.direction == "LEFT":
            self.position[0] = self.position[0] - stg.SNAKE_SPEED
        elif self.direction == "UP":
            self.position[1] = self.position[1] - stg.SNAKE_SPEED
        elif self.direction == "DOWN":
            self.position[1] = self.position[1] + stg.SNAKE_SPEED
        self.body.insert(0, list(self.position))

        if (foodPos[0] - stg.SNAKE_SPEED//2 <= self.position[0] <= foodPos[0] + stg.SNAKE_SPEED//2) and \
                (foodPos[1] - stg.SNAKE_SPEED//2 <= self.position[1] <= foodPos[1] + stg.SNAKE_SPEED//2):
            self.length += 1
            return 1
        else:
            self.body.pop()
            return 0

    def direction_update(self):
        key = pygame.key.get_pressed()
        if self.direction != None:
            self.last_dir = self.direction

        if key[pygame.K_LEFT] and self.direction != "RIGHT":
            self.direction = "LEFT"

        elif key[pygame.K_RIGHT] and self.direction != "LEFT":
            self.direction = "RIGHT"

        elif key[pygame.K_UP] and self.direction != "DOWN":
            self.direction = "UP"

        elif key[pygame.K_DOWN] and self.direction != "UP":
            self.direction = "DOWN"

        self.rotate_head()


    def rotate_head(self):
        if self.last_dir == "RIGHT" and self.direction == "UP":
            self.head_img = pygame.transform.rotate(self.head_img, 90)

        elif self.last_dir == "RIGHT" and self.direction == "DOWN":
            self.head_img = pygame.transform.rotate(self.head_img, 270)

        elif self.last_dir == "LEFT" and self.direction == "UP":
            self.head_img = pygame.transform.rotate(self.head_img, 270)

        elif self.last_dir == "LEFT" and self.direction == "DOWN":
            self.head_img = pygame.transform.rotate(self.head_img, 90)

        elif self.last_dir == "UP" and self.direction == "RIGHT":
            self.head_img = pygame.transform.rotate(self.head_img, 270)

        elif self.last_dir == "UP" and self.direction == "LEFT":
            self.head_img = pygame.transform.rotate(self.head_img, 90)

        elif self.last_dir == "DOWN" and self.direction == "RIGHT":
            self.head_img = pygame.transform.rotate(self.head_img, 90)

        elif self.last_dir == "DOWN" and self.direction == "LEFT":
            self.head_img = pygame.transform.rotate(self.head_img, 270)

        elif self.last_dir == "DOWN" and self.direction == "UP":
            self.head_img = pygame.transform.rotate(self.head_img, 180)

    def checkCollision(self):
        if self.position[0] > stg.SCREEN_W - stg.SNAKE_SIZE or self.position[0] < stg.SNAKE_SIZE:
            return 1
        elif self.position[1] > stg.SCREEN_H or self.position[1] < stg.SNAKE_SIZE:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        return 0

