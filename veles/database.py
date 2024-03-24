import sqlalchemy
import sqlalchemy.orm as orm

import funds.models

BASES = [
    funds.models.Base.metadata
]

DBSession = None

def connect():
    global DBSession

    engine = sqlalchemy.create_engine('sqlite:///veles.sqlite')

    for base_meta in BASES:
        base_meta.drop_all(engine)
        base_meta.create_all(engine)
        base_meta.bind = engine

    DBSession = orm.sessionmaker(bind=engine)


def get_session():
    if DBSession is None:
        connect()

    db = DBSession()

    try:
        yield db
    finally:
        db.close()
