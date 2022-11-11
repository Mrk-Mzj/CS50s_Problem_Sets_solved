# Program Flask uruchamiamy z terminala poleceniem:
# cd CS50X/09__Flask/09_06__SQLite
#
# auto restart serwera przy każdym zapisie:
# flask --debug run


from flask import Flask, redirect, render_template, request


app = Flask("__name__")


SPORTS = ["Basketball", "Soccer", "Frisbee"]
ZAPISANI = {}


@app.route("/")
def index():

    # przekazujemy do index.html naszą zmienną SPORTS:
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    # Sprawdzenie imienia:
    name = request.form.get("name")

    if not name:
        return render_template("error.html", message="Nie podano imienia.")

    # Sprawdzenie sportu:
    sport = request.form.get("sport")

    if not sport:
        return render_template("error.html", message="Nie wybrano sportu.")
    if sport not in SPORTS:
        return render_template("error.html", message="Sport spoza listy sportów!")

    # Zapisanie osoby na sport:
    ZAPISANI[name] = sport

    # Potwierdzenie zapisania:
    return redirect("/zapisani")


@app.route("/zapisani")  # tu metoda GET; POST był tylko przy obsłudze formularza
def zapisani():
    return render_template("zapisani.html", zapisani=ZAPISANI)
