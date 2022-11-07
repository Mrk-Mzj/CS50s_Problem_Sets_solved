# Flask wymaga istnienia pliku app.py, pliku requirements.txt (opisującego użyte moduły),
# folderu na templatki HTML i folderu na elementy static, których Flask ma nie zmieniać,
# np. CSS, skrypty javy, zdjęcia, itp.

# Program Flask uruchamiamy z terminala poleceniem:
# cd CS50X/09__Flask/09_01
# flask run

# domyślnie otwiera się http://127.0.0.1:5000/
# jeśli chcemy przekazać parametr name: http://127.0.0.1:5000/?name=Marek%20Mazij

from flask import Flask, render_template, request


# zmień ten plik, w którym jesteśmy (__name__) na aplikację Flaska:
app = Flask("__name__")


# Funkcja dekorująca @app.route mówi:
# w przypadku wywołania podstawowego URL...
@app.route("/")

# ...uruchom funkcję, która będzie zwracać stronę www wyrenderowaną na bazie szablonu...
def index():

    # ...a jeśli w URL znajdzie się parametr "name" przypisz go do zmiennej "name"...
    name = request.args.get("name")

    # ...i uruchom szablon index.html, przekazując mu tę zmienną z zapytania:
    if name == None:
        return render_template("index.html", name="Stranger")
    else:
        return render_template("index.html", name=name)
