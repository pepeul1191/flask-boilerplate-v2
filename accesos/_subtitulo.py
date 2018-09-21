#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from sqlalchemy.sql import select
from main.databases import engine_accesos, session_accesos
from .models import Subtitulo
from main.middlewares import check_csrf

subtitulo_routes = Blueprint('subtitulo_routes', __name__)

@subtitulo_routes.route('/accesos/subtitulo/listar/<int:modulo_id>', methods=['GET'])
@check_csrf
def listar(modulo_id):
  rpta = None
  status = 200
  try:
    conn = engine_accesos.connect()
    stmt = select([Subtitulo]).where(Subtitulo.modulo_id == modulo_id)
    rs = conn.execute(stmt)
    rpta = [dict(r) for r in conn.execute(stmt)]
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en listar los subtítulos del módulo',
        str(e)
      ],
    }
    status = 500
  return json.dumps(rpta), status

@subtitulo_routes.route('/accesos/subtitulo/guardar', methods=['POST'])
@check_csrf
def guardar():
  status = 200
  data = json.loads(request.form['data'])
  nuevos = data['nuevos']
  editados = data['editados']
  eliminados = data['eliminados']
  modulo_id = data['extra']['modulo_id']
  array_nuevos = []
  rpta = None
  session = session_accesos()
  try:
    if len(nuevos) != 0:
      for nuevo in nuevos:
        temp_id = nuevo['id']
        s = Subtitulo(
          nombre = nuevo['nombre'],
          modulo_id = modulo_id,
        )
        session.add(s)
        session.flush()
        temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
        array_nuevos.append(temp)
    if len(editados) != 0:
      for editado in editados:
        session.query(Subtitulo).filter_by(id = editado['id']).update({
          'nombre': editado['nombre'],
        })
    if len(eliminados) != 0:
      for id in eliminados:
        session.query(Subtitulo).filter_by(id = id).delete()
    session.commit()
    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha registrado los cambios en los subtítulos del módulo',
        array_nuevos
      ]
    }
  except Exception as e:
    status = 500
    session.rollback()
    rpta = {
      'tipo_mensaje' : 'error',
      'mensaje' : [
        'Se ha producido un error en guardar los subtítulos del módulo',
        str(e)
      ]
    }
  return json.dumps(rpta), status
