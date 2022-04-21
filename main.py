import pygame
import snake as sn
import settings as stg
import fruit as fr
import title as ttl
import time


def title(screen):
    pygame.font.init()

    while True:
        screen.fill(stg.BLACK)

        if stg.isHighScore:
            if ttl.highScore(screen):
                continue

            else:
                stg.isHighScore = False
                continue

        ttl.draw(screen)

        if not ttl.react(pygame.mouse.get_pos()):
            break

        else:
            stg.isHighScore = True

def main():
    pygame.init()

    screen = pygame.display.set_mode((stg.SCREEN_W, stg.SCREEN_H))

    pygame.display.set_caption(stg.TITLE)

    fps = pygame.time.Clock()

    snakehead = sn.Snake()

    fruits = fr.Fruit()

    run = True

    start = 0

    while run:
        screen.fill(stg.BLACK)
        if stg.isTitle:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            title(screen)

        else:
            if stg.startTime:
                start = time.time()
                stg.startTime = False

            fruits.draw(screen)
            snakehead.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                elif event.type == pygame.KEYDOWN:
                    snakehead.direction_update()

            if snakehead.checkCollision() == 1:
                end = time.time()
                stg.isTitle = True
                stg.startTime = True

                with open('high_score.txt', 'w') as f:
                    f.write('Score: {} Time: {}s\n'.format(snakehead.length, round(end - start)))

                snakehead = sn.Snake()
                fruits = fr.Fruit()

            if snakehead.move(fruits.pos):
                fruits = fr.Fruit()

            pygame.display.update()
            pygame.display.set_caption("Snake | Score: " + str(snakehead.length))
            fps.tick(15)

    pygame.quit()


main()
