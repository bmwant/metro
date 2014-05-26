__author__ = 'Most Wanted'

import tables
import numpy
import datetime
import time

from app import app, server, database
from app.models import MetroEvent
import dataloader
import forms
import pprint

class HallDate(tables.IsDescription):
    hall = tables.StringCol(100, pos=1)
    time = tables.Time64Col(pos=2)
    cashier = tables.StringCol(100, pos=3)


def log(string):
    return app.logger.debug(string)

def grab_all_adbk_for_hall(hall):
    filename = '%s.h5' % hall
    hall_tables = tables.open_file(filename, 'w')
    adbks = forms.get_adbk_for_hall(hall)
    pprint.pprint(adbks)
    for index, adbk in enumerate(adbks):
        server_filename = '%s/%s' % (app.config['DUMP_DIR'], adbk)
        print server_filename
        db_path = server.download_file(server_filename, adbk, lazy=False)
        unrar_path = dataloader.unrar(db_path, dataloader.DB_EXT)
        dataloader.move_db(unrar_path, 'data/%s.%s.db3' % (hall, index))
        database.only_bind_database()
        result = MetroEvent.query.all()
        for res in result:
            print res.datetime
            print res.cardno

    tbl = hall_tables.create_table('/', 'hall_data', HallDate)
    tbl.row['hall'] = '23asdf'
    tbl.row['time'] = time.time()
    tbl.row['cashier'] = 'Tasdf DSA SADf'
    tbl.row.append()


    tbl.flush()
    table = hall_tables.root.hall_data
    for row in table.iterrows():
        print row['hall']
    hall_tables.close()
    #forms.get_adbk_for_hall(hall)

def grab_all_adbk():
    halls = forms.get_unique_halls()
    grab_all_adbk_for_hall(next(halls.iterkeys()))


grab_all_adbk()