import pytmx
import Basic_Level

from utils.constans import MAPS_DIR
from utils.constans import HERO_START_POS


class Level1(Basic_Level):
    def __init__(self, busy_tiles, finish_tile):
        self.map = pytmx.load_pygame(f"{MAPS_DIR}/{Level1}")
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.busy_tiles = busy_tiles
        self.finish_tile = finish_tile

