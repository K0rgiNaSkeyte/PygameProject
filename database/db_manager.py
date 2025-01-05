import sqlite3


class DatabaseManager:
    def __init__(self, db_path: str = "game_database.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS game_scores (
                walkthrough_number INTEGER PRIMARY KEY,
                score INTEGER NOT NULL
            )
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS player_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                position_x INTEGER NOT NULL,
                position_y INTEGER NOT NULL,
                level_number INTEGER NOT NULL,
                current_score INTEGER NOT NULL,
                save_name TEXT NOT NULL UNIQUE,
                walkthrough_number INTEGER,
                FOREIGN KEY (walkthrough_number) REFERENCES game_scores (walkthrough_number)
            )
        ''')

        conn.commit()
        conn.close()

    def save_game(self, x_pos, y_pos, lvl, current_score, save_name, walkthrough_number):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        try:
            cur.execute('''
            INSERT INTO player_data (position_x, position_y, level_number, current_score, save_name, walkthrough_number)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (x_pos, y_pos, lvl, current_score, save_name, walkthrough_number))
            conn.commit()
        except sqlite3.IntegrityError:
            pass
        finally:
            conn.close()

    def get_saved_games(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT save_name FROM player_data")
        saves = cur.fetchall()
        conn.close()
        saves = [save[0] for save in saves]
        return saves

    def get_save_game(self, save_name):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute("SELECT * FROM player_data WHERE save_name = ?", (save_name,))
        save_data = cur.fetchone()
        conn.close()

        return {
            'id': save_data[0],
            'position_x': save_data[1],
            'position_y': save_data[2],
            'lvl': save_data[3],
            'current_score': save_data[4],
            'save_name': save_data[5],
            'walkthrough_number': save_data[6]
        }

    def update_score(self, walkthrough_number, score):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute('SELECT * FROM game_scores WHERE order_number = ?', (walkthrough_number,))
        result = cur.fetchone()

        if result:
            cur.execute('UPDATE game_scores SET score = ? WHERE order_number = ?', (score, walkthrough_number))
        else:
            cur.execute('INSERT INTO game_scores (order_number, score) VALUES (?, ?)', (walkthrough_number, score))

        conn.commit()
        conn.close()

    def get_score(self, walkthrough_number):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT score FROM game_scores WHERE walkthrough_number = ?", (walkthrough_number,))
        score = cur.fetchone()
        conn.close()
        return score[0]

    def get_all_scores(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT walkthrough_number, score FROM game_scores")
        scores = cur.fetchall()
        conn.close()

        return scores
