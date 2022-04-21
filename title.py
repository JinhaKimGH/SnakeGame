# Title Functions
import pygame
import settings as stg


def draw(screen):
    font = pygame.font.Font('freesansbold.ttf', stg.FONT_SIZE)
    title = pygame.font.Font('freesansbold.ttf', stg.titleFont)

    # Title
    caption = title.render('Snake', True, stg.WHITE)
    captionRect = caption.get_rect()
    captionRect.center = (stg.SCREEN_W // 2, stg.titleFont)
    title_bg = title.render('Snake', True, stg.PALE_WHITE)
    titleRect = title_bg.get_rect()
    titleRect.center = (stg.SCREEN_W // 2 + 4, stg.titleFont + 4)
    screen.blit(title_bg, titleRect)
    screen.blit(caption, captionRect)

    # Play button
    play = font.render('PLAY', True, stg.PLAY_HOVER)
    playRect = play.get_rect(center=(stg.SCREEN_W // 2, stg.SCREEN_H // 2))
    screen.blit(play, playRect)

    # High Scores Button
    highScore = font.render('HIGH SCORES', True, stg.HIGHSCORE_HOVER)
    highScoreRect = highScore.get_rect(center=(stg.SCREEN_W // 2, (stg.SCREEN_H // 2) + stg.FONT_SIZE * 2))
    screen.blit(highScore, highScoreRect)

    # Exit Button
    exit = font.render('EXIT', True, stg.EXIT_HOVER)
    exitRect = exit.get_rect(center=(stg.SCREEN_W // 2, stg.SCREEN_H // 2 + stg.FONT_SIZE * 4))
    screen.blit(exit, exitRect)

    pygame.display.update()


def react(pos):
    # If the mouse hovers over the play button
    if (stg.SCREEN_W // 2 - stg.FONT_SIZE * 1.25 <= pos[0] <= stg.SCREEN_W // 2 + stg.FONT_SIZE * 1.25) \
            and (stg.SCREEN_H // 2 - stg.FONT_SIZE // 1.5 <= pos[1] <= stg.SCREEN_H // 2 + stg.FONT_SIZE // 3):
        if pygame.mouse.get_pressed()[0] is False:
            stg.PLAY_HOVER = stg.GREEN
            stg.EXIT_HOVER = stg.WHITE
            stg.HIGHSCORE_HOVER = stg.WHITE

        # If the mouse clicks the play button
        else:
            stg.isTitle = False
            stg.PLAY_HOVER = stg.WHITE
            stg.EXIT_HOVER = stg.WHITE
            stg.HIGHSCORE_HOVER = stg.WHITE
            return False

    # If the mouse hovers the High Score button
    elif (stg.SCREEN_W // 2 - stg.FONT_SIZE * 3.5 <= pos[0] <= stg.SCREEN_W // 2 + stg.FONT_SIZE * 3.5) \
            and (stg.SCREEN_H // 2 - stg.FONT_SIZE // 3 + stg.FONT_SIZE * 1.5 <= pos[
        1] <= stg.SCREEN_H // 2 + stg.FONT_SIZE // 3 + stg.FONT_SIZE * 2):
        if pygame.mouse.get_pressed()[0] is False:
            stg.EXIT_HOVER = stg.WHITE
            stg.HIGHSCORE_HOVER = stg.GREEN
            stg.PLAY_HOVER = stg.WHITE

        # If the mouse clicks the High Score Button
        else:
            stg.EXIT_HOVER = stg.WHITE
            stg.HIGHSCORE_HOVER = stg.GREEN
            stg.PLAY_HOVER = stg.WHITE
            return True

    # If the mouse hovers the Exit Button
    elif (stg.SCREEN_W // 2 - stg.FONT_SIZE * 1.25 <= pos[0] <= stg.SCREEN_W // 2 + stg.FONT_SIZE * 1.25) \
            and (stg.SCREEN_H // 2 - stg.FONT_SIZE // 3 + stg.FONT_SIZE * 3.5 <= pos[
        1] <= stg.SCREEN_H // 2 + stg.FONT_SIZE // 3 + stg.FONT_SIZE * 4):
        if pygame.mouse.get_pressed()[0] is False:
            stg.EXIT_HOVER = stg.RED
            stg.HIGHSCORE_HOVER = stg.WHITE
            stg.PLAY_HOVER = stg.WHITE

        # If the mouse clicks the Exit Button
        else:
            stg.isTitle = False
            pygame.quit()
            stg.PLAY_HOVER = stg.WHITE
            stg.HIGHSCORE_HOVER = stg.WHITE
            return False

    else:
        stg.PLAY_HOVER = stg.WHITE
        stg.EXIT_HOVER = stg.WHITE
        stg.HIGHSCORE_HOVER = stg.WHITE


# Draws the High Score Screen
def highScore(screen):
    screen.fill(stg.BLACK)

    with open('high_score.txt', 'r') as f:
        scores_list = f.readlines()

        for i in range(0, 10):
            if i < len(scores_list):
                print(scores_list[i])

            else:
                break

    stg.isHighScore = False

    pygame.display.update()

    return False
