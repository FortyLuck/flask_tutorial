#! /usr/bin/python3

from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Dmitry!</p>"


@app.route("/bot", methods=["POST"])
def bot():
    try:
        if request.json:
            return format_text_response('{}: {}'.format(get_intent_name(request.json), get_query_text(request.json)))
    except:
        return format_text_response("Error happened")


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


def format_text_response(msg):
    return {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        msg
                    ]
                }
            }
        ]
    }

def get_intent_name(data):
    try:
        return data['queryResult']['intent']['displayName']
    except:
        return None
