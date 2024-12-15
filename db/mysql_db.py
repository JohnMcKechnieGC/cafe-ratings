"""
Implement a database interface using MySQL.
"""

import atexit
import mysql.connector
from mysql.connector import Error as MySQLError
from db.mysql_config import config
from db.db_interface import DbInterface
from db.exceptions.database_connection_error import DatabaseConnectionError


class MySQLDB(DbInterface):
    """
    MySQL implementation of the database interface.
    """

    def __init__(self):
        atexit.register(self.cleanup)
        try:
            self.conn = mysql.connector.connect(
                user=config['user'],
                password=config['password'],
                host=config['host'],
                database=config['database']
            )
        except MySQLError as error:
            raise DatabaseConnectionError(f'MySQL error: {error}') from error

    def cleanup(self):
        """
        Explicitly clean up the database connection when the program exits. 
        """
        if self.conn is not None:
            self.conn.close()

    def add_feedback(self, customer_name, date_of_visit, rating):
        cursor = self.conn.cursor(prepared=True)
        sql = 'INSERT INTO ratings (name, date, rating) ' \
              'VALUES (?, ?, ?);'
        values = (customer_name, date_of_visit, rating)
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()

    def get_all_feedback(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT rating_id, name, date, rating FROM ratings;')
        data = []
        for (rating_id, name, date, rating) in cursor:
            data.append((rating_id, name, str(date), rating))
        cursor.close()
        return data

    def sum_ratings(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT SUM(rating) FROM ratings;')
        sum_of_ratings, = cursor.fetchone()
        cursor.close()
        return int(sum_of_ratings)

    def count_ratings(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(rating) FROM ratings;')
        count_of_ratings, = cursor.fetchone()
        cursor.close()
        return int(count_of_ratings)
