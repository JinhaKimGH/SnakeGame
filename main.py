import pygame
import snake as sn
import settings as stg
import fruit as fr
import random
import title as ttl

def title(screen):

    pygame.font.init()

    while True:
        screen.fill(stg.BLACK)

        ttl.draw(screen)

        if not ttl.react(pygame.mouse.get_pos()):
            break


def main():
    pygame.init()

    screen = pygame.display.set_mode((stg.SCREEN_W, stg.SCREEN_H))

    pygame.display.set_caption(stg.TITLE)

    fps = pygame.time.Clock()

    snakehead = sn.Snake()

    fruits = fr.Fruit()

    run = True

    while run:
        screen.fill(stg.BLACK)
        if stg.isTitle:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            title(screen)

        elif stg.isEndScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break


        else:
            fruits.draw(screen)
            snakehead.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                elif event.type == pygame.KEYDOWN:
                    snakehead.direction_update()

            if (snakehead.checkCollision() == 1):
                run = False
                #stg.isEndScreen = True

            if (snakehead.move(fruits.pos)):
                fruits.pos = [random.randint(1, stg.SCREEN_W//stg.SNAKE_SPEED) * stg.SNAKE_SPEED, random.randint(1, stg.SCREEN_H//stg.SNAKE_SPEED)]

            pygame.display.update()
            pygame.display.set_caption("Snake | Score: " + str(snakehead.length))
            fps.tick(25)


    pygame.quit()

main()
