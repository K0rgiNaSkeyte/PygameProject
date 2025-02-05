import pygame
import random
from utils.game_object import GameObject
from utils.constans import HERO_HEALTH, HERO_MAX_MANA, HERO_MIN_MANA


# 2 класса - герой на карте и герой на экране сражения.

class Hero(GameObject):
    def __init__(self, position):
        self.x, self.y = position
        self.speed = 5

    def get_pos(self):
        return self.x, self.y

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 50, 50)

    def change_pos(self, newpos):
        self.x = newpos[0]
        self.y = newpos[1]

    def render(self):
        pass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def set_speed(self, new_speed):
        self.speed = new_speed


class HeroInBattle:
    def __init__(self):
        self.health = HERO_HEALTH
        self.mana = random.randint(HERO_MIN_MANA, HERO_MAX_MANA)
        self.name = "The Grand Hero"
