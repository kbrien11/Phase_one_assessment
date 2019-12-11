import csv
import sqlite3

def dump_employees(filepath):
    with open(filepath, 'r') as input_csv:
        reader = csv.reader(input_csv)
        next(reader)
        for line in reader:
            Name = line[0]
            City = line[1]
            Cuisine_style = line[2]
            Ranking = line[3]
            Rating = line[4]
            Price_range = line[5]
            Number_of_reviews = line[6]
            Reviews = line[7]
            add_value(Name,City,Cuisine_style,Ranking,Rating,Price_range,Number_of_reviews,Reviews)
 
def add_value(Name,City,Cuisine_style,Ranking,Rating,Price_range,Number_of_reviews,Reviews):
    with sqlite3.connect("food.db") as conn:
        cursor = conn.cursor()

        SQL = """ INSERT INTO food (Name,City,Cuisine_style,Ranking,Rating,Price_range,Number_of_reviews,Reviews)
            VALUES (?,?,?,?,?,?,?,?)"""

        cursor.execute(SQL, (Name,City,Cuisine_style,Ranking,Rating,Price_range,Number_of_reviews,Reviews))


if __name__=="__main__":
   dump_employees('food.csv')