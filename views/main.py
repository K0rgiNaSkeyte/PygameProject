import pygame
import sys
from views.over_screen import draw_game_over


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.get_height()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        screen.fill((192, 192, 192))
        draw_game_over(screen)
        pygame.display.update()
        clock.tick(60)
