import sqlite3

import os

DIR = os.path.dirname(__file__)
DBNAME = "work.db"
DBPATH = os.path.join(DIR, DBNAME)

def schema(dbpath):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        SQL = "DROP TABLE IF EXISTS branches;"
        cursor.execute(SQL)

        SQL ="""CREATE TABLE branches(
             pk INTEGER PRIMARY KEY AUTOINCREMENT,
             City VARCHAR(64),
             State VARCHAR(2),
             zip_code VARCHAR(5)
            );"""

        cursor.execute(SQL)

        SQL = "DROP TABLE IF EXISTS employees;"
        cursor.execute(SQL)

        
        SQL ="""CREATE TABLE employees(
             pk INTEGER PRIMARY KEY AUTOINCREMENT,
             Last_name VARCHAR(30),
             First_name VARCHAR(30),
             employee_id VARCHAR(5),
             Salary FLOAT,
             branches_pk,
             FOREIGN KEY(branches_pk) REFERENCES branches(pk)
            );"""

        cursor.execute(SQL)

schema(DBPATH)