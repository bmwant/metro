# -*- coding: utf-8 -*-

from datetime import datetime

from flask.ext.wtf import Form
from wtforms.fields import TextField, SelectField, SubmitField
from wtforms.validators import Required
from wtforms_html5 import DateField

#: TODO: move logic from this
from sqlalchemy import and_
from sqlalchemy.sql import func


from app import app, server, dataloader, flash, models, database
import pprint
from collections import OrderedDict

#: TODO: set lazy
def get_halls():
    """
    Ger list of tuples with hall code and name

    Look at dumps and nodes file structure, and you will understand this code :)
    """
    dumps = server.get_list_of_dir(app.config['DUMP_DIR'])
    #pprint.pprint(dumps)
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


def get_cashiers_for_hall(hall):
    result = models.MetroEvent.query.\
            filter(and_(models.MetroEvent.datetime >= self.start_date.data,
                 models.MetroEvent.datetime <= self.end_date.data,
                 models.MetroEvent.eventcode == 231))


def get_unique_halls():
    """
    Returns dictionary of unique halls
    {
        'hall_code1': 'hall_name1',
        ...
        'hall_codeN': 'hall_nameN'
    }
    """
    nodes = iter(server.get_file_content('nodes.name'))
    #halls = []
    #node = nodes.next().split(';')
    halls = {}
    for item in nodes:
        node = item.split(';')
        halls[node[0]] = node[1].decode("utf-8")
    return halls


def get_adbk_for_hall(hall):
    dumps = server.get_list_of_dir(app.config['DUMP_DIR'])
    result = []
    for item in dumps:
        raw_item = item.split('.')
        code = raw_item[1]
        if code == hall:
            result.append(item)
    return result


def get_cashiers_statistic():
    halls = get_unique_halls()
    for code, name in halls.iteritems():
        pass


def get_halls_statistic():
    """
    The most awful code I have ever written
    """
    print get_adbk_for_hall('n0261')
    halls = get_unique_halls()
    stat = OrderedDict()
    for code, name in halls.iteritems():
        adbks = get_adbk_for_hall(code)
        adbk_info = {}
        for adbk in adbks:
            filename = '%s/%s' % (app.config['DUMP_DIR'], adbk)
            adbk_date = server.get_file_modtime(filename)
            adbk_num = adbk.split('.')[2][-1]
            adbk_info[adbk_num] = adbk_date
        sorted_adbk_info = []
        for i in range(1, 5):
            index = str(i)
            if index in adbk_info.keys():
                adbk_date = datetime.strptime(adbk_info[index], '%d %B %Y %H:%M:%S')
                actual_date = datetime(2012, 6, 1)  # June 1st, 2012
                if adbk_date > actual_date:
                    status = 'Updated'
                else:
                    status = 'Outdated'
                sorted_adbk_info.append({index: adbk_info[index],
                                         'status': status})
            else:
                sorted_adbk_info.append(({index: None,
                                          'status': 'Absent'}))
        stat[code] = {
            'name': name,
            'adbk': sorted_adbk_info
        }
    sorted_stat = sorted(stat.items(), key=lambda k: k[0])
    return OrderedDict(sorted_stat)


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
        app.logger.debug('Downloading file: %s' % filename)
        db_path = server.download_file(filename,
                                   ''.join([dataloader.DB_ALIAS, '.rar']))
        #: TODO: except broken pip - create new server
        mdtime = server.get_file_modtime(filename)
        if db_path:
            unrar_path = dataloader.unrar(db_path, dataloader.DB_EXT)
            dataloader.move_db(unrar_path)
            database.bind_models_to_database()
            # import database #: rebind model
            # database.bind_models_to_database()
            flash('%s loaded into %s' % (filename, db_path))
            flash('%s last modified %s' % (filename, mdtime))
        else:
            flash('Database file exists')

        result = models.MetroEvent.query.filter_by(cardno=self.card_number.data).all()
        flash('Found %s records' % len(result))

        return result


class HallForm(Form):
    hall = SelectField('Hall', validators=[Required()],
                       choices=get_halls())
    start_date = DateField('Start', validators=[Required()])
    end_date = DateField('End', validators=[Required()])

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
            database.bind_models_to_database()
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




