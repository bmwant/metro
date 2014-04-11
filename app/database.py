# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*- #
"""
Configuring ORM
"""

import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.query import Query
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy import event
from app import app

"""
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    print 'connection listener'
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""



def create_session(engine):
    return scoped_session(sessionmaker(bind=engine))


def extend_engine(engine, sql_file):
    with file(sql_file) as f:
        sql = f.readlines()

    for statement in sql:
        engine.execute(statement)


def bind_models_to_database():
    engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'],
                                      convert_unicode=True)
    extend_engine(engine, app.config['SQLALCHEMY_META'])
    session = sessionmaker(bind=engine)
    db_session = create_session(engine)
    Base = declarative_base()
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return Base, session


Base, session = bind_models_to_database()
