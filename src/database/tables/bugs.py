from sqlalchemy import BIGINT, Column, INTEGER
from sqlalchemy.orm import declarative_base, DeclarativeBase

bugs_base: DeclarativeBase = declarative_base()


class TableBugs(bugs_base):
    __tablename__ = "bugs"

    id = Column("id", BIGINT, autoincrement=True, primary_key=True)
    user_id = Column("user_id", BIGINT, nullable=False)
    reports = Column("reports", INTEGER, nullable=False)

    def __init__(self, user_id: int, reports: int):
        self.user_id = user_id
        self.reports = reports

    def __repr__(self) -> str:
        return f"{self.id}, {self.user_id}, {self.reports}"
