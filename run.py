# -*- coding: utf-8 -*-
from app import app

app.run(debug=app.config['DEBUG'], port=app.config['SERVER_PORT'])
        #, extra_files=app.config['DATABASE'])
