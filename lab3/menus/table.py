import pygame
from tools.loader import TABLE, BACK
from tools.utils import rounded_rect


def showScreen(win):
    win.fill((0, 0, 0))
    rounded_rect(win, (255, 255, 255), (70, 10, 360, 60), 16, 4)
    rounded_rect(win, (255, 255, 255), (10, 80, 480, 410), 10, 4)

    win.blit(TABLE.HEAD, (100, 12))
    for cnt, i in enumerate(TABLE.TEXT):
        win.blit(i, (20, 90 + cnt * 30))

    win.blit(BACK, (460, 0))
    pygame.display.update()


def main(win):
    showScreen(win)
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 < x < 500 and 0 < y < 50:
                    return 1

