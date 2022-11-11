# Program Flask uruchamiamy z terminala poleceniem:
# cd CS50X/09_05__zapisy__porzadki_i_petle_w_Jinja
#
# auto restart serwera przy każdym zapisie:
# flask --debug run


from flask import Flask, render_template, request


app = Flask("__name__")

# Poczyśćmy kod. Poprzednio w dwóch plikach wymienialiśmy sporty.
# Zamieńmy je na "stałą", czyli zmienną pisaną wielkimi literami,
# której nie należy ruszać:

SPORTS = ["Basketball", "Soccer", "Frisbee"]


@app.route("/")
def index():

    # przekazujemy do index.html naszą zmienną SPORTS:
    return render_template("index.html", sports=SPORTS)


@app.route("/register/", methods=["POST"])
def register():

    # Error checking:
    print(request.form.get("sport"))
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")

    # Jeśi wszystko jest ok:
    return render_template("success.html")
