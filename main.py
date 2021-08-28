from flask import flask
from flask.app import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return "Hello Word!"