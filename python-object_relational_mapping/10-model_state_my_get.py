#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument from
the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    if len(sys.argv) == 5:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        state_name = sys.argv[4]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(user, passwd, db), pool_pre_ping=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.name == state_name).first()

        if state:
            print(state.id)
        else:
            print('Not found')
    else:
        print('Usage: {} <username> <password> <database> <state>'.
              format(sys.argv[0]))
        sys.exit(1)
