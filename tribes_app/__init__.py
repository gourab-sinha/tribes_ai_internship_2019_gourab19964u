#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from .views import app,graph
import json
import codecs
import os
from .models import Team,Member,Ground,Match


# JSON File load
path = os.path.dirname(os.path.abspath(__file__))
sample = os.path.join(path, 'sample.json')
payload = json.load(codecs.open(sample, 'r', 'utf-8-sig'))["payload"]


def load_data(pay_load):
	teams = pay_load["teams"]
	for team in teams:
		team_obj = Team(team)
		team_obj.create_team()
	
	grounds = pay_load["grounds"]
	for ground in grounds:
		ground_obj = Ground(ground)
		ground_id = ground_obj.create_ground()
	
	sport = payload["sport"]
	sport_obj = Match(sport)
	sport_obj.create_match(teams)


load_data(payload)

session = graph.session()
session.close()
