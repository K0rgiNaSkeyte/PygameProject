import pytmx
import pygame

from utils.constans import MAPS_DIR


class LevelLoader:
    def __init__(self, level):
        self.map = pytmx.load_pygame(f"{MAPS_DIR}/{level}")
        self.collisions = []
        self.load_collisions()

    def load_collisions(self):
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if "walkable" in obj.properties and obj.properties["walkable"]:
                        rect = pygame.Rect(int(float(obj.x)), int(float(obj.y)), int(float(obj.width)), int(float(obj.height)))
                        self.collisions.append(rect)

    def check_collisions(self, player_rect):
        for collision in self.collisions:
            if player_rect.colliderect(collision):
                return True
        return False

    def check_enter_objects(self, player_rect):
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if 'is_player_enter' in obj.properties:
                        enter_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                        if player_rect.colliderect(enter_rect):
                            return obj.properties.get()
