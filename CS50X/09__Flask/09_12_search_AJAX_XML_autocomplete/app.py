# Szukanie filmów z użyciem Ajax.
# Kod Java Script w pliku index.html wysyła w locie zapytania na ścieżkę /search.

from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///shows.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():

    # Typowe zapytanie GET; sprawdź wartość przy kluczu ?q=
    # jeśli istnieje, poszukaj jej w bazie danych i dodaj do shows:
    q = request.args.get("q")
    if q:
        shows = db.execute(
            "SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + q + "%"
        )

    # Jeśli user wyczyścił pole szukania, wyczyść również listę shows:
    else:
        shows = []
    return render_template("search.html", shows=shows)
