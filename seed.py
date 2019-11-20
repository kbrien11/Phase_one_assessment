import sqlite3
import os

DIR = os.path.dirname(__file__)
DBNAME = "work.db"
DBPATH = os.path.join(DIR, DBNAME)

def seed(dbpath):

    branches = [
            ("Flushing", "NY", "11368"),
            ("Houston", "TX", "77002")]  

    employees = [
            ("Lockett", "Walker", "S0001",45000,1),
            ("Coleman", "Casey", "S0002", 70000,2),
            ("Kilome", "Franklyn", "S0003",67000,2),
            ("Santiago", "Hecton", "S0004",100000,1),
            ("Valdez", "Framber", "S0005",39000,1),
            ("Guduan", "Reymin", "S0007", 67000,2),
            ("Cole", "Gerrit", "S0008", 55000,1)]


    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()

        SQL = """INSERT INTO branches(City, State, Zip_code) VALUES (?,?,?)"""
        for branch in branches:
            cursor.execute(SQL, branch)


        SQL = """INSERT INTO employees(Last_name,First_name,employee_id,salary,branches_pk) VALUES (?,?,?,?,?)"""
        for employee in employees:
            cursor.execute(SQL, employee)


if __name__ == "__main__":
    seed(DBPATH)