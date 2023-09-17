#!/usr/bin/python3
"""Script that retrieves the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)

    with Session() as session:
        first_state = session.query(State).first()

        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")
