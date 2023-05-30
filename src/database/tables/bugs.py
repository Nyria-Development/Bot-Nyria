# All Rights Reserved
# Copyright (c) 2023 Nyria
#
# This code, including all accompanying software, documentation, and related materials, is the exclusive property
# of Nyria. All rights are reserved.
#
# Any use, reproduction, distribution, or modification of the code without the express written
# permission of Nyria is strictly prohibited.
#
# No warranty is provided for the code, and Nyria shall not be liable for any claims, damages,
# or other liability arising from the use or inability to use the code.

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
