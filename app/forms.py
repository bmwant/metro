# -*- coding: utf-8 -*-
__author__ = 'viach_os'

from flask.ext.wtf import Form
from wtforms.fields import TextField, SelectField, SubmitField
from wtforms.validators import Required

from app import app, server, dataloader, flash

#: TODO: set lazy
def get_halls():
    """
    Ger list of tuples with hall code and name

    Look at dumps and nodes file structure, and you will understand this code :)
    """
    dumps = server.get_list_of_dir(app.config['DUMP_DIR'])
    nodes = iter(server.get_file_content('nodes.name'))


    halls = []
    node = nodes.next().split(';')
    for item in dumps:
        raw_item = item.split('.')
        code = raw_item[1]

        if code > node[0]:
            node = nodes.next().split(';')

        halls.append(('.'.join(raw_item[1:3]),
                      ': '.join((node[-1][:-1].decode("utf-8", "replace"),
                                raw_item[2]))))
    return halls


class CardForm(Form):
    """
    Form for card search input
    """
    hall = SelectField('Hall', validators=[Required()],
                       choices=get_halls())
    #: TODO: add number validator
    card = TextField('Card Number', validators=[Required()])

    def process_input(self):
        """

        """
        filename = '%s/adbk.%s.rar' % (app.config['DUMP_DIR'], self.hall.data)
        db_path = server.download_file(filename,
                                   ''.join([dataloader.DB_ALIAS, '.rar']))

        if db_path:
            unrar_path = dataloader.unrar(db_path, dataloader.DB_EXT)
            dataloader.move_db(unrar_path)
            flash('%s loaded into %s' % (filename, db_path))
        else:
            flash('File exists')

        #: allocate card for this hall

        #: if card are allocated
            #: return result
        pass





