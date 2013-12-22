__author__ = 'viach_os'

from flask import Flask, render_template
app = Flask(__name__)

app.config.from_object('config')

from app import views
