# -*- coding: utf-8 -*-
__author__ = 'viach_os'

from app import app, render_template


@app.route("/")
def index():
    return render_template('interaction.html', title='Card', form='Form', result='Result')


@app.route("/card", methods=['GET', 'POST'])
def card():
    pass


def output_card():
    pass


def input_card():
    pass