# -*- coding: utf-8 -*-
# A simple Python script to convert csv files to sqlite (with type guessing)
#
# @author: Rufus Pollock
# Placed in the Public Domain
import csv
import sqlite3

def convert(filepath_or_fileobj, dbpath, table='data'):
    if isinstance(filepath_or_fileobj, basestring):
        fo = open(filepath_or_fileobj)
    else:
        fo = filepath_or_fileobj
    reader = csv.reader(fo)

    types = _guess_types(fo)
    fo.seek(0)
    headers = reader.next()

    _columns = ','.join(
        ['"%s" %s' % (header, _type) for (header,_type) in zip(headers, types)]
    )

    conn = sqlite3.connect(dbpath)
    conn.text_factory = str
    c = conn.cursor()
    #: c.execute('CREATE table %s (%s)' % (table, _columns))

    _insert_tmpl = 'insert into %s values (%s)' % (table,
                                                   ','.join(['?']*len(headers)))
    for row in reader:
        # we need to take out commas from int and floats for sqlite to
        # recognize them properly ...
        row = [ x.replace(',', '') if y in ['real', 'integer'] else x
                for (x,y) in zip(row, types) ]
        print row
        c.execute(_insert_tmpl, row)

    conn.commit()
    c.close()

def _guess_types(fileobj, max_sample_size=100):
    '''Guess column types (as for SQLite) of CSV.

    :param fileobj: read-only file object for a CSV file.
    '''
    reader = csv.reader(fileobj)
    # skip header
    _headers = reader.next()
    # we default to text for each field
    types = ['text'] * len(_headers)
    # order matters
    # (order in form of type you want used in case of tie to be last)
    options = [
        ('text', unicode),
        ('real', float),
        ('integer', int)
        # 'date',
    ]
    # for each column a set of bins for each type counting successful casts
    perresult = {
        'integer': 0,
        'real': 0,
        'text': 0
    }
    results = [ dict(perresult) for x in range(len(_headers)) ]
    for count,row in enumerate(reader):
        for idx,cell in enumerate(row):
            cell = cell.strip()
            # replace ',' with '' to improve cast accuracy for ints and floats
            cell = cell.replace(',', '')
            for key,cast in options:
                try:
                    # for null cells we can assume success
                    if cell:
                        cast(cell)
                    results[idx][key] = (results[idx][key]*count + 1) / float(count+1)
                except (ValueError), inst:
                    pass
        if count >= max_sample_size:
            break
    for idx,colresult in enumerate(results):
        for _type, dontcare in options:
            if colresult[_type] == 1.0:
                types[idx] = _type
    return types


if __name__ == '__main__':
    import os
    basedir = os.path.abspath(os.path.dirname(__file__))
    csv_path = r'/home/natalia/viach/py_workspace/aggr/metadata/Basa 2013.csv'
    db_path = r'/home/natalia/viach/py_workspace/aggr/metadata/meta.db3'
    convert(csv_path, db_path, 'cashiers')