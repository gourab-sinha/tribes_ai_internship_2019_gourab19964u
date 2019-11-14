#!/usr/bin/env python3
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from tribes_app import app
import os

app.secret_key = os.urandom(24)
app.debug = True
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=5000)