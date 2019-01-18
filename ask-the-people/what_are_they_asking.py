#!/usr/bin/python3
from flask import Flask, render_template, request, url_for
from services.SuggestedQueries import SuggestedQueries

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/questions/", methods=["POST", "GET"])
def questions():
    if request.method == "POST":
        query = SuggestedQueries.get_suggested_queries(request.form["keywords"])
        return str(query)
    else:
        return "put in some keywords and you'll get questions"



if __name__ == "__main__": 
    app.run()