__author__ = 'Most Wanted'

import tables
import numpy
import datetime
import time


class HallDate(tables.IsDescription):
    hall = tables.StringCol(100, pos=1)
    time = tables.Time64Col(pos=2)
    cashier = tables.StringCol(100, pos=3)


def grab_all_adbk_for_hall(hall):
    filename = '%s.h5' % hall
    hall_tables = tables.open_file(filename, 'w')
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

grab_all_adbk_for_hall('ae43')