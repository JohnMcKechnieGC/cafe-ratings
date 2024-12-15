"""
Define an abstract base class to define the interface that all DB classes will implement.
"""

from abc import ABC, abstractmethod


class DbInterface(ABC):
    """
    Abstract base class to define the interface that all DB classes will implement.
    """
    @abstractmethod
    def add_feedback(self, customer_name, date_of_visit, rating):
        """
        Adds a feedback to the the database.
        :param customer_name: String
        :param date_of_visit: String formatted as YYYY-MM-MM
        :param rating: Number between 1 and 5
        """

    @abstractmethod
    def get_all_feedback(self):
        """
        Returns all the user ratings from the database.
        :return: A list of user rating records.
        """

    @abstractmethod
    def sum_ratings(self):
        """
        Returns the sum of all ratings.
        :return: Sum of all ratings.
        """

    @abstractmethod
    def count_ratings(self):
        """
        Returns the count of user ratings.
        :return: The number of user rating records.
        """
