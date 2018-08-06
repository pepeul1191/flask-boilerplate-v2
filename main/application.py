#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, session
from .blueprints import register
from .constants import constants
from .templates import load_css, load_js

app = Flask(
  __name__,
  template_folder = '../templates',
  static_folder='../static',
  static_url_path='/static'
)
#registrar blueprints
register(app)
#configuración de session
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = constants['key']
#configur de filters/helpers en los templates
@app.context_processor
def utility_processor():
  return dict(load_css = load_css, load_js = load_js)
# una ruta de prueba
@app.route('/hello')
def hello_world():
  return 'Hello, World???!'
#setear cabeceras
@app.after_request
def apply_caching(response):
  response.headers['Server'] = 'Werkzeug/0.14.1 Python/3.5.2; Ubuntu;'
  return response
