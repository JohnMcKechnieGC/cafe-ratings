from ui.user_interface_abc import UserInterfaceABC
import tkinter as tk
from tkinter import messagebox, simpledialog


class CafeFeedbackTkInterUI(UserInterfaceABC):
    def __init__(self, controller):
        super().__init__(controller)
        self.root = tk.Tk()
        self.root.title('Cafe Feedback System')

        tk.Button(self.root, text='Add Feedback', command=self.add_feedback).pack()
        tk.Button(self.root, text='View All Feedback', command=self.view_all_feedback).pack()
        tk.Button(self.root, text='View Average Rating', command=self.view_average_rating).pack()
        tk.Button(self.root, text='Exit', command=self.root.quit).pack()

    def run(self):
        self.root.mainloop()

    def add_feedback(self):
        customer_name = simpledialog.askstring('Input', 'Enter customer name:', parent=self.root)
        rating = simpledialog.askinteger('Input', 'Enter rating (1-5):', parent=self.root, minvalue=1, maxvalue=5)
        status, message = self.controller.add_feedback(customer_name, rating)
        messagebox.showinfo(status, message)

    def view_all_feedback(self):
        feedback = self.controller.view_all_feedback()
        messagebox.showinfo('All Feedback', feedback)

    def view_average_rating(self):
        message = self.controller.view_average_rating()
        messagebox.showinfo('Average Rating', message)
