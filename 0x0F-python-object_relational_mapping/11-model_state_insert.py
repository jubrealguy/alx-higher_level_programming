#!/usr/bin/python3
"""
A script that add a new state Louisiana to the
State objects from the database hbtn_0e_6_usa
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

    # Adding new state to the table and commit
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print("{:d}".format(new_state.id))

    session.close()
