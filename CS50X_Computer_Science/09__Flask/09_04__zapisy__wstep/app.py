# Program Flask uruchamiamy z terminala poleceniem:
# cd CS50X/09_04__zapisy__wstep
#
# auto restart serwera przy każdym zapisie:
# flask --debug run


from flask import Flask, render_template, request


app = Flask("__name__")


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/register/", methods=["POST"])
def register():

    # Error checking
    # jeśli user zapomniał podać nazwisko lub wybrał sport spoza tych trzech..
    print(request.form.get("sport"))
    if not request.form.get("name") or request.form.get("sport") not in [
        "Basketball",
        "Soccer",
        "Frisbee",
    ]:
        return render_template("failure.html")

    # Jeśi wszystko jest ok:
    return render_template("success.html")
