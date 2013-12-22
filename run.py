# -*- coding: utf-8 -*-
__author__ = 'viach_os'

from app import app

app.run(debug=app.config['DEBUG'], port=app.config['SERVER_PORT'])
