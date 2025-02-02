from models.game import Game


def main():
    app = Game("RPG Game beta v.0.0.1", 800, 600, 60)
    app.run()
