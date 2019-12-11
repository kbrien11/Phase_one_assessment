from flask import Flask, request, render_template, redirect, session, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/api/login', methods=['GET'])
def login():
    return render_template('structure.html')

@app.route('/api/restaurants/<City>', methods=['GET'])
def lookup_item(City):
    with sqlite3.connect('food.db') as conn:
        cursor = conn.cursor()
        sql = """SELECT * FROM food WHERE City=?"""
        cursor.execute(sql, (City,))
        result = cursor.fetchall()
        if result:
            return jsonify({"name":result[1], "city":result[2], "cuisine_style":result[3],"ranking":result[4],"rating":result[5],"price_range":result[6],"number_of_reviews":result[7],"reviews":result[8]})
        else:
            return jsonify({"error":"City does not exist"})

if __name__ == "__main__":
    app.run(debug=True , port = 5000)