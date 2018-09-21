#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
import json
from flask import Blueprint, render_template, request, session, redirect
from main.constants import constants
from main.middlewares import session_false, session_true
from .helpers import index_css, index_js

accesos_view = Blueprint('accesos_view', __name__)

@accesos_view.route('/accesos/', methods=['GET'])
@session_false
def index():
  locals = {
    'title': 'Accesos',
    'mensaje': '',
    'constants': constants,
    'csss': index_css(),
    'jss': index_js(),
    'data': json.dumps({
      'modulo' : 'Accesos',
    }),
    'menu': json.dumps([
      {
        'url' : 'accesos/',
        'nombre' : 'Accesos'
      },
    ]),
    'items': json.dumps([
      {
        'subtitulo':'Opciones',
        'items':
		  [
		    {
              'item':'Gestión de Menu',
              'url':'accesos/#/modulo'
            },
            {
              'item':'Gestión de Permisos',
              'url':'accesos/#/permiso'
            },
            {
              'item':'Gestión de Roles',
              'url':'accesos/#/rol'
            },
            {
              'item':'Gestión de Usuarios',
              'url':'accesos/#/usuario'
            },
		  ]
	  },
    ]),
  }
  return render_template('accesos/index.html', locals = locals)
