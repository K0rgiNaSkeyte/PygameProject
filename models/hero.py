import pygame
from utils.game_object import GameObject
from utils.constans import HERO_HEALTH, HERO_MAX_MANA, HERO_MIN_MANA


class Hero(GameObject):
    def __init__(self, position):
        self_x, self.y = position

    def get_pos(self):
        return self.x, self.y

    def render(self):
        pass
