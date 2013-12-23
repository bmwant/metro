__author__ = 'viach_os'

from flask import Flask, render_template, flash,request
app = Flask(__name__)

app.config.from_object('config')

import views
#: TODO: app import system, package
