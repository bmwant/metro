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
    return render_template('card_table.html', title='Card', form=form, result=result)

@app.route("/hall", methods=['GET', 'POST'])
def hall():
    form = forms.HallForm()
    result, summ = None, None
    if form.validate_on_submit():
        result, summ = form.process_input()
    return render_template('hall_table.html', title='Hall', form=form, result=result, summ=summ)
