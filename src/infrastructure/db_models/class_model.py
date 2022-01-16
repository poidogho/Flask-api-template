from dataclasses import dataclass
from sqlalchemy import Column, String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from ...application import db

Base = declarative_base()

registration = Table('registration',
                     Base.metadata,
                     Column('userId', String, ForeignKey('User.id')),
                     Column('classId', String, ForeignKey('Class.id')))


@dataclass
class ClassDataModel(db.Model):
    __tablename__ = 'Class'
    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    users = relationship('User', secondary=registration, backref=backref(
        'User', lazy='dynamic'), lazy='dynamic')
