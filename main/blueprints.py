#!/usr/bin/env python
# -*- coding: utf-8 -*-
from home.blueprints import blueprints as home_blueprints
from home.views import home_view

def register(app):
  modules_blueprints = []
  #registrar blueprint of apps
  modules_blueprints.append(home_blueprints)
  #cargar blueprints a app
  for blueprints in modules_blueprints:
    for blueprint in blueprints:
      app.register_blueprint(blueprint)
