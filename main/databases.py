#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# ubicaciones
engine_ubicaciones = create_engine('sqlite:///db/ubicaciones.db')
session_ubicaciones = sessionmaker()
session_ubicaciones.configure(bind=engine_ubicaciones)
# accesos
engine_accesos = create_engine('sqlite:///db/accesos.db')
session_accesos = sessionmaker()
session_accesos.configure(bind=engine_accesos)
