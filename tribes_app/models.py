#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from py2neo import Graph, Node, Relationship
from datetime import datetime
import os
import uuid

# -------------------------------------------------
# Graph Database Connection
# -------------------------------------------------
url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')

# Graph Instance
graph = Graph(url + '/db/data/', username=username, password=password)

