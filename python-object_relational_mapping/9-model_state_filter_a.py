#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@localhost/'
        f'{DATABASE_NAME}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()
