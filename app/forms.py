# -*- coding: utf-8 -*-
__author__ = 'viach_os'

from flask.ext.wtf import Form
from wtforms.fields import TextField, SelectField, SubmitField
from wtforms.validators import Required


class CardForm(Form):
    """
    Form for card search input
    """
    hall = SelectField('Hall', validators=[Required()],
                       choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    #: TODO: add number validator
    card = TextField('Card Number', validators=[Required(), ])

    def process_input(self):
        #: load hall

        #: allocate card for this hall

        #: if card are allocated
            #: return result
        pass





