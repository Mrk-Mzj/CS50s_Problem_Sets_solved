# cd 09_07__zapisy__i_usuwanie_z_SQLite
# flask --debug run


from flask import Flask, redirect, render_template, request
from cs50 import SQL


app = Flask("__name__")
db = SQL("sqlite:///zapisani.db")

SPORTS = ["Basketball", "Soccer", "Frisbee"]


@app.route("/")
def index():

    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    # Sprawdzenie inputów; trochę uproszczone:
    name = request.form.get("name")
    sport = request.form.get("sport")

    if not name or sport not in SPORTS:
        return render_template("failure.html")

    # Zapisanie osoby na sport:
    db.execute("INSERT INTO zapisani (name, sport) VALUES (?, ?)", name, sport)

    # Potwierdzenie zapisania:
    return redirect("/zapisani")


@app.route("/zapisani")
def zapisani():
    zapisani = db.execute("SELECT * FROM zapisani")
    return render_template("zapisani.html", zapisani=zapisani)


@app.route("/wypisz", methods=["POST"])
def wypisz():

    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM zapisani WHERE id = ?", id)
    return redirect("/zapisani")
