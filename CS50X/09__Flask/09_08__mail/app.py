# PIP install flask_mail

import os
import re

from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)


# Aplikacja zapisuje użytkownika na zajęcia i wysyła mu mail z potwierdzeniem.
# Mail z którego idzie potwierdzenie konfigurujemy poniżej.
# Mail na który przyjdzie potwierdzenie podaje się w formularzu.

# W ustawieniach konta Google generujesz "Hasło do aplikacji".
# To hasło podajesz w miejsce MAIL_PASSWORD. Jest w keepass.

# Możesz je podać w cudzysłowiu, w kodzie. TO FATALNY POMYSŁ.
# Takie hasło może przypadkowo wyciec.
# Dlatego poniżej stosujemy zmienne środowiskowe dla użytkownika Marek (nie systemowe).
# Tworzymy takie trzy pary klucz-wartość i restartujemy system:

# MAIL_DEFAULT_SENDER = ‘“Marek” <mail@google.com>’
# MAIL_PASSWORD = ‘password’
# MAIL_USERNAME = ‘mail@google.com’

app.config["MAIL_DEFAULT_SENDER"] = os.environ["MAIL_DEFAULT_SENDER"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
mail = Mail(app)

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    name = request.form.get("name")
    email = request.form.get("email")
    sport = request.form.get("sport")
    if not name or not email or sport not in SPORTS:
        return render_template("failure.html")

    # Send email
    message = Message("You are registered!", recipients=[email])
    mail.send(message)

    # Confirm registration
    return render_template("success.html")
