# -*- coding: utf-8 -*-
__author__ = 'viach_os'

from app import app, render_template, request
import forms


def index():
    pass

@app.route("/card", methods=['GET', 'POST'])
def card():
    form = forms.CardForm()
    result = None
    if form.validate_on_submit():
        result = form.process_input()
    return render_template('interaction.html', title='Card', form=form, result=result)


"""
def output_card():
    return card('POST')

@app.route("/card", methods=['GET'])
def input_card():
    return card('GET')
"""