#!/usr/bin/python3
"""
a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    new_name = 'New Mexico'
    session = Session()
    
    state_to_update = session.query(State).filter(State.id == 2).first()
    state_to_update = new_name
    session.commit()
    session.close()