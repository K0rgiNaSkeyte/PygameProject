import pygame
import random
from utils.game_object import GameObject
from utils.constans import HERO_HEALTH, HERO_MAX_MANA, HERO_MIN_MANA


# 2 класса - герой на карте и герой на экране сражения.

class Hero(GameObject):
    def __init__(self, position):
        self_x, self.y = position

    def get_pos(self):
        return self.x, self.y

    def render(self):
        pass


class HeroInBattle:
    def __init__(self):
        self.health = HERO_HEALTH
        self.mana = random.randint(HERO_MIN_MANA, HERO_MAX_MANA)
        self.name = "The Grand Hero"
