from src.database.core.engine import SQLEngine
from src.database.tables import bugs, setup, level
from src.logger.logger import Logging


class Register:

    @staticmethod
    def register():
        bugs.bugs_base.metadata.create_all(bind=SQLEngine.engine)
        setup.base_setup.metadata.create_all(bind=SQLEngine.engine)
        #level.base_level.metadata.create_all(bind=SQLEngine.engine)
        Logging().info("Database ready")
