#!/usr/bin/python

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/FlaskApp")

from flaskapp import app as application