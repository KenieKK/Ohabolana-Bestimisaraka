from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_proverbe_aleatoire():
    conn = sqlite3.connect("proverbes.db")
    c = conn.cursor()
    c.execute("SELECT texte FROM proverbes ORDER BY RANDOM() LIMIT 1")
    proverbe = c.fetchone()[0]
    conn.close()
    return proverbe

@app.route("/")
def index():
    proverbe = get_proverbe_aleatoire()
    return render_template("/index.html", proverbe=proverbe)

if __name__ == "__main__":
    app.run(debug=True)

