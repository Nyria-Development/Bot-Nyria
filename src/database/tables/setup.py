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
    on_message = Column("on_message", VARCHAR(3), nullable=False)
    on_message_edit = Column("on_message_edit", VARCHAR(3), nullable=False)
    on_message_delete = Column("on_message_delete", VARCHAR(3), nullable=False)
    on_reaction_add = Column("on_reaction_add", VARCHAR(3), nullable=False)
    on_member_ban = Column("on_member_ban", VARCHAR(3), nullable=False)
    on_member_unban = Column("on_member_unban", VARCHAR(3), nullable=False)

    def __init__(
            self,
            server_id: int,
            log_channel_id: int,
            on_message: str,
            on_message_edit: str,
            on_message_delete: str,
            on_reaction_add: str,
            on_member_ban: str,
            on_member_unban: str
    ):
        self.server_id = server_id
        self.log_channel_id = log_channel_id
        self.on_message = on_message
        self.on_message_edit = on_message_edit
        self.on_message_delete = on_message_delete
        self.on_reaction_add = on_reaction_add
        self.on_member_ban = on_member_ban
        self.on_member_unban = on_member_unban

    def __repr__(self):
        return f"{self.server_id}, {self.log_channel_id}, {self.on_message}, {self.on_message_edit}, " \
               f"{self.on_message_delete}, {self.on_reaction_add}, {self.on_member_ban}, {self.on_member_unban}"


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
