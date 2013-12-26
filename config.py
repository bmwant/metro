# -*- coding: utf-8 -*-
__author__ = 'viach_os'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
DEBUG = True
SERVER_PORT = 5000
SECRET_KEY = 'aGGr'

SERVER = 'avms.dit.in.ua'
USERNAME = 'student'
PASSWORD = 'student'
DUMP_DIR = 'ADBK_dump20130225'
DATABASE = os.path.join(basedir, 'data', 'db.db3')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
SQLALCHEMY_META = os.path.join(basedir, 'metadata', 'meta.sql')
