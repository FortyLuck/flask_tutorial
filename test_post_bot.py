import pytest
import json

import app

NONE_DATA = None
EMPTY_DATA = {}
BASE_DATA = {
    "responseId": "response-id",
    "session": "projects/project-id/agent/sessions/session-id",
    "queryResult": {
        "queryText": "End-user expression",
        "parameters": {
            "param-name": "param-value"
        },
        "allRequiredParamsPresent": True,
        "fulfillmentText": "Response configured for matched intent",
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        "Response configured for matched intent"
                    ]
                }
            }
        ],
        "outputContexts": [
            {
                "name": "projects/project-id/agent/sessions/session-id/contexts/context-name",
                "lifespanCount": 5,
                "parameters": {
                        "param-name": "param-value"
                }
            }
        ],
        "intent": {
            "name": "projects/project-id/agent/intents/intent-id",
            "displayName": "matched-intent-name"
        },
        "intentDetectionConfidence": 1,
        "diagnosticInfo": {},
        "languageCode": "en"
    },
    "originalDetectIntentRequest": {}
}


def test_simple_post():

    json_str = json.dumps(BASE_DATA)

    assert app.parse_request(json_str) == BASE_DATA


def test_get_session_id():
    json_data = BASE_DATA.copy()
    expected_session_id = '123456'
    expected_project_id = 'proj-23118'

    json_data['session'] = 'projects/{}/agent/sessions/{}'.format(
        expected_project_id, expected_session_id)

    assert app.get_session_id(json_data) == expected_session_id
    assert app.get_project_id(json_data) == expected_project_id


def test_get_query_text():
    assert app.get_query_text(BASE_DATA) == 'End-user expression'
    assert app.get_query_text(NONE_DATA) == None
    assert app.get_query_text(EMPTY_DATA) == None


def test_format_text_message():
    message = "Simple example message"
    expected_data = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                         message
                    ]
                }
            }
        ]
    }

    assert app.format_text_response(message) == expected_data

def test_get_intent_name():
    assert app.get_intent_name(BASE_DATA) == 'matched-intent-name'