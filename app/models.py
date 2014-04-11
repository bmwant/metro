# -*- coding: utf-8 -*-
"""
Models
SQLAlchemy declarative is used.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class ErrorType(Base):

    __table_args__ = {'extend_existing': True}
    __tablename__ = 'ref_errors'

    errorcode = Column('ErrorCode', Integer, primary_key=True)
    errorname = Column('ErrorName', String)

    def __repr__(self):
        return '%s "%s"' % (self.__tablename__, self.errorcode)


class EventType(Base):

    __table_args__ = {'extend_existing': True}
    __tablename__ = 'ref_events'

    eventcode = Column('EventCode', Integer, primary_key=True)
    eventname = Column('EventName', String)

    def __repr__(self):
        return '%s "%s"' % (self.__tablename__, self.eventcode)


class MetroEvent(Base):
    """
    Event with card
    """
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'events'

    id = Column('ID', Integer, primary_key=True)
    datetime = Column('DateTime', String)
    eventcode = Column('EventCode', Integer)
    event = relationship('EventType', foreign_keys='EventType.eventcode', uselist=False,
                         primaryjoin="MetroEvent.eventcode==EventType.eventcode")

    errorcode = Column(Integer, ForeignKey(ErrorType.errorcode))
    error = relationship('ErrorType', foreign_keys='ErrorType.errorcode', uselist=False,
                         primaryjoin="MetroEvent.errorcode==ErrorType.errorcode")

    usercardsn = Column('UserCardSN', String)
    userasppsn = Column('UserASPPSN', String)
    cashcardsn = Column('CashCardSN', String)
    cashasppsn = Column('CashASPPSN', String)

    contractid = Column('ContractID', Integer)
    contractcopyid = Column('ContractCopyID', Integer)
    contractvalue = Column('ContractValue', Integer)

    transactionvalue = Column('TransactionValue', Integer)

    amount = Column('Amount', Integer)  # $ value in cents

    cardno = Column('CardNo', String)  # card number
    cashier = relationship('Cashier', foreign_keys='Cashier.cardno', uselist=False,
                         primaryjoin="MetroEvent.cardno==Cashier.cardno")

    pursevalue = Column('PurseValue', Integer)
    bunkeramount = Column('BunkerAmount', Integer)

    def __repr__(self):
        return '%s "%s"' % (self.__tablename__, self.id)

    def to_cells(self):
        suffix = {'old': 'code', 'new': 'name'}
        cells = []
        for key in self.__table__.columns.keys():
            field_name = key.lower()
            if suffix['old'] in field_name:
                base = field_name.split(suffix['old'])[0]
                try:
                    reference = getattr(self, base)
                    value = getattr(reference, base + suffix['new'])
                except AttributeError:
                    value = 'None'
            else:
                value = getattr(self, field_name)
            cells.append(value)
        return cells


class Cashier(Base):
    __tablename__ = 'cashiers'
    id = Column('ID', Integer, primary_key=True)

    surname = Column('Surname', String)
    name = Column('Name', String)
    fathername = Column('Fathername', String)
    position = Column('Position', String)
    cardno = Column('CardNo', String)  # card number

    @property
    def fullname(self):
        return ' '.join([self.surname, self.name, self.fathername])


    def __repr__(self):
        return '%s "%s"' % (self.__tablename__, self.id)

