Python Expense Tracker
This repository contains a simple expense tracker application built using Python and Tkinter. It allows users to add and view expenses, storing them in a SQLite database.

Features
Add Expenses: Users can input date, category, amount, and description of expenses.
View Expenses: A separate window displays a list of all recorded expenses.
Error Handling: Alerts users to invalid input and required fields.
Clear Entries: Option to clear all input fields.
Installation
Clone the repository:

bash
Copy code:
git clone https://github.com/JAYXAD/python-expense-tracker.git
cd python-expense-tracker
Install dependencies:
Ensure you have Python installed. Tkinter and SQLite are typically included with Python distributions.

Run the application:

bash
Copy code:
python expense_tracker.py
Usage
Add an Expense:

Fill in the date, category, amount, and description fields.
Click "Add Expense" to save the entry.
Clear Entries:

Click "Clear Entries" to reset all input fields.
View Expenses:

Click "Show Expenses" to open a new window displaying all saved expenses.
Code Overview
Main Window:

Provides input fields for date, category, amount, and description.
Buttons to add expenses, clear entries, and show all expenses.
Expense List Window:

Displays a list of all expenses from the SQLite database.
Scrollable listbox for easy navigation of expenses.
Database Operations:

Uses SQLite to store and retrieve expense data.
Ensures data persistence between application runs.
Contributing
Contributions are welcome! If you have suggestions or improvements, please feel free to submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or suggestions, feel free to contact me at jayadityameesala@gmail.com.
