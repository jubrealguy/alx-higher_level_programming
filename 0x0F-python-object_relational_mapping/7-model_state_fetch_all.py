#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    
    # Engine for Database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost/{}".
                format(user, passwd, db), pool_pre_ping=True
                )
    Session = sessionmaker(bind=engine)  # Creating a session
    session = Session()  # Instatiate our Session

    # Database querying using python instances
    for inst in session.query(State).order_by(State.id):
        print("{:d}:{:s}".format(inst.id, inst.name))

    session.close()
