#!/usr/bin/python3
"""
 Write a script that deletes all State objects with a
 name containing the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://localhost:3306')

Base = declarative_base()

class State(Base):
    """
    Write a script that deletes all State objects with a
    name containing the letter a from the database hbtn_0e_6_usa
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

Base.metadata.create_all(engine)
