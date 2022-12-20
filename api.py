from flask import Flask, request
from marshmallow import ValidationError
from model import CreateCredSchema, UpdateCredSchema
import json
app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():
    schema = CreateCredSchema()
    try:
        x = schema.load(request.get_json())
    except ValidationError as e:
        return e.messages
    print(x)
    return x


@app.route("/", methods=['PUT'])
def hello_worla():
    schema = UpdateCredSchema()
    try:
        x = schema.load(request.get_json(),partial=True)
    except ValidationError as e:
        return e.messages
    print(x)
    return x
