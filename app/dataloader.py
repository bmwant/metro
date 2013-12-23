# -*- coding: utf-8 -*-
__author__ = 'viach_os'

SERVER = 'avms.dit.in.ua'
USERNAME = 'student'
PASSWORD = 'student'
DB_ALIAS = 'db'
DB_EXT = 'db3'

DATAPATH = 'data'

import ftplib
import os
import StringIO


class DataLoader(object):
    """
    Load data from FTP
    """
    def __init__(self, server, username, password):
        self.connection = ftplib.FTP(server)
        self.connection.login(username, password)

        if not os.path.exists(DATAPATH):
            os.makedirs(DATAPATH)

    def get_file_content(self, filename):
        """
        Return list of string
        """
        file = StringIO.StringIO()
        self.connection.retrbinary("RETR %s" % filename, file.write)
        file.seek(0)
        return file.readlines()

    def download_file(self, filename, local_name=None, lazy=True):
        """
        Return full file name
        """
        local_name = local_name or filename

        #TODO: move /data to upper level
        filepath = os.path.join(DATAPATH, local_name)
        abspath = os.path.abspath(filepath)

        #:TODO: rewrite lazy loading with local index
        try:
            if lazy and self.connection.size(filename) == os.path.getsize(filepath):
                return False
        except OSError:
            pass

        with open(filepath, 'wb') as file:
            self.connection.retrbinary("RETR %s" % filename, file.write)

        return abspath

def get_available_halls():
    """
    nodes.name + list of ADBK_dump20130225/*
    """
    pass


def get_card_by_hall(hall, card_number):
    pass


def connect_to_sqlite():
    pass

def unrar(rar_path, extension):
    import rarfile

    with rarfile.RarFile(rar_path) as rf:
        for file in rf.infolist():
            if file.filename.split('.')[-1] == extension:
                rf.extract(file)
                return file.filename


def move_db(filename):
    import shutil
    db_file = '.'.join([DB_ALIAS, DB_EXT])
    if '\\' in filename:
        filename = filename.replace('\\', '/')

    shutil.move(filename, os.path.join(DATAPATH, db_file))
    shutil.rmtree(filename.split(os.path.sep)[0])

if __name__ == '__main__':
    loader = DataLoader(SERVER, USERNAME, PASSWORD)
    nodes = loader.get_file_content('nodes.name')
    workers = loader.download_file('Basa 2013.xls')
    db_path = loader.download_file('ADBK_dump20130225/adbk.n0261.11.rar',
                                   ''.join([DB_ALIAS, '.rar']))
    if db_path:
        unrar_path = unrar(db_path, DB_EXT)
        move_db(unrar_path)



