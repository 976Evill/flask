from flask import Flask
from flask import request
from flask import g
from time import time

from werkzeug.exceptions import BadRequest
app = Flask(__name__)


@app.route("/")
def index():
    return 'First Flask Page'


@app.route('/hello')
def hello():
    return 'Hello, World again ;)'






