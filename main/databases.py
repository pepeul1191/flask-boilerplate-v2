#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine_ubicaciones = create_engine('sqlite:///db/ubicaciones.db')
session_ubicaciones = sessionmaker()
session_ubicaciones.configure(bind=engine_ubicaciones)
