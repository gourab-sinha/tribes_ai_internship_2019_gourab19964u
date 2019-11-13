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
from py2neo import (GraphDatabase,
					Graph,
					Node,
					Relationship)
from datetime import datetime
import json
import codecs

# -------------------------------------------------
# Flask Instance
# -------------------------------------------------
app = Flask(__name__)

# -------------------------------------------------
# Graph Instance
# -------------------------------------------------
graph = Graph()

# Load JSON file
payload = json.load(codecs.open('sample.json', 'r', 'utf-8-sig'))

# Unique Constraints
# def createUniqueConstraint(label, property):
# 	query = "CREATE CONSTRAINT ON (n:{label}) ASSERT n.{property} IS UNIQUE"
# 	query = query.format(label=label, property=property)
# 	graph.cypher.execute(query)

# createUniqueConstraint("Team","id")
# createUniqueConstraint("Sport","id")
# createUniqueConstraint("City","id")
# createUniqueConstraint("State","id")
# createUniqueConstraint("Ground","id")
# createUniqueConstraint("Player","id")
# createUniqueConstraint("Match","id")

# Node Creation
# class Nodes:
# 	def createTeamNode(teamNode):
# 	def createSportNode(sportNode):
# 	def createGroundNode(groundNode):
# 	def createCountryNode(countryNode):
# 	def createStateNode(stateNode):
# 	def createMatchNode(matchNode):
# 	def createCityNode(cityNode):
# 	def createPlayerNode(playerNode):	

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "Gaurabh@1234"))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.1', port=8000)