from sqlalchemy import create_engine
from src.loader.logins import GetLogin


class SQLEngine:
    host, user, password, database = GetLogin().get_mariadb()
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
