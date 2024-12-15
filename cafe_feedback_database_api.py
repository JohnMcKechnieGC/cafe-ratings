class CafeFeedbackDatabaseAPI:
    def __init__(self, database):
        self.database = database

    def add_new_feedback(self, customer_name, date_of_visit, rating):
        self.database.add_feedback(customer_name, date_of_visit, rating)

    def retrieve_all_feedback(self):
        return self.database.get_all_feedback()

    def sum_ratings(self):
        return self.database.sum_ratings()

    def count_ratings(self):
        return self.database.count_ratings()
