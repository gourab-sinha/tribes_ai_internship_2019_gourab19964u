#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from .views import app
from .models import graph

# -------------------------------------------------
# Constraints
# -------------------------------------------------
def create_unique_constraint(label,property):
	query = "CREATE CONSTRAINT ON (n:{label}) ASSERT n.property IS UNIQUE"
	query = query.format(label=label,property=property)
	session = graph.session()
	session.run(query)
	session.close()

create_unique_constraint("Team","team_id")
create_unique_constraint("Sport","sport_id")
create_unique_constraint("City","city_id")
create_unique_constraint("State","state_id")
create_unique_constraint("Ground","ground_id")
create_unique_constraint("Player","player_id")
create_unique_constraint("Match","match_id")
