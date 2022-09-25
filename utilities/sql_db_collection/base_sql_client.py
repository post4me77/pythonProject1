import mysql.connector
from mysql.connector import Error
from utilities.project_logger import logger, set_logger


class BaseSqlConnection:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database = db_name
        set_logger()

    def _create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.database
            )
        except Error as e:
            logger.error(f"The error '{e}' occurred")
        return connection

    def _create_cursor(self, connection):
        return connection.cursor()

    def execute_query(self, query):
        connection = self._create_connection()
        cursor = self._create_cursor(connection)
        try:
            cursor.execute(query)
            connection.commit()
            logger.info(f'QUERY : {query} executed')
        except Error as e:
            logger.error(f"The error '{e}' occurred")
