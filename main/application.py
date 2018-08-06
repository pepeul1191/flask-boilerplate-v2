#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from .blueprints import register

app = Flask(__name__, template_folder = '../templates')
register(app)

@app.route('/hello')
def hello_world():
  return 'Hello, World???!'

@app.after_request
def apply_caching(response):
  response.headers['Server'] = 'Werkzeug/0.14.1 Python/3.5.2; Ubuntu;'
  return response
