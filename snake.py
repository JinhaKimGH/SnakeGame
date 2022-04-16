import settings as stg
import pygame

class Snake:
    def __init__(self):
        self.x = stg.SCREEN_W//2
        self.y = stg.SCREEN_H//2
        self.direction = None
        self.next = None
        self.length = 1
        self.just_ate = False

    def update(self):
        self.pos_update()
        self.draw()

    def draw(self, screen=stg.screen):
        temp_node = self
        while temp_node != None:
            print(1)
            rect = pygame.Rect(temp_node.x, temp_node.y, 1, 1)
            #pygame.draw.rect(screen, stg.snake_skin, rect, 2)
            print(2)
            temp_node = temp_node.next

        temp_node = None

    def pos_update(self):
        temp_node = self
        hold_x = temp_node.x
        hold_y = temp_node.y

        while temp_node.next != None:
            temp_node.next.x, hold_x = hold_x, temp_node.next.x
            temp_node.next.y, hold_y = hold_y, temp_node.next.y

            temp_node = temp_node.next

        if (self.direction == "LEFT") and (self.x < stg.SCREEN_W):
            self.x += 1

        elif (self.direction == "RIGHT") and (self.x > 0):
            self.x -= 1

        elif (self.direction == "DOWN") and (self.y < stg.SCREEN_H):
            self.y += 1

        elif (self.direction == "UP") and (self.y > 0):
            self.y -= 1

        else:
            pygame.quit()

    def direction_update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.direction = "LEFT"

        elif key[pygame.K_RIGHT]:
            self.direction = "RIGHT"

        elif key[pygame.K_UP]:
            self.direction = "UP"

        elif key[pygame.K_DOWN]:
            self.direction = "DOWN"

    def add_part(self):
        if self.just_ate == True:
            temp = self
            self.pos_update()
            self.next = temp
            self.just_ate = False
