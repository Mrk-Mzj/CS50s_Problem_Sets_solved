# API_KEY zapisałem w pliku tekstowym. Ustawiamy go w cmd:
# set API_KEY=pk_3b6cf277dec74af49ff62d8c0f2e22d4
# i restartujemy cmd.
# Dla bash i powershell komendy brzmią trochę inaczej.
# Zmienne można też wpisać na stałe, w ustawieniach systemu.


import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# funkcje importowane z helpers.py:
from helpers import apology, login_required, lookup, usd


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
# usd to funkcja w helpers.py; ułatwia formatowanie walut.
app.jinja_env.filters["usd"] = usd

# Konfiguruj aplikację by ciastka sesji były trzymane w lokalnym systemie, np. na dysku.
# Tak, jak robiliśmy to już wcześniej. Flask na domyślnych ustawieniach tworzyłby sesje
# w cyfrowo podpisanych ciastkach.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    # Wyłączamy cache by zmiany, jakie robimy w plikach, były zawsze widziane przez przeglądarkę
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Login_required to funkcja dekorująca, stworzona w helpers.py.
# Przekierowuje niezalogowanych do strony logowania.
@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


# Login zamienia wprowadzone hasło na hasz. Porównuje go z haszem w bazie danych.
# Tworzy ciastko z id użytkownika. W ten sposób ścieżki wiedzą, który user jest zalogowany.
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):  # type: ignore
            # powyższy dopisek to info do Pylance by nie podkreślał błędu w kodzie od autorów.
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
