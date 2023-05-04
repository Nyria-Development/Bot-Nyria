from sqlalchemy import VARCHAR, Column, BIGINT, INTEGER
from sqlalchemy.orm import declarative_base, DeclarativeBase

base_setup: DeclarativeBase = declarative_base()


class VoiceTable(base_setup):
    __tablename__ = "voice_setup"

    id = Column("id", BIGINT, autoincrement=True, primary_key=True)
    server_id = Column("server_id", BIGINT, nullable=False)
    category_name = Column("category_name", VARCHAR(30), nullable=False)

    def __init__(self, server_id: int, category_name: str):
        self.server_id = server_id
        self.category_name = category_name

    def __repr__(self) -> str:
        return f"{self.server_id}, {self.category_name}"


class LogsTable(base_setup):
    __tablename__ = "logs_setup"

    id = Column("id", BIGINT, autoincrement=True, primary_key=True)
    server_id = Column("server_id", BIGINT, nullable=False)
    log_channel_id = Column("log_channel_id", BIGINT, nullable=False)
    log_config_int = Column("log_config_int", BIGINT, nullable=False)

    def __init__(
            self,
            server_id: int,
            log_channel_id: int,
            log_config_int: int
    ):
        self.server_id = server_id
        self.log_channel_id = log_channel_id
        self.log_config_int = log_config_int

    def __repr__(self):
        return f"{self.server_id}, {self.log_channel_id}, {self.log_config_int}"


class LevelTable(base_setup):
    __tablename__ = "level_setup"

    id = Column("id", BIGINT, autoincrement=True, primary_key=True)
    server_id = Column("server_id", BIGINT, nullable=False)
    level_speed = Column("level_speed", INTEGER, nullable=False)

    def __init__(self, server_id: int, level_speed: int):
        self.server_id = server_id
        self.level_speed = level_speed

    def __repr__(self) -> str:
        return f"{self.server_id}, {self.level_speed}"
