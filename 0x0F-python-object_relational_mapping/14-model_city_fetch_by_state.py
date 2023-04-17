#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State

if __name__ == "__main__":
    # Engine for Database
    engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost/{}"
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
                )
    Session = sessionmaker(bind=engine)  # Creating a session
    session = Session()  # Instatiate our Session

    # Database querying using python instances
    for inst in session.query(State.name, City.id, City.name)\
            .filter(State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(inst[0], inst[1], inst[2]))

    session.close()
