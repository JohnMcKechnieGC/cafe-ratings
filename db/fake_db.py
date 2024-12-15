"""
Implement a database interface that does not depend on any database engine.
This may be useful for testing. 
"""

from db.db_interface import DbInterface


class FakeDB(DbInterface):
    """
    Implementation of the database interface that uses a list in memory,
    rather than depending on a database engine.
    """
    def __init__(self, data=None):
        # raise RuntimeError('Testing error handling')
        if data is None:
            self.data = [(0, 'Fred', '2023.12.07', 4), (1, 'Mary', '2023.12.07', 3)]
        else:
            self.data = data

    def add_feedback(self, customer_name, date_of_visit, rating):
        # raise RuntimeError('Testing error handling')
        next_id = max(self.data, key=lambda x: x[0])[0] + 1
        new_record = (next_id, customer_name, date_of_visit, rating)
        self.data.append(new_record)

    def get_all_feedback(self):
        # raise RuntimeError('Testing error handling')
        return self.data.copy()

    def sum_ratings(self):
        # raise RuntimeError('Testing error handling')
        return sum(entry[3] for entry in self.data)

    def count_ratings(self):
        # raise RuntimeError('Testing error handling')
        return len(self.data)
