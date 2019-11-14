#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from neo4j import GraphDatabase
from datetime import datetime
import os
import uuid
import json
import codecs
# -------------------------------------------------
# Graph Database Connection and Session
# -------------------------------------------------
uri = "bolt://localhost:7687"
graph = GraphDatabase.driver(uri,auth=("neo4j","Gaurabh@1234"))
session = graph.session()

# JSON File load
path = os.path.dirname(os.path.abspath(__file__))
sample = os.path.join(path,'sample.json')
payload = json.load(codecs.open(sample, 'r', 'utf-8-sig'))
session.close()

