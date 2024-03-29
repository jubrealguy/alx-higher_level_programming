#!/usr/bin/python3
"""
A script that deletes State objects with letter a
from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    # Engine for Database
    engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost/{}"
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
                )
    Session = sessionmaker(bind=engine)  # Creating a session
    session = Session()  # Instatiate our Session

    # deleting states with a in their names
    for inst in session.query(State).filter(State.name.like('%a%')).all():
        if 'a' in inst.name:
            session.delete(inst)

    session.commit()
    session.close()
