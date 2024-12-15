from ui.user_interface_abc import UserInterfaceABC
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QGridLayout


class QtUI(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Create input fields
        self.name_input = QLineEdit()
        self.rating_input = QLineEdit()

        self.arrange_ui()

    # noinspection PyUnresolvedReferences
    def arrange_ui(self):
        self.setWindowTitle('Cafe Feedback System')
        self.setGeometry(300, 300, 730, 300)  # x, y, width, height

        # Create widgets
        name_label = QLabel("Customer Name:")
        rating_label = QLabel("Rating (1-5):")
        add_button = QPushButton("Add Feedback")
        add_button.clicked.connect(self.add_feedback)
        view_all_button = QPushButton("View All Feedback")
        view_all_button.clicked.connect(self.view_all_feedback)
        view_average_button = QPushButton("View Average Rating")
        view_average_button.clicked.connect(self.view_average_rating)
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)

        # Create layout and add widgets
        layout = QGridLayout()
        layout.addWidget(name_label, 0, 0)
        layout.addWidget(rating_label, 1, 0)
        layout.addWidget(self.name_input, 0, 1)
        layout.addWidget(self.rating_input, 1, 1)
        layout.addWidget(add_button, 2, 0, 1, 2)
        layout.addWidget(view_all_button, 3, 0, 1, 2)
        layout.addWidget(view_average_button, 4, 0, 1, 2)
        layout.addWidget(exit_button, 5, 0, 1, 2)

        self.setLayout(layout)

    def add_feedback(self):
        customer_name = self.name_input.text()
        rating = self.rating_input.text()
        status, message = self.controller.add_feedback(customer_name, rating)
        QMessageBox.information(self, status, message)

    def view_all_feedback(self):
        feedback = self.controller.view_all_feedback()
        QMessageBox.information(self, 'All Feedback', feedback)

    def view_average_rating(self):
        message = self.controller.view_average_rating()
        QMessageBox.information(self, "Average Rating", message)


class CafeFeedbackQtUI(UserInterfaceABC):
    def run(self):
        app = QApplication(sys.argv)
        ui = QtUI(self.controller)
        ui.show()
        sys.exit(app.exec_())
