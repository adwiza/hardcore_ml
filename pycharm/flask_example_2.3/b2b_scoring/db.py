from string import Template
import sqlalchemy
from sqlalchemy import Integer, Column, create_engine, ForeignKey, String
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    val1 = Column(String)
    val2 = Column(String)
    val3 = Column(String)


class Features(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True)
    feat1 = Column(Integer)
    feat2 = Column(String)
    feat3 = Column(String)


SQL_GET_DATA_FOR_OUTLIER = Template("SELECT * FROM scores.outliers WHERE id $id")
