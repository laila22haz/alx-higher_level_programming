#!/usr/bin/python3
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

    with engine.connect() as connection:
        result = select(State).order_by(State.id.asc())
        states = connection.execute(result)
        for row in states:
            print(f"{row.id}: {row.name}")
    engine.dispose()
