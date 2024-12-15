from ui.user_interface_abc import UserInterfaceABC


class CafeFeedbackConsoleUI(UserInterfaceABC):
    def run(self):
        while True:
            print('\n1. Add Feedback\n2. View All Feedback\n3. View Average Rating\n4. Exit')
            choice = input('Enter your choice: ')

            if choice == '1':
                self.add_feedback()
            elif choice == '2':
                self.view_all_feedback()
            elif choice == '3':
                self.view_average_rating()
            elif choice == '4':
                break
            else:
                print('Invalid choice. Please try again.')

    def add_feedback(self):
        customer_name = input('Please enter your name: ')
        rating = int(input('Please give your visit a rating from 1-5: '))
        status, message = self.controller.add_feedback(customer_name, rating)
        print(f'{status}: {message}')

    def view_all_feedback(self):
        feedback = self.controller.view_all_feedback()
        print(feedback)

    def view_average_rating(self):
        message = self.controller.view_average_rating()
        print(message)
