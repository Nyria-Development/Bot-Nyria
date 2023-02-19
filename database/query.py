import mysql.connector
from database.pool import Pool


class Query:
    def __init__(self, pool_name: str, pool_size: int):
        self.pool_name = pool_name
        self.pool_size = pool_size

        self.connection_pool = Pool(
            pool_name=self.pool_name,
            pool_size=self.pool_size
        ).create()

    def execute(self, query: str, data: list):
        connection: mysql.connector.MySQLConnection = self.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

        cursor.execute(query, data)
        if query.startswith("SELECT"):
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result

        connection.commit()
        cursor.close()
        connection.close()
