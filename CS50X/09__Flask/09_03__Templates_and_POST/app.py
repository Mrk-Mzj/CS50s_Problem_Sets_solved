# Program Flask uruchamiamy z terminala poleceniem:
# cd CS50X/09__Flask/09_03__Templates_and_POST
# flask run

# Nasze pliki HTML mają sporo powtarzającego się kodu. Stwórzmy szablon "layout",
# zawierający część wspólną templatek, a w templatkach deklarujmy tylko zmiany.
# Do opisu zmian wewnątrz plików HTML użyjemy składni JINJA.

# Plik Pythona nie zmienia się, ponieważ w modelu MVC kontroler (app.py)
# jest rozdzielony od warstwy prezentacji (HTML).

# Jednak przy okazji zmienię metodę GET na POST, aby dane nie leciały w URL.

from flask import Flask, render_template, request


app = Flask("__name__")


@app.route("/")
def index():

    return render_template("index.html")


# zmiana 1/3:
# greetings/") na
# greetings/", methods=["POST"])


@app.route("/greetings/", methods=["POST"])
def greetings():

    # zmiana 2/3:
    # args na form:
    name = request.form.get("name")

    # zmiana 3/3:
    # ...w pliku index.html.

    if name == None:
        name = "Stranger"

    return render_template("greetings.html", name=name)
