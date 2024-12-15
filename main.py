"""
This file demonstrates how to easily switch between different database technologies such
as SQLite and MySQL.
"""

import sys
import logging
from cafe_feedback_database_api import CafeFeedbackDatabaseAPI
from cafe_feedback_controller import CafeFeedbackController

# Import the chosen database implementation by uncommenting your preferred option
# from db.sqlite_db import SQLiteDB as Db
# from db.mysql_db import MySQLDB as Db  # Requires MySQL with a cafe ratings database
from db.invalid_mysql_db import InvalidMySQLDB as Db
# from db.fake_db import FakeDB as Db

from db.exceptions.database_connection_error import DatabaseConnectionError

# Import the chosen user interface implementation
from ui.console_ui import CafeFeedbackConsoleUI as CafeFeedbackUI
# from ui.tk_graphical_ui import CafeFeedbackTkInterUI as CafeFeedbackUI
# from ui.qt_graphical_ui import CafeFeedbackQtUI as CafeFeedbackUI


def main():
    """
    Run the demo using the imported Db and UI.
    """
    logging.basicConfig(filename='cafe_ratings.log', level=logging.INFO)

    try:
        database = Db()
    except DatabaseConnectionError as error:
        logging.info('Ending the program because of no valid database.')
        logging.exception(error)
        sys.exit('Could not open the database. Please contact your administrator for support.')

    database_api = CafeFeedbackDatabaseAPI(database)
    controller = CafeFeedbackController(database_api)
    user_interface = CafeFeedbackUI(controller)
    user_interface.run()


if __name__ == '__main__':
    main()
