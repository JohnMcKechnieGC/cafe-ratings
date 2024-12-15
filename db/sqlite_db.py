"""
Implement a database interface using SQLite.
"""

import atexit
import sqlite3
from db.db_interface import DbInterface
from db.exceptions.database_connection_error import DatabaseConnectionError


class SQLiteDB(DbInterface):
    """
    SQLite implementation of the database interface.
    """
    def __init__(self, db_file='./db/data/ratings.db'):
        self.db_file = db_file
        self.conn = None
        self.connect()

        atexit.register(self.cleanup)

    def connect(self):
        """
        Try to connect to the specified SQLite file.
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
        except sqlite3.Error as error:
            raise DatabaseConnectionError(f'SQLite error: {error}') from error

        sql = ('CREATE TABLE IF NOT EXISTS '
               'ratings (rating_id INTEGER PRIMARY KEY AUTOINCREMENT, '
               'name TEXT, date TEXT, rating INTEGER)')
        self.conn.execute(sql)

    def cleanup(self):
        """
        Explicitly clean up the database connection when the program exits. 
        """
        if self.conn:
            self.conn.close()

    def add_feedback(self, customer_name, date_of_visit, rating):
        sql = 'INSERT INTO ratings (name, date, rating) VALUES (?, ?, ?);'
        values = (customer_name, date_of_visit, rating)
        cursor = self.conn.cursor()
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()

    def get_all_feedback(self):
        sql = 'SELECT rating_id, name, date, rating FROM ratings;'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return [(rating_id, name, date, rating) for rating_id, name, date, rating in data]

    def sum_ratings(self):
        sql = 'SELECT SUM(rating) FROM ratings;'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        sum_of_ratings, = cursor.fetchone()
        cursor.close()
        return 0 if sum_of_ratings is None else sum_of_ratings

    def count_ratings(self):
        sql = 'SELECT COUNT(rating) FROM ratings;'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        count_of_ratings, = cursor.fetchone()
        cursor.close()
        return int(count_of_ratings)
