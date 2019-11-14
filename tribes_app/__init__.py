#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from .views import app
from .models import graph

# -------------------------------------------------
# Constraints
# -------------------------------------------------
graph.schema.create_uniqueness_constraint("Team", "team_id")
graph.schema.create_uniqueness_constraint("Sport", "sport_id")
graph.schema.create_uniqueness_constraint("Match", "match_id")
graph.schema.create_uniqueness_constraint("City", "city_id")
graph.schema.create_uniqueness_constraint("State", "match_id")
graph.schema.create_uniqueness_constraint("Ground", "ground_id")
graph.schema.create_uniqueness_constraint("Player", "player_id")



