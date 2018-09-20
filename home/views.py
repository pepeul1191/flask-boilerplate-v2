#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from main.constants import constants
from main.middlewares import session_true

home_view = Blueprint('home_view', __name__)

@home_view.route('/', methods=['GET'])
@session_true
def index():
  return '<a href="' + constants['base_url'] + 'accesos/">Ir a Accesos</a>'

@home_view.route('/x', methods=['GET'])
def xd():
  return 'xd'
