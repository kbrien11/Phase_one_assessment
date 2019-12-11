import sqlite3
import os

DIR = os.path.dirname(__file__)
DBNAME = "food.db"
DBPATH = os.path.join(DIR, DBNAME)

def schema(dbpath):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        SQL = "DROP TABLE IF EXISTS food;"
        cursor.execute(SQL)

        SQL = """CREATE TABLE food(
             pk INTEGER PRIMARY KEY AUTOINCREMENT,
             Name VARCHAR(64),
             City VARCHAR(32),
             Cuisine_style TEXT,
             Ranking INTEGER,
             Rating INTEGER,
             Price_range INTEGER,
             Number_of_reviews INTEGER,
             Reviews TEXT
            );"""

        cursor.execute(SQL)
schema(DBPATH)