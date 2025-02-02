import pygame
import sys

from level1 import Level1
from level2 import Level2
from level3 import Level3
from views.battle_screen import draw_battle
from views.over_screen import draw_game_over
from views.pause_menu import draw_pause_menu
from views.win_screen import draw_win


class Game:
    def __init__(self, caption, width, height, frame_rate):
        self.frame_rate = frame_rate
        self.game_over = False
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    for handler in self.keydown_nadlers[event.key]:
                        handler(event.key)
                case pygame.KEYUP:
                    for handler in self.keydown_handlers[event.key]:
                        handler(event.key)
                case pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP:
                    for handler in self.mouse_handlers:
                        handler(event.type, event.pos)

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)