#Title Functions
import pygame
import settings as stg

def draw(screen):
    font = pygame.font.Font('freesansbold.ttf', stg.FONT_SIZE)
    title = pygame.font.Font('freesansbold.ttf', stg.titleFont)

    #Title
    caption = title.render('Snake', True, stg.WHITE)
    captionRect = caption.get_rect()
    captionRect.center = (stg.SCREEN_W//2, stg.titleFont)
    title_bg = title.render('Snake', True, stg.PALE_WHITE)
    titleRect = title_bg.get_rect()
    titleRect.center = (stg.SCREEN_W//2 + 4, stg.titleFont + 4)

    #Play Button
    pygame.draw.rect(screen, stg.PLAY_HOVER, pygame.Rect(stg.SCREEN_W//2 - 5, stg.SCREEN_H//2 - stg.FONT_SIZE), width=2)

    #Exit Button
    pygame.draw.rect(screen, stg.EXIT_HOVER, pygame.Rect(stg.SCREEN_W // 2 - 5, stg.SCREEN_H // 2 + stg.FONT_SIZE * 2), width=2)

    #Play button
    play = font.render('PLAY', True, stg.PLAY_HOVER, stg.BLACK)
    playRect = play.get_rect(center=(stg.SCREEN_W//2, stg.SCREEN_H//2))
    screen.blit(play, playRect)

    #Exit Button
    exit = font.render('EXIT', True, stg.EXIT_HOVER, stg.BLACK)
    exitRect = exit.get_rect(center=(stg.SCREEN_W//2, stg.SCREEN_H//2 + stg.FONT_SIZE * 2))
    screen.blit(exit, exitRect)

    pygame.display.update()