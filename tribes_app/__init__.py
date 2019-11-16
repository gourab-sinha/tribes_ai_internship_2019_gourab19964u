#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from .views import app,graph,payload
import json
import codecs
import os
from .models import Team,Member,Ground


# JSON File load
path = os.path.dirname(os.path.abspath(__file__))
sample = os.path.join(path,'sample.json')
payload = json.load(codecs.open(sample, 'r', 'utf-8-sig'))["payload"]

teams = payload["teams"]
for team in teams:
	teamObj = Team(team)
	teamObj.createteam()

session =  graph.session()
session.close()
