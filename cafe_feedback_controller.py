from datetime import datetime
import logging


class CafeFeedbackController:
    def __init__(self, database_api):
        self.database_api = database_api

    def add_feedback(self, customer_name, rating):
        try:
            date_of_visit = datetime.today().strftime('%Y-%m-%d')
            self.database_api.add_new_feedback(customer_name, date_of_visit, rating)
            return 'Success', 'Feedback added successfully.'
        except Exception as error:
            logging.exception(error)
            return 'Error', 'Sorry, could not add feedback. Please contact your administrator for support.'

    def view_all_feedback(self):
        try:
            records = self.database_api.retrieve_all_feedback()
            if len(records) == 0:
                result = 'No feedback records in database.'
            else:
                result = '\n'.join([str(record) for record in records])
            return result
        except Exception as error:
            logging.exception(error)
            return 'Sorry, could not retrieve feedback. Please contact your administrator for support.'

    def view_average_rating(self):
        try:
            count_of_ratings = self.database_api.count_ratings()

            if count_of_ratings == 0:
                result = 'There are no ratings in the database.'
            else:
                sum_of_ratings = self.database_api.sum_ratings()
                avg_rating = sum_of_ratings / count_of_ratings
                result = f'The average rating is: {avg_rating:.1f}'

            return result

        except Exception as error:
            logging.exception(error)
            return 'Sorry, could not retrieve ratings. Please contact your administrator for support.'
