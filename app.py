#! /usr/bin/python3

from flask import Flask, request
import json

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


def parse_request(data):
    return json.loads(data)

def get_session_id(data):
    try:
        return data['session'].split('/')[-1]
    except:
        return None

def get_project_id(data):
    try:
        return data['session'].split('/')[1]
    except:
        return None

def get_query_text(data):
    try:
        return data['queryResult']['queryText']
    except:
        return None
