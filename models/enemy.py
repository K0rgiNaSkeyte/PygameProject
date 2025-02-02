import pygame
from random import randint
from utils.game_object import GameObject
from utils.constans import ENEMY_MAX_HEALTH, ENEMY_MIN_HEALTH, ENEMY_MAX_MANA, ENEMY_MIN_MANA

# 2 класса - враг на карте и враг на экране сражения.

class Enemy(GameObject):
    def __init__(self, position):
        self_x, self.y = position

    def get_pos(self):
        return self.x, self.y

    def render(self):
        pass


class EnemyInBattle:
    def __init__(self):
        self.health = randint(ENEMY_MIN_HEALTH, ENEMY_MAX_HEALTH)
        self.mana = randint(ENEMY_MIN_MANA, ENEMY_MAX_MANA)
        self.name = "The Paranormal Demon"
