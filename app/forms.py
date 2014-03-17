# -*- coding: utf-8 -*-
__author__ = 'viach_os'

from flask.ext.wtf import Form
from wtforms.fields import TextField, SelectField, SubmitField
from wtforms.validators import Required

#: TODO: move logic from this
from sqlalchemy import and_
from sqlalchemy.sql import func


from app import app, server, dataloader, flash, models, database


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
    card_number = TextField('Card No', validators=[Required()])

    def process_input(self):
        """
        Download file with db from FTP and search in it
        """
        filename = '%s/adbk.%s.rar' % (app.config['DUMP_DIR'], self.hall.data)
        db_path = server.download_file(filename,
                                   ''.join([dataloader.DB_ALIAS, '.rar']))
        #: TODO: except broken pip - create new server

        if db_path:
            unrar_path = dataloader.unrar(db_path, dataloader.DB_EXT)
            dataloader.move_db(unrar_path)
            # import database #: rebind model
            # database.bind_models_to_database()
            flash('%s loaded into %s' % (filename, db_path))
        else:
            flash('Database file exists')

        result = models.MetroEvent.query.filter_by(cardno=self.card_number.data).all()
        flash('Found %s records' % len(result))

        return result


class HallForm(Form):
    hall = SelectField('Hall', validators=[Required()],
                       choices=get_halls())
    start_date = TextField('Start', validators=[Required()])
    end_date = TextField('End', validators=[Required()])

    def process_input(self):
        filename = '%s/adbk.%s.rar' % (app.config['DUMP_DIR'], self.hall.data)
        db_path = server.download_file(filename,
                                       ''.join([dataloader.DB_ALIAS, '.rar']))
        #: TODO: except broken pip - create new server

        if db_path:
            unrar_path = dataloader.unrar(db_path, dataloader.DB_EXT)
            dataloader.move_db(unrar_path)
            # import database #: rebind model
            # database.bind_models_to_database()
            flash('%s loaded into %s' % (filename, db_path))
        else:
            flash('Database file exists')


        """
        database.session.query(models.MetroEvent.cardno,
            label('members', func.count(models.MetroEvent.id)),
            label('total_balance', func.sum(models.MetroEvent.amount))).group_by(User.group).all()
        """

        result = models.MetroEvent.query.\
            filter(and_(models.MetroEvent.datetime >= self.start_date.data,
                 models.MetroEvent.datetime <= self.end_date.data,
                 models.MetroEvent.eventcode == 231)).\
            group_by(models.MetroEvent.cardno).all()
        flash('Found %s records' % len(result))

        for item in result:
            item.amount *= -0.01

        amount = map(lambda item: item.amount, result)
        return result, sum(amount)




