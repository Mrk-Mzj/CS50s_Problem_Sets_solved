import os
import requests  # type: ignore -dopisek dla Pylance, by nie podkreślał błędu w kodzie od autorów
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        # Kiedy pojawia się błąd, funkcja otwiera stronę apology.html i przekazuje jej komunikat.
        # Generator memów, użyty na tej stronie, oczekuje komunikatów w formie GET, czyli w URL.
        # URL nie obsługuje wszystkich znaków. Twórca generatora wmyślił obejście, zastępowanie
        # jendych znaków innymi. Poniżej je implementujemy.
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """

    # To taka funkcja strażnik, napisana przez twórców Flaska.
    # Przyjmuje parametry (login, hasło) funkcji dekorowanej i zwraca ją z tymi parametrami.
    # Czyli nie robi nic, jest przezroczysta — chyba, że id usera nie ma w sesji; wtedy przekierowuje na /login.
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Połącz się z API:
    try:
        api_key = os.environ.get("API_KEY")

        # Stwórz URL z nazwą firmy i kluczem API:
        # ...quote_plus() - bierze symbol oznaczający firmę i konwertuje go do postaci bezpiecznej dla URL;
        # np. '/El Niño/' -> '%2FEl+Ni%C3%B1o%2F'
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"

        # zapisz odpowiedź serwera w zmiennej response:
        response = requests.get(url)

        # jeśli pojawi się błąd podczas pobierania obiektu z URL, zwróć obiekt HTTPError który wyjaśni, co się stało:
        response.raise_for_status()

    except requests.RequestException:
        return None

    # Przetwórz odpowiedź na zmienne:
    try:
        # Zamień odpowiedź serwera na obiekt JSON o nazwie quote,
        # wyciągnij z niego 3 wartości i zwróć z naszymi krótszymi nazwami: name, price i symbol:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"],
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
