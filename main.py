import pygame
import snake as sn
import settings as stg
import fruit as fr
import title as ttl
import time


# A function for the title
def title(screen):
    while True:
        screen.fill(stg.BLACK)
        pygame.event.get()

        if stg.isHighScore:
            ttl.highScore(screen, pygame.mouse.get_pos())

        else:
            ttl.draw(screen)

            if not ttl.react(pygame.mouse.get_pos()):
                break


def main():
    # Initializing all the important objects and modules
    pygame.init()

    pygame.font.init()

    screen = pygame.display.set_mode((stg.SCREEN_W, stg.SCREEN_H))

    img = pygame.image.load(r'Resources\bg.png')

    pygame.display.set_caption(stg.TITLE)

    fps = pygame.time.Clock()

    snakehead = sn.Snake()

    fruits = fr.Fruit()

    run = True

    start = 0

    # The game's main loop
    while run:
        # Runs the title screen
        if stg.isTitle:
            screen.fill(stg.BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            title(screen)

        else:
            # Starts recording the time
            if stg.startTime:
                start = time.time()
                stg.startTime = False

            # Draws all the necessary objects
            screen.blit(img, (-50, -50))
            fruits.draw(screen)
            snakehead.update(screen)

            # Checks pygame events and runs the direction update when a key is pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                elif event.type == pygame.KEYDOWN:
                    snakehead.direction_update()

            # Checks for a collision; if the user lost
            if snakehead.checkCollision() == 1:
                stg.isSorted = False
                end = time.time()
                stg.isTitle = True
                stg.startTime = True

                # Opens and writes to the high_score text file
                with open('high_score.txt', 'a') as f:
                    f.write('Score: {} Time: {}s\n'.format(snakehead.length, round(end - start)))

                # Adds the newest line to the scores_list
                with open('high_score.txt', 'r') as f:
                    stg.scores_list = f.readlines()

                snakehead = sn.Snake()
                fruits = fr.Fruit()

            # If the snakehead is equal to the fruits position
            if snakehead.move(fruits.pos):
                fruits = fr.Fruit()

            pygame.display.update()
            pygame.display.set_caption("Snake | Score: " + str(snakehead.length))
            fps.tick(20)

    pygame.quit()


main()
