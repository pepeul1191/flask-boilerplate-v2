#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from main.constants import constants

home_view = Blueprint('home_view', __name__)

@home_view.route('/', methods=['GET'])
def index():
  return 'home'

@home_view.route('/x', methods=['GET'])
def xd():
  return 'xd'
