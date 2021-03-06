#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from sqlalchemy.sql import select
from main.databases import engine_accesos, session_accesos
from .models import Item, VWModuloSubtituloItem
from main.middlewares import check_csrf

item_routes = Blueprint('item_routes', __name__)

@item_routes.route('/accesos/item/listar/<int:subtitulo_id>', methods=['GET'])
@check_csrf
def listar(subtitulo_id):
  rpta = None
  status = 200
  try:
    conn = engine_accesos.connect()
    stmt = select([Item]).where(Item.subtitulo_id == subtitulo_id)
    rs = conn.execute(stmt)
    rpta = [dict(r) for r in conn.execute(stmt)]
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en listar los items del subtítulo',
        str(e)
      ],
    }
    status = 500
  return json.dumps(rpta), status

@item_routes.route('/accesos/item/guardar', methods=['POST'])
@check_csrf
def guardar():
  status = 200
  data = json.loads(request.form['data'])
  nuevos = data['nuevos']
  editados = data['editados']
  eliminados = data['eliminados']
  subtitulo_id = data['extra']['subtitulo_id']
  array_nuevos = []
  rpta = None
  session = session_accesos()
  try:
    if len(nuevos) != 0:
      for nuevo in nuevos:
        temp_id = nuevo['id']
        s = Item(
          nombre = nuevo['nombre'],
          url = nuevo['url'],
          subtitulo_id = subtitulo_id,
        )
        session.add(s)
        session.flush()
        temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
        array_nuevos.append(temp)
    if len(editados) != 0:
      for editado in editados:
        session.query(Item).filter_by(id = editado['id']).update({
          'nombre': editado['nombre'],
          'url': editado['url'],
        })
    if len(eliminados) != 0:
      for id in eliminados:
        session.query(Item).filter_by(id = id).delete()
    session.commit()
    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha registrado los cambios en los items del subtítulo',
        array_nuevos
      ]
    }
  except Exception as e:
    status = 500
    session.rollback()
    rpta = {
      'tipo_mensaje' : 'error',
      'mensaje' : [
        'Se ha producido un error en guardar los items del subtítulo',
        str(e)
      ]
    }
  return json.dumps(rpta), status

"""
@item_view.route('/menu', method='GET')
@enable_cors
@headers
@check_csrf
def menu():
  rpta = None
  status = 200
  sistema_id = request.query.sistema_id
  modulo = request.query.modulo
  try:
    conn = engine.connect()
    rs = session_db().query(VWModuloSubtituloItem).filter_by(sistema_id = sistema_id, modulo = modulo)
    subtitulos = []
    subtitulos_temp = []
    items = []
    for r in rs:
      subtitulo = r.subtitulo
      if (subtitulo  in subtitulos) == False:
        subtitulos.append(subtitulo)
        i = {'subtitulo': r.subtitulo, 'items': []}
        items.append(i)
      t = {'subtitulo': r.subtitulo, 'item': r.item, 'url': r.url_item}
      subtitulos_temp.append(t)
    for subtitulo in subtitulos:
      for temp in subtitulos_temp:
        if(temp['subtitulo'] == subtitulo):
          i = {'item': temp['item'], 'url': temp['url']}
          for item in items:
            if subtitulo == item['subtitulo']:
              item['items'].append(i)
    rpta = items
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en listar el menú de los items del módulo',
        str(e)
      ],
    }
    status = 500
  return json.dumps(rpta), status

"""
