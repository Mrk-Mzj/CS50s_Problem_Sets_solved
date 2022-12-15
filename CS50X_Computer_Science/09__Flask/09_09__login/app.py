# Logowanie (samym imieniem)
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Skonfigurujmy sesję.
# Sesja permanentna utrzymuje się po odświerzeniu strony. Nie chcemy takiej:
app.config["SESSION_PERMANENT"] = False

# Ciastka po stronie serwera. Mogą być w RAM, bazie danych, tu w plikach.
# Utworzy się dla nich folder. Każdy zaloowany user będzie miał swoje ciastko sesji.
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    # Strona główna wpuszcza tylko tych, którzy mają ciastko sesji.
    # Jeśli ktoś wejdzie na nią ręcznie, nie będzie istniało ciastko.
    # Zostanie więc skierowany do strony logowania. Tam powstają ciastka sesji:
    if not session.get("name"):
        return redirect("/login")

    # Ale jeśli podał wcześniej imię, ma ciastko i zobaczy pełną stronę index.html:
    return render_template("index.html")


# Strona logowania obsługuje dwie metody: GET i POST.
# To pozwala obsłużyć dwie różne akcje:
# tworzenie ciastek i przekierowywanie userów z ciastkami na główną.
@app.route("/login", methods=["GET", "POST"])
def login():

    # 1
    # Jeśli user trafił tu z formularza (POST) kod weźmie jego imię, doda je do ciastka
    # i przekieruje go na stronę główną:
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    # 2
    # Jeśli jednak user trafił tu samodzielnie albo z przekierowania (GET),
    # zostanie mu wyświetlona strona logowania:
    return render_template("login.html")

    # Plik login.html wykonuje ciekawy manewr. Jego formularz linkuje z powrotem do login.html.
    # To od powyższego kodu Pythona zależy właściwe rozprowadzenie ruchu, nie od linku w HTMLu.

    # Ostatecznie gdyby formularz kierował wprost na główną, nie miałoby kiedy powstać ciastko.
    # Główna odrzuciłaby takiego użytkownika. Do powstania ciastka potrzebna jest albo podstrona
    # pośrednia, albo strona logowania o dwóch funkcjach - jak wyżej.


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")
