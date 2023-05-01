from src.database.core.engine import SQLEngine
from sqlalchemy.orm import sessionmaker, Session


class SQLSession:

    @staticmethod
    def create_session() -> Session:
        session = sessionmaker(bind=SQLEngine.engine)
        return session()
