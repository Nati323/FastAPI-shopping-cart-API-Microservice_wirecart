from contextlib import contextmanager

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

class Database:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(self.db_url, connect_args={
            "check_same_thread": False})
        self.session_factory = orm.scoped_session(
            orm.sessionmaker(autocommit=False,
                             autoflush=False, bind=self.engine))

    @contextmanager
    def session(self):
        session: Session = self.session_factory()
        global err
        err = None
        try:
            yield session
        except Exception as e:
            # Init exception variable so it can be raised later
            # And be handled by the service layer
            err = e

            print('Session rollback because of exception: %s', e)
            session.rollback()
        finally:
            session.close()

            if err:
                raise Exception(err)
