import pygame

from utils.game_object import GameObject
from utils.text_object import TextObject
from utils import config as c


class Button(GameObject):
    def __init__(self, x, y, w, h, text, on_click=lambda x: None, padding=0):
        super().init(x, y, w, h)
        self.state = "normal"
        self.on_click = on_click
        self.text = TextObject(x + padding,
                               y + padding, lambda: text,
                               c.button_text_color,
                               c.font_name,
                               c.font_size)

    def draw(self, screen):
        pygame.draw.rect(screen,
                         self.back_color,
                         self.bounds)
        self.text.draw(screen)
