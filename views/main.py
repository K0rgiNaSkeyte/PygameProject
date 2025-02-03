from models.game import Game
from utils.config import SCREEN_HEIGHT, SCREEN_WIDTH


# Создаём объект класса Game, задаём название, размеры и частоту кадров, запускаем игру.
def main():
    app = Game("RPG Game beta v.0.0.1", SCREEN_WIDTH, SCREEN_HEIGHT, 60)
    app.run()
