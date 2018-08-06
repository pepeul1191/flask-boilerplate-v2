#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
from flask import Blueprint, render_template, request, session, redirect
from main.constants import constants
from main.middlewares import session_false, session_true
from .helpers import index_css, index_js

login_view = Blueprint('login_view', __name__)

@login_view.route('/login', methods=['GET'])
@session_false
def index():
  locals = {
    'title': 'Bienvenido',
    'mensaje': '',
    'constants': constants,
    'csss': index_css(),
    'jss': index_js(),
  }
  return render_template('login/index.html', locals = locals)

@login_view.route('/login/acceder', methods=['POST'])
def acceder():
  mensaje = ''
  continuar = True
  try:
    usuario = request.form['usuario']
    # validar usuario/sistema
    r1 = requests.post(
      constants['servicios']['accesos']['url'] + 'sistema/usuario/validar',
      headers = {
        constants['servicios']['accesos']['key'] : constants['servicios']['accesos']['secret'],
      },
      data = {
        'usuario' : usuario,
        'sistema_id' : constants['sistema_id'],
      }
    )
    if r1.status_code == 200:
      if r1.text != '1':
        continuar = False
        mensaje = 'Usuario no se encuentra registrado en el sistema'
    else:
      continuar = False
      mensaje = 'Se ha producido un error no esperado al validar usuario/sistema'
  except ConnectionError as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'No se puede acceder al servicio de validación de usuario/sistema',
        str(e)
      ],
    }
    print(rpta)
    mensaje = rpta['mensaje'][0]
    continuar = False
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error no controlado al validar usuario/sistema',
        str(e)
      ],
    }
    print(rpta)
    mensaje = rpta['mensaje'][0]
    continuar = False
  # validar usuario/contrasenia
  if continuar == True:
    try:
      usuario = request.form['usuario']
      contrasenia = request.form['contrasenia']
      # validar usuario/sistema
      r2 = requests.post(
        constants['servicios']['accesos']['url'] + 'usuario/externo/validar',
        headers = {
          constants['servicios']['accesos']['key'] : constants['servicios']['accesos']['secret'],
        },
        data = {
          'usuario' : usuario,
          'contrasenia' : contrasenia,
        }
      )
      if r2.status_code == 200:
        if r2.text != '1':
          continuar = False
          mensaje = 'Usuario y/o contraseña no coincide'
        else:
          x = 1
          # habilitar session
          session['usuario'] = usuario
          session['estado'] = 'activo'
          session['tiempo'] = str(datetime.datetime.now())
          return redirect('')
      else:
        continuar = False
        mensaje = 'Se ha producido un error no esperado al validar usuario/contraseña'
    except ConnectionError as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'No se puede acceder al servicio de validación de usuario/contrasenia',
          str(e)
        ],
      }
      print(rpta)
      mensaje = rpta['mensaje'][0]
      continuar = False
    except Exception as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'Se ha producido un error no controlado al validar usuario/contrasenia',
          str(e)
        ],
      }
      print(rpta)
      mensaje = rpta['mensaje'][0]
      continuar = False
  locals = {
    'title': 'Login',
    'mensaje': mensaje,
    'constants': constants,
    'csss': index_css(),
    'jss': index_js(),
  }
  return render_template('login/index.html', locals = locals), 500

@login_view.route('/ver', methods=['GET'])
@session_true
def ver():
    rpta = ''
    if not session['usuario']:
      rpta = '<h1>El usuario no se encuentra logueado</h1>'
    else:
      rpta = '<h1>Usuario Logeado</h1><ul><li>' + str(session['usuario']) + '</li><li>' +  str(session['tiempo']) + '</li><li>' + str(session['estado']) + '</li></ul>'
    return rpta

@login_view.route('/salir', methods=['GET'])
def salir():
  session.clear()
  return redirect('/login')
