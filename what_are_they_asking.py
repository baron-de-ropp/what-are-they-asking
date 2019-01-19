#!/usr/bin/python3
from flask import Flask, render_template, request, url_for, redirect
from services.TopicsProvider import TopicsProvider
import json
import requests as r

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/questions/", methods=["POST"])
def questions():
    return redirect(url_for("questions_get", keywords=request.form["keywords"]))


@app.route("/qustions/<keywords>")
def questions_get(keywords):
    model = TopicsProvider.get_topics(keywords)
    return render_template("questions.html", model=model)


if __name__ == "__main__": 
    app.run()