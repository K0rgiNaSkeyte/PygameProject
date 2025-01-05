import sqlite3


class DatabaseManager:
    def __init__(self, db_path: str = "game.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        pass

    def save_game(self):
        pass

    def get_saved_games(self):
        pass

    def get(self):
        pass

    def update_score(self):
        pass

    def get_score(self):
        pass

    def get_all_scores(self):
        pass
