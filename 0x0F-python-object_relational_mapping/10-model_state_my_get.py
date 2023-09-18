#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine, select
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True,
        )
    state_name = sys.argv[4]
    with engine.connect() as connection:
        result = select(State) \
            .where(State.name == state_name)
        states = connection.execute(result).first()
        if states:
            print(states.id)
        else:
            print("Not found")
    engine.dispose()
