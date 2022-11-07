# Program Flask uruchamiamy z terminala poleceniem:
# cd CS50X/09__Flask/09_02
# flask run

from flask import Flask, render_template, request


app = Flask("__name__")


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/greetings/")
def greetings():

    name = request.args.get("name")

    if name == None:
        name = "Stranger"

    return render_template("greetings.html", name=name)
