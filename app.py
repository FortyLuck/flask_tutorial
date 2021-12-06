#! /usr/bin/python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Dmitry!</p>"
    
@app.route("/bot", methods=["POST"])
def bot():
    if request.json:
        print(request.json)
        return request.json
    
    return "It's not json"