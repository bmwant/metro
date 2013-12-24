__author__ = 'viach_os'

from flask import Flask, render_template, flash, request, g


app = Flask(__name__)

app.config.from_object('config')

import dataloader
server = dataloader.DataLoader(app.config['SERVER'], app.config['USERNAME'],
                               app.config['PASSWORD'])

import views




#: TODO: app import system, package
