# Cafe-Ratings Demo
This project shows one way to easily swap different database technologies in and out of a project. The purpose of the demo is to encourage software development students to not "bake in" decisions, such as which database technology to use. It should be possible to defer decisions like that until later when we have a better idea of what we want to use, or easily change a database technology that does not support our use case.

In this demo we can choose between SQLite or MySQL (assuming that you have a MySQL database that you can connect to). You choose the db you want to use by modifying main.py to comment/uncomment the choice as you see fit:

# Import the chosen database implementation by uncommenting your preferred option
from db.sqlite_db import SQLiteDB as Db
# from db.mysql_db import MySQLDB as Db  # Requires MySQL with a cafe ratings database
# from db.invalid_mysql_db import InvalidMySQLDB as Db
# from db.fake_db import FakeDB as Db


Similarly, there are three user interfaces that can be used. None are very exciting, but the point is that we can easily swap between them. This is also done using comments in main.py.

# Import the chosen user interface implementation
from ui.console_ui import CafeFeedbackConsoleUI as CafeFeedbackUI
# from ui.tk_graphical_ui import CafeFeedbackTkInterUI as CafeFeedbackUI
# from ui.qt_graphical_ui import CafeFeedbackQtUI as CafeFeedbackUI
