from models.game import Game

#Создаём объект класса Game, задаём название, размеры и частоту кадров, запускаем игру.
def main():
    app = Game("RPG Game beta v.0.0.1", 800, 600, 60)
    app.run()
