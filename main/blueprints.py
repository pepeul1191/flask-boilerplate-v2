#!/usr/bin/env python
# -*- coding: utf-8 -*-
from home.blueprints import blueprints as home_blueprints
from login.blueprints import blueprints as login_blueprints
from error.blueprints import blueprints as error_blueprints
from ubicaciones.blueprints import blueprints as ubicaciones_blueprints

def register(app):
  modules_blueprints = []
  #registrar blueprint of apps
  modules_blueprints.append(home_blueprints)
  modules_blueprints.append(login_blueprints)
  modules_blueprints.append(error_blueprints)
  modules_blueprints.append(ubicaciones_blueprints)
  #cargar blueprints a app
  for blueprints in modules_blueprints:
    for blueprint in blueprints:
      app.register_blueprint(blueprint)
