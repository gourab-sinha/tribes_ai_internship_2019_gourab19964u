#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from tribes_app import app
import os

# Application Configuration
app.secret_key = os.urandom(24)
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=5000, debug = True, use_reloader = True)