import logging
import mysql.connector
from mysql.connector import Error as MySQLError
from db.exceptions.database_connection_error import DatabaseConnectionError
from db.db_interface import DbInterface


class InvalidMySQLDB(DbInterface):
    def __init__(self):
        logging.info('Attempting to open a MySQL database without providing necessary info.')
        try:
            self.conn = mysql.connector.connect(user='', password='', host='', database='')
        except MySQLError as error:
            raise DatabaseConnectionError(f'MySQL error: {error}') from error

    def add_feedback(self, customer_name, date_of_visit, rating):
        pass

    def get_all_feedback(self):
        pass

    def sum_ratings(self):
        pass

    def count_ratings(self):
        pass
