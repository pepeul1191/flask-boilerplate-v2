#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, session
from main.constants import constants

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
  return 'home'
