#!/usr/bin/python3
"""
Write a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    db = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                       format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)

    Session = sessionmaker(bind=db)
    session = Session()

    result = session.query(State).filter(State.name.like
                                         ('%a%')).order_by(State.id)

    if result.count() > 0:
        for state in result:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
