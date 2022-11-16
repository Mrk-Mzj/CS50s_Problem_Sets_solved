# Dodawanie książek do koszyka zakupowego.

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
db = SQL("sqlite:///store.db")

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Root wyświetla wszystkie książki z bazy danych.
# Dowolną z nich można dodać do koszyka przyciskiem.
# Przycisk działa identycznie, jak formularz
# z niewidocznym polem w którym z góry wpisany jest ID książki z bazy.
# Kliknięcie przycisku kieruje metodą POST do /cart.
@app.route("/")
def index():
    books = db.execute("SELECT * FROM books")
    return render_template("books.html", books=books)


@app.route("/cart", methods=["GET", "POST"])
def cart():

    # Stwórz pusty koszyk, jeżeli nie zrobiliśmy tego wcześniej
    # przy dodawaniu innej książki:
    if "cart" not in session:
        session["cart"] = []

    # POST - czyli ktoś wszedł z formularza. Powinniśmy znać ID dodanej książki.
    # Jeśli rzeczywiście tak jest, dodajmy ją do ciastka sesji i przeładujmy stronę:
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["cart"].append(id)
        return redirect("/cart")

    # GET - ktoś wszedł bezpośrednio, albo z przeładowania po dodaniu książki.
    # Sprawdźmy nazwy książek w koszyku na podstawie ich ID z ciastka i wylistujmy:
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
    return render_template("cart.html", books=books)
