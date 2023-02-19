from mysql.connector import pooling
from src.loader.jsonLoader import JsonLoader


class Pool:
    def __init__(self, pool_name: str, pool_size: int):
        self.pool_name = pool_name
        self.pool_size = pool_size

        self.host, self.user, self.password, self.database = JsonLoader().maria_db()

    def create(self):
        connection_pool = pooling.MySQLConnectionPool(
            pool_size=self.pool_size,
            pool_name=self.pool_name,
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return connection_pool
