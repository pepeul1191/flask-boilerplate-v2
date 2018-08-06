#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from main.constants import constants
from .helpers import index_css, index_js

login_view = Blueprint('login_view', __name__)

@login_view.route('/login', methods=['GET'])
def index():
  locals = {
    'title': 'Bienvenido',
    'mensaje': '',
    'constants': constants,
    'csss': index_css(),
    'jss': index_js(),
  }
  return render_template('login/index.html', locals = locals)
