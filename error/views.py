#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from main.constants import constants
from .helpers import error_access_css, error_access_js

error_view = Blueprint('error_view', __name__)

@error_view.route('/error/access/<int:numero_error>', methods=['GET'])
def access(numero_error):
  errores = {
    '404' : {
      'mensaje': 'Archivo no encontrado',
      'numero': '404',
      'descripcion': 'La página que busca no se encuentra en el servidor',
    },
    '505' : {
      'mensaje': 'Acceso restringido',
      'numero': '505',
      'descripcion': 'Necesita estar logueado',
    },
  }
  locals = {
    'title': 'Error',
    'mensaje': '',
    'constants': constants,
    'csss': error_access_css(),
    'jss': error_access_js(),
    'mensaje': errores[str(numero_error)]['mensaje'],
    'numero': errores[str(numero_error)]['numero'],
    'descripcion': errores[str(numero_error)]['descripcion'],
  }
  return render_template('error/access.html', locals = locals), numero_error
