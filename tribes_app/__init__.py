#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from .views import app
from .models import graph

# -------------------------------------------------
# Constraints
# -------------------------------------------------
# graph.schema.create_uniqueness_constraint("User", "username")
# graph.schema.create_uniqueness_constraint("Tag", "name")
# graph.schema.create_uniqueness_constraint("Post", "id")
