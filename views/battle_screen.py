import pygame
from random import randint
from utils.config import SCREEN_WIDTH as WIDTH, SCREEN_HEIGHT as HEIGHT
from models.enemy import EnemyInBattle
from models.hero import HeroInBattle


class BattleScreen:
    def __init__(self, screen, hero_image, enemy_image):
        self.screen = screen
        self.hero = HeroInBattle()
        self.enemy = EnemyInBattle()
        self.enemy_max_health = self.enemy.health
        self.hero_image = hero_image
        self.enemy_image = enemy_image
        self.font = pygame.font.Font(None, 36)
        self.message = ""

    def draw(self):
        self.screen.fill("BLACK")

        self.screen.blit(self.hero_image, (50, 150))
        self.screen.blit(self.enemy_image, (WIDTH - 250, 150))

        hero_name_surface = self.font.render(self.hero.name, True, "WHITE")
        enemy_name_surface = self.font.render(self.enemy.name, True, "WHITE")
        self.screen.blit(hero_name_surface, (50, 100))
        self.screen.blit(enemy_name_surface, (WIDTH - 250, 100))

        # Отрисовка показателей здоровья и маны
        health_surface = self.font.render(f"Здоровье: {self.hero.health}  Мана: {self.hero.mana}", True, "WHITE")
        enemy_health_surface = self.font.render(f"Здоровье: {self.enemy.health}  Мана: {self.enemy.mana}", True,
                                                "WHITE")
        self.screen.blit(health_surface, (50, 250))
        self.screen.blit(enemy_health_surface, (WIDTH - 250, 250))

        # Отрисовка сообщения о действии
        message_surface = self.font.render(self.message, True, "WHITE")
        message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(message_surface, message_rect)

        # Отрисовка кнопок действий
        pygame.draw.rect(self.screen, "GREEN", (50, HEIGHT - 100, 200, 50))
        pygame.draw.rect(self.screen, "GREEN", (300, HEIGHT - 100, 200, 50))
        pygame.draw.rect(self.screen, "GREEN", (550, HEIGHT - 100, 200, 50))

        action_font = pygame.font.Font(None, 30)
        attack_surface = action_font.render("Атака", True, "BLACK")
        restore_surface = action_font.render("Восстановление", True, "BLACK")
        charge_surface = action_font.render("Зарядка маны", True, "BLACK")

        self.screen.blit(attack_surface, (125, HEIGHT - 80))
        self.screen.blit(restore_surface, (400, HEIGHT - 80))
        self.screen.blit(charge_surface, (650, HEIGHT - 80))

        pygame.display.flip()

    def attack(self):
        damage = randint(1, 15)
        self.enemy.health -= damage
        self.message = f"Герой атакует! Урон: {damage}. Здоровье врага: {self.enemy.health}"

    def heal(self):
        if self.hero.mana > 0:
            healing_amount = randint(1, 15)
            mana_cost = randint(1, 3)
            if self.hero.mana >= mana_cost:
                self.hero.health += healing_amount
                self.hero.mana -= mana_cost
                self.message = f"Герой восстанавливает здоровье! Восстановлено: {healing_amount}. Здоровье героя: {self.hero.health}. Мана героя: {self.hero.mana}"

    def restore_mana(self):
        mana_gain = randint(1, 5)
        self.hero.mana += mana_gain
        self.message = f"Герой восстанавливает ману! Восстановлено: {mana_gain}. Мана героя: {self.hero.mana}"

    def enemy_turn(self):
        action = randint(1, 2)  # 1 = атака, 2 = восстановление
        if action == 1:
            damage = randint(1, 15)
            self.hero.health -= damage
            self.message = f"Враг атакует! Урон: {damage}. Здоровье героя: {self.hero.health}"
        elif action == 2 and self.enemy.health < self.enemy_max_health:
            healing_amount = randint(1, 15)
            self.enemy.health += healing_amount
            self.message = f"Враг восстанавливает здоровье! Восстановлено: {healing_amount}. Здоровье врага: {self.enemy.health}"

    def run_battle(self):
        while self.hero.health > 0 and self.enemy.health > 0:
            self.draw()
            # Здесь следует ожидать нажатия кнопки для выбранного действия
            # Например, имитация нажатия кнопки "Атака"
            self.attack()
            self.draw()  # Обновляем экран после действия героя

            if self.enemy.health > 0:
                self.enemy_turn()
                self.draw()  # Обновляем экран после действия врага

            if self.hero.health <= 0:
                print("Герой повержен!")
            elif self.enemy.health <= 0:
                print("Враг повержен!")