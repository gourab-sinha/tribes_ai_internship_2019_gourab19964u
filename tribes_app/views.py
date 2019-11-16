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
from neo4j import GraphDatabase
import json
import codecs
import os
# -------------------------------------------------
# Graph Database Connection and Session
# -------------------------------------------------
uri = "bolt://localhost:7687"
graph = GraphDatabase.driver(uri,auth=("neo4j","Gaurabh@1234"))
session = graph.session()

# -------------------------------------------------
# Flask Instance
# -------------------------------------------------
app = Flask(__name__)

# JSON File load
path = os.path.dirname(os.path.abspath(__file__))
sample = os.path.join(path,'sample.json')
payload = json.load(codecs.open(sample, 'r', 'utf-8-sig'))["payload"]


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

