import mysql.connector
from src.loader.jsonLoader import Tokens
from mysql.connector.errors import Error


class Check:
    def __init__(self):
        self.host, self.user, self.password, self.database = Tokens().maria_db()
        self.state_database: bool = False

    def inspect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
        except Error:
            raise Exception("Can't connect to database. Is your config right?")

        cursor = connection.cursor(prepared=True)
        cursor.execute("Show databases")
        databases = cursor.fetchall()

        for data in databases:
            if str(data[0]).lower() == "nyria":
                self.state_database = True
                print("Database faultless")
                connection.close()

        if not self.state_database:
            self.__create(connection=connection)

    @staticmethod
    def __create(connection: mysql.connector.MySQLConnection):
        cursor = connection.cursor()

        # create database Nyria
        cursor.execute("CREATE DATABASE Nyria")
        cursor.execute("USE Nyria")

        cursor.execute("CREATE TABLE bug_reports (userId BIGINT NOT NULL, reports INT NOT NULL)")
        cursor.execute("CREATE TABLE welcome (serverId BIGINT NOT NULL, channelId BIGINT NOT NULL)")
        cursor.execute("CREATE TABLE music (serverId BIGINT NOT NULL, tracksId INT NOT NULL, trackName TEXT NOT NULL)")

        connection.commit()
        connection.close()
