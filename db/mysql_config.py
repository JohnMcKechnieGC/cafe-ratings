"""
Specify the host and database. Read the user and password from environment variables.
"""

import os

config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PW'),
    'host': 'localhost',
    'database': 'cafe_ratings'
}
