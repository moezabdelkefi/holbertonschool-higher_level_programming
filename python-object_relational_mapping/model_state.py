#!/usr/bin/python3
"""
 Write a script that deletes all State objects with a
 name containing the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create the SQLAlchemy engine to connect to the MySQL server
engine = create_engine('mysql://localhost:3306')

# create the declarative base instance
Base = declarative_base()

# define the State class, inheriting from Base
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# create the table in the MySQL database
Base.metadata.create_all(engine)
