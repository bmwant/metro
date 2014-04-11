# -*- coding: utf-8 -*-
from app import app, render_template, request, redirect
import forms
import pprint

@app.route("/")
def index():
    return redirect('/card')


@app.route("/card", methods=['GET', 'POST'])
def card():
    form = forms.CardForm()
    result = None
    if form.validate_on_submit():
        result = form.process_input()
    return render_template('card_table.html', title='Card', form=form,
                           result=result,
                           link='card')


@app.route("/hall", methods=['GET', 'POST'])
def hall():
    form = forms.HallForm()
    result, summ = None, None
    if form.validate_on_submit():
        result, summ = form.process_input()
    return render_template('hall_table.html', title='Hall', form=form,
                           result=result, summ=summ, link='hall')


@app.route("/reports", methods=['GET', 'POST'])
def reports():
    halls = forms.get_halls()
    h = forms.get_unique_halls()
    halls_statistic = forms.get_halls_statistic()
    return render_template('reports.html', title='Reports',
                           halls=halls_statistic,
                           stations=h,
                           link='reports')


@app.route("/charts", methods=['GET', 'POST'])
def charts():
    pass