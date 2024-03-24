from flask import Flask, render_template
import sqlite3 

app = Flask(__name__)

@app.route('/home.html')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return ""

@app.route("/pizza/<int:id>")
def pizza(id):
    conn = sqlite3.connect('pizza.db')
    cur = conn.cursor()
    cur.execute('select * FROM Pizza WHERE id=?', (id,))
    pizza = cur.fetchone()

    return render_template('pizza.html', pizza = pizza)
 
if __name__ == "__main__":
    app.run(debug=True)

