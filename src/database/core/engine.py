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

from sqlalchemy import create_engine
from src.loader.logins import GetLogin


class SQLEngine:
    host, user, password, database = GetLogin().get_mariadb()
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
