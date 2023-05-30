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

from src.database.core.engine import SQLEngine
from src.database.tables import bugs, setup
from src.logger.logger import Logging


class Register:

    @staticmethod
    def register():
        bugs.bugs_base.metadata.create_all(bind=SQLEngine.engine)
        setup.base_setup.metadata.create_all(bind=SQLEngine.engine)
        Logging().info("Database ready")
