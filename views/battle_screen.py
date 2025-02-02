import pygame
import sys
from random import randint
from utils.config import SCREEN_WIDTH as WIDTH
from utils.config import SCREEN_HEIGHT as HEIGHT
from models.enemy import EnemyInBattle
from models.hero import HeroInBattle


# Окно боя, самое сложное окно с тремя кнопками, портретами, показателями здоровья, маны и именами.

def draw_battle(screen, hero_image, enemy_image):
    pygame.init()
    hero = HeroInBattle()
    enemy = EnemyInBattle()
    screen.fill("BLACK")

    screen.blit(hero_image, (50, 150))
    screen.blit(enemy_image, (WIDTH - 250, 150))

    font = pygame.font.Font(None, 36)
    hero_name_surface = font.render(hero.name, True, BLACK)
    enemy_name_surface = font.render(enemy.name, True, BLACK)
    screen.blit(hero_name_surface, (50, 100))
    screen.blit(enemy_name_surface, (WIDTH - 250, 100))

    # Отрисовка показателей здоровья и маны
    health_surface = font.render(f"Здоровье: {hero.health}  Мана: {hero.mana}", True,
                                 "WHITE")
    enemy_health_surface = font.render(
        f"Здоровье: {enemy.health}  Мана: {enemy.mana}", True, "WHITE")
    screen.blit(health_surface, (50, 250))
    screen.blit(enemy_health_surface, (WIDTH - 250, 250))

    # Отрисовка кнопок действий
    pygame.draw.rect(screen, "GREEN", (50, HEIGHT - 100, 200, 50))
    pygame.draw.rect(screen, "GREEN", (300, HEIGHT - 100, 200, 50))
    pygame.draw.rect(screen, "GREEN", (550, HEIGHT - 100, 200, 50))

    action_font = pygame.font.Font(None, 30)
    attack_surface = action_font.render("Атака", True, "BLACK")
    restore_surface = action_font.render("Восстановление маны", True, "BLACK")
    charge_surface = action_font.render("Зарядка маны", True, "BLACK")

    screen.blit(attack_surface, (125, HEIGHT - 80))
    screen.blit(restore_surface, (400, HEIGHT - 80))
    screen.blit(charge_surface, (650, HEIGHT - 80))

    pygame.display.flip()