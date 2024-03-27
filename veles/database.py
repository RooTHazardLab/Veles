import sqlalchemy
import sqlalchemy.orm as orm

class Base(orm.DeclarativeBase):
    pass


DBSession = None


def connect():
    global DBSession

    engine = sqlalchemy.create_engine('sqlite:///veles.sqlite')

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBSession = orm.sessionmaker(bind=engine)


def get_session():
    if DBSession is None:
        connect()

    db = DBSession()

    try:
        yield db
    finally:
        db.close()
