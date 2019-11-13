#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   jsonify,
                   url_for,
                   flash,
                   make_response)
from datetime import datetime
import json
import codecs

# -------------------------------------------------
# Flask Instance
# -------------------------------------------------
app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def HomePage():
    homepage = '''<html>
                    <head>
                        <tiltle>Homepage</title>
                    </head>
                    <body>
                        <h1>Hello World</h1>
                    </body>
                </html>'''
    return homepage;

# Load JSON file
#payload = json.load(codecs.open('sample.json', 'r', 'utf-8-sig'))
