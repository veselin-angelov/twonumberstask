import sqlite3

DB_NAME = 'numbers.db'

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS numbers
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number1 INTEGER NOT NULL,
        number2 INTEGER NOT NULL,
        string TEXT NOT NULL
    )
''')

conn.commit()

class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()