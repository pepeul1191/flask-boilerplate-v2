#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .views import accesos_view
from ._modulo import modulo_routes

blueprints = [
  accesos_view,
  modulo_routes,
]
