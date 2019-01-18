#!/usr/bin/python3
from flask import Flask, render_template
from services.SuggestedQueries import SuggestedQueries

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<keywords>")
def hello(keywords=None):
    query = SuggestedQueries.get_suggested_queries(keywords)
    return str(query)


if __name__ == "__main__": 
    app.run()