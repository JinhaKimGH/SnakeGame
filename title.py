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
            stg.HIGHSCORE_HOVER = stg.WHITE
            stg.PLAY_HOVER = stg.WHITE
            stg.isHighScore = True

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

    # Resets the hover color if mouse is not hovering over anything
    else:
        stg.PLAY_HOVER = stg.WHITE
        stg.EXIT_HOVER = stg.WHITE
        stg.HIGHSCORE_HOVER = stg.WHITE


# Translates the text file for high scores
def translateTXT(scores):
    if len(scores) == stg.scoreDict:
        return

    else:
        length = len(scores)
        for i in range(0, length):
            acc_score = ""
            acc_time = ""

            index = 7
            while scores[i][index] != " ":
                acc_score += scores[i][index]

                index += 1

            index += 7

            while scores[i][index] != "s":
                acc_time += scores[i][index]

                index += 1

            stg.scoreDict[scores[i]] = [int(acc_score), int(acc_time)]


# Sorts the list of scores
def scoreSort(scores):
    length = len(scores)
    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            if stg.scoreDict[scores[j]][0] > stg.scoreDict[scores[j+1]][0]:
                scores[j], scores[j+1] = scores[j+1], scores[j]

            elif stg.scoreDict[scores[j]][0] == stg.scoreDict[scores[j + 1]][0]:
                if stg.scoreDict[scores[j]][1] < stg.scoreDict[scores[j + 1]][1]:
                    scores[j], scores[j+1] = scores[j+1], scores[j]

    stg.isSorted = True


# Draws the High Score Screen
def highScore(screen, mousePos):
    # Reads the text in the high_score.txt file
    if not stg.scores_list:
        with open('high_score.txt', 'r') as f:
            stg.scores_list = f.readlines()

    # Sorts the score list by highest score and lowest time
    if not stg.isSorted:
        translateTXT(stg.scores_list)
        scoreSort(stg.scores_list)
        stg.scores_list.reverse()

    font = pygame.font.Font('freesansbold.ttf', stg.SCORE_FONT)

    title = pygame.font.Font('freesansbold.ttf', stg.HIGHSCORE_FONT)

    # Title
    caption = title.render('HIGH SCORES', True, stg.WHITE)
    captionRect = caption.get_rect()
    captionRect.center = (stg.SCREEN_W // 2, stg.titleFont)

    # Go Back
    menuFont = pygame.font.Font('freesansbold.ttf', stg.FONT_SIZE)
    back = menuFont.render('BACK', True, stg.BACK_HOVER)
    backRect = back.get_rect()
    backRect.center = (stg.SCREEN_W // 2, stg.SCREEN_H - stg.FONT_SIZE)

    # Screen Updates
    screen.fill(stg.BLACK)

    screen.blit(back, backRect)
    screen.blit(caption, captionRect)

    # If the mouse is hovering the back button
    if (stg.SCREEN_H - stg.FONT_SIZE*1.5 <= mousePos[1] <= stg.SCREEN_H - stg.FONT_SIZE//2) and \
            (stg.SCREEN_W // 2 - stg.FONT_SIZE * 2 <= mousePos[0] <= stg.SCREEN_W // 2 + stg.FONT_SIZE * 2):
        stg.BACK_HOVER = stg.RED

        # If the mouse clicks on the back button
        if pygame.mouse.get_pressed()[0] is True:
            stg.isHighScore = False
            stg.isTitle = True

    # The color resets otherwise
    else:
        stg.BACK_HOVER = stg.WHITE

    start_y = stg.HIGHSCORE_FONT * 3

    # Displays the High Scores
    for i in range(0, 7):
        if i < len(stg.scores_list):
            scores = font.render(str(stg.scores_list[i])[:-1], True, stg.WHITE)
            scoresRect = scores.get_rect()
            scoresRect.center = (stg.SCREEN_W // 2, start_y)
            start_y += stg.SCORE_FONT * 2

            screen.blit(scores, scoresRect)

        else:
            break

    pygame.display.update()

