# @name: __init__.py
# @creation_date: 2023-10-24
# @license: The MIT License <https://opensource.org/licenses/MIT>
# @author: Simon Bowie <simon.bowie.19@gmail.com>
# @purpose: Initialises the app
# @acknowledgements:

from flask import Flask, render_template, request
from flask_moment import Moment
import requests
import urllib.request, json
import os
import markdown
import re
import random

# initiate Moment for datetime functions
moment = Moment()

app = Flask(__name__)

moment.init_app(app)

@app.route('/')
def index():
    with open('app/content/thoughts.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template('index.html', html=html)

@app.route('/what')
def what():
    with open('app/content/about.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
        html = re.sub("<h1.*?>\s", "", html)
        html = re.sub("<h2>about</h2>", "<h2>what is this?</h2>", html)
    return render_template('what.html', html=html)

@app.route('/thoughts')
def thoughts():
    with open('app/content/thoughts.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template('thoughts.html', html=html)

@app.route('/sounds')
def sounds():
    with open('app/content/sounds.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template('sounds.html', html=html)    