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
# path = os.path.dirname(os.path.abspath(__file__))
# sample = os.path.join(path,'sample.json')
# payload = json.load(codecs.open(sample, 'r', 'utf-8-sig'))["payload"]
@app.route('/teams/')
@app.route('/team/')
@app.route('/teams/')
@app.route('/Teams/')
def Teams():
  query = '''MATCH(n:Team) RETURN n.team_name'''
  result = session.run(query).values()
  teams = list()
  for team in result:
    teams.append(str(team[0]))
  for team in teams:
    print(team)
  #return '''<html><body>Hello</body></html>'''
  return render_template('teams.html', teams = teams)

@app.route('/member/<string:team_name>')
@app.route('/members/<string:team_name>')
@app.route('/members/<string:team_name>')
@app.route('/Members/<string:team_name>')
def Members(team_name):
  print(team_name)
  query = '''Match(:Team{team_name:'%s'})--(p:Player) 
             RETURN p.player_name,p.age,p.player_id'''%(str(team_name))
  result = session.run(query).values()
  playerlist = list()
  for player in result:
    playerlist.append(player)

  #return '''<html><body>Hello</body></html>'''
  return render_template('members.html', members = playerlist, team_name = str(team_name))

@app.route('/grounds/')
def Grounds():
  query = '''MATCH(n:Ground) RETURN n.ground_name,n.ground_id,n.host_international'''
  result = session.run(query).values()
  print(result)
  groundlist = list()
  for ground in result:
    groundlist.append(ground)

  return render_template('grounds.html', grounds = groundlist)

