#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ._departamento import departamento_routes
from ._provincia import provincia_routes
from ._distrito import distrito_routes

blueprints = [
  departamento_routes,
  provincia_routes,
  distrito_routes,
]
