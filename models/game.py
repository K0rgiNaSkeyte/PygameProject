import pygame
import sys
import pytmx

from models.hero import Hero
from utils.config import HERO_START_POS_LVL1, HERO_START_POS_LVL2, HERO_START_POS_LVL3
from models.level import LevelLoader
from views.battle_screen import BattleScreen
from views.over_screen import draw_game_over
from views.pause_menu import draw_pause_menu
from views.win_screen import draw_win


class Game:
    def __init__(self, caption, width, height, frame_rate):
        self.screen = pygame.display.set_mode((width, height))
        self.frame_rate = frame_rate
        self.curr_map = "one.tmx"
        self.level_loader = LevelLoader("one.tmx")
        self.game_over = False
        self.player = Hero(HERO_START_POS_LVL1)
        self.enemies = self.level_loader.get_enemy_objects()  # Получаем врагов из уровня
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

    def load_level1(self):
        self.level_loader = LevelLoader("one.tmx")
        self.player.change_pos(HERO_START_POS_LVL1)
        self.curr_map = "one.tmx"
        self.enemies = self.level_loader.get_enemy_objects()  # Обновляем список врагов

    def load_level2(self):
        self.level_loader = LevelLoader("two.tmx")
        self.player.change_pos(HERO_START_POS_LVL2)
        self.curr_map = "two.tmx"
        self.enemies = self.level_loader.get_enemy_objects()

    def load_level3(self):
        self.level_loader = LevelLoader("three.tmx")
        self.player.change_pos(HERO_START_POS_LVL3)
        self.curr_map = "three.tmx"
        self.enemies = self.level_loader.get_enemy_objects()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-self.player.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.player.move(self.player.speed, 0)
        if keys[pygame.K_UP]:
            self.player.move(0, -self.player.speed)
        if keys[pygame.K_DOWN]:
            self.player.move(0, self.player.speed)

        player_rect = self.player.get_rect()
        next_map = self.level_loader.check_enter_objects(player_rect)

        if self.level_loader.check_collisions(player_rect):
            print("Collision detected!")

        for enemy in self.enemies:
            if not enemy.defeated and player_rect.colliderect(enemy.get_rect()):
                battle_screen = BattleScreen(self.screen, self.player.image, enemy.image)
                battle_screen.run_battle()
                if enemy.health <= 0:
                    enemy.defeated = True  # Устанавливаем defeated в True

        if next_map and self.curr_map == "one.tmx":
            self.load_level2()
        if next_map and self.curr_map == "two.tmx":
            self.load_level3()
        if next_map and self.curr_map == "three.tmx":
            pass

    #         self.load_win()

    def draw(self):
        # Очищаем экран
        self.screen.fill((0, 0, 0))

        # Получаем список видимых слоев
        visible_layers = list(self.level_loader.map.visible_layers)

        # Отрисовываем каждый слой
        for layer in visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    # Получаем изображение тайла по GID
                    tile_image = self.level_loader.map.get_tile_image_by_gid(gid)

                    if tile_image:  # Проверяем, существует ли изображение тайла
                        # Отрисовываем тайл на экране
                        self.screen.blit(tile_image,
                                         (x * self.level_loader.map.tilewidth, y * self.level_loader.map.tileheight))

        # Отрисовываем игрока
        pygame.draw.rect(self.screen, (255, 0, 0), self.player.get_rect())

        # Рисуем врагов, которые еще не были побеждены
        for enemy in self.enemies:
            if not enemy.defeated:
                self.screen.blit(enemy.image,
                                 enemy.get_position())

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
