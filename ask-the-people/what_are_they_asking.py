#!/usr/bin/python3
from flask import Flask, render_template, request, url_for
from services.TopicsProvider import TopicsProvider
import json

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/questions/", methods=["POST", "GET"])
def questions():
    if request.method == "POST":
        model = TopicsProvider.get_topics(request.form["keywords"])
        return render_template("questions.html", model=model)
    else:
        return "put in some keywords and you'll get questions"



if __name__ == "__main__": 
    app.run()