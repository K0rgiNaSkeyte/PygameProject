import pygame
import pytmx
import Basic_Level

from utils.constans import MAPS_DIR


class Level1(Basic_Level):
    def __init__(self, free_tiles, finish_tile):
        self.map = pytmx.load_pygame(f"{MAPS_DIR}/{Level1}")
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

