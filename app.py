#!/usr/bin/python3
from flask import Flask, render_template, request, url_for, redirect
import services.TopicsProvider as tp

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/questions/", methods=["POST"])
def questions():
    return redirect(url_for("questions_get", keywords=request.form["keywords"]))


@app.route("/questions/<keywords>")
def questions_get(keywords):
    model = tp.get_topics(keywords)
    return render_template("questions.html", model=model)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)