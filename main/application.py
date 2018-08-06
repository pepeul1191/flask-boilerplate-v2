#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from home.views import home

app = Flask(__name__)
app.register_blueprint(home)

@app.route('/hello')
def hello_world():
  return 'Hello, World???!'

@app.after_request
def apply_caching(response):
  response.headers['Server'] = 'Werkzeug/0.14.1 Python/3.5.2; Ubuntu;'
  return response
