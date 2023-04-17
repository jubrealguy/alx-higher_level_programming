#!/usr/bin/python3
"""
A script that creates the State “California” with the
City “San Francisco”from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Engine for Database
    engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost/{}"
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
                )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # Creating a session
    session = Session()  # Instatiate our Session

    # Create new state and new city and commit
    new_state = State(name="California")  # Create a new state
    new_city = City(name="San Francisco")  # Create a new city
    new_state.cities.append(new_city)  # Append the new city to the new city

    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()
