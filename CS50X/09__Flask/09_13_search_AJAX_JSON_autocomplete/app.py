# Szukanie z użyciem Ajax i JSON. Warto przeczytać najpierw plik 09_12.

# Poprzedni kod działał poprawnie, ale pod maską przesyłał mało elegancką listę
# znaczników <li></li> i tytułów między nimi, jako XML czytelny tylko dla HTMLa.
# Używanie XML w Ajax To stara szkoła.

# Obecnie API piszę się tak, by przesyłały dane w uniwersalnym dla wielu języków formacie JSON,
# czyli listę słowników: [{"id":123, "title":abc}, {"id":456, "title":def}].
# JSON łatwiej przeformatować dla potrzeb Java Scriptu czy Pythona.


from cs50 import SQL
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///shows.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        shows = db.execute(
            "SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + q + "%"
        )
    else:
        shows = []
    return jsonify(shows)
