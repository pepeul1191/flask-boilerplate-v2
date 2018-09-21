#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from sqlalchemy.sql import select
from main.databases import engine_accesos, session_accesos
from .models import Permiso
from main.middlewares import check_csrf

permiso_routes = Blueprint('permiso_routes', __name__)

@permiso_routes.route('/accesos/permiso/listar', methods=['GET'])
@check_csrf
def listar():
  rpta = None
  status = 200
  try:
    conn = engine_accesos.connect()
    stmt = select([Permiso])
    rs = conn.execute(stmt)
    rpta = [dict(r) for r in conn.execute(stmt)]
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en listar los permisos del sistema',
        str(e)
      ],
    }
    status = 500
  return json.dumps(rpta), status


@permiso_routes.route('/accesos/permiso/guardar', methods=['POST'])
@check_csrf
def guardar():
  status = 200
  data = json.loads(request.form['data'])
  nuevos = data['nuevos']
  editados = data['editados']
  eliminados = data['eliminados']
  array_nuevos = []
  rpta = None
  session = session_accesos()
  try:
    if len(nuevos) != 0:
      for nuevo in nuevos:
        temp_id = nuevo['id']
        s = Permiso(
          nombre = nuevo['nombre'],
          llave = nuevo['llave'],
        )
        session.add(s)
        session.flush()
        temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
        array_nuevos.append(temp)
    if len(editados) != 0:
      for editado in editados:
        session.query(Permiso).filter_by(id = editado['id']).update({
          'nombre': editado['nombre'],
          'llave': editado['llave'],
        })
    if len(eliminados) != 0:
      for id in eliminados:
        session.query(Permiso).filter_by(id = id).delete()
    session.commit()
    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha registrado los cambios en los permisos del sistema',
        array_nuevos
      ]
    }
  except Exception as e:
    status = 500
    session.rollback()
    rpta = {
      'tipo_mensaje' : 'error',
      'mensaje' : [
        'Se ha producido un error en guardar los permisos del sistema',
        str(e)
      ]
    }
  return json.dumps(rpta), status
