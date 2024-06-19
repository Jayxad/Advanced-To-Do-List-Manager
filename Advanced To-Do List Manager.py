import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog
import sqlite3
from datetime import datetime

# Task and Category classes
class Task:
    def __init__(self, title, description="", due_date=None, priority=1, category=None, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nCategory: {self.category}\nStatus: {status}"

# To-Do List Manager Application
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced To-Do List Manager")

        self.initialize_database()
        self.initialize_gui()

    def initialize_database(self):
        self.conn = sqlite3.connect('tasks.db')
        self.create_tables()
        self.load_tasks()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            description TEXT,
                            due_date TEXT,
                            priority INTEGER DEFAULT 1,
                            category TEXT,
                            completed INTEGER DEFAULT 0
                        )''')
        self.conn.commit()

    def load_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM tasks''')
        rows = cursor.fetchall()
        self.tasks = []
        for row in rows:
            task = Task(row[1], row[2], row[3], row[4], row[5], bool(row[6]))
            self.tasks.append(task)

    def save_task(self, task):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO tasks (title, description, due_date, priority, category, completed) 
                          VALUES (?, ?, ?, ?, ?, ?)''', 
                       (task.title, task.description, task.due_date, task.priority, task.category, 1 if task.completed else 0))
        self.conn.commit()
        self.load_tasks()

    def remove_task(self, title):
        cursor = self.conn.cursor()
        cursor.execute('''DELETE FROM tasks WHERE title = ?''', (title,))
        self.conn.commit()
        self.load_tasks()

    def complete_task(self, title):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE tasks SET completed = 1 WHERE title = ?''', (title,))
        self.conn.commit()
        self.load_tasks()

    def list_tasks(self):
        top = tk.Toplevel()
        top.title("List of Tasks")
        top.configure(bg="#222222")

        text_area = scrolledtext.ScrolledText(top, width=80, height=20, bg="#363636", fg="white")
        text_area.pack(padx=10, pady=10)

        for task in self.tasks:
            text_area.insert(tk.END, str(task) + "\n\n")

    def initialize_gui(self):
        # GUI elements
        self.root.configure(bg="#222222")

        self.label_title = tk.Label(self.root, text="To-Do List Manager", font=("Arial", 18), bg="#222222", fg="#00FF00")
        self.label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Password entry
        password = simpledialog.askstring("Password", "Enter password:", show='*')
        if password != "meesala":
            messagebox.showerror("Error", "Incorrect password. Exiting...")
            root.destroy()
            return

        self.label_task_input = tk.Label(self.root, text="Enter Task:", bg="#222222", fg="white")
        self.label_task_input.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_task_input = tk.Entry(self.root, width=50)
        self.entry_task_input.grid(row=1, column=1, padx=10, pady=5)

        self.label_task_description = tk.Label(self.root, text="Description:", bg="#222222", fg="white")
        self.label_task_description.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_task_description = tk.Entry(self.root, width=50)
        self.entry_task_description.grid(row=2, column=1, padx=10, pady=5)

        self.label_task_due_date = tk.Label(self.root, text="Due Date (YYYY-MM-DD HH:MM):", bg="#222222", fg="white")
        self.label_task_due_date.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_task_due_date = tk.Entry(self.root, width=20)
        self.entry_task_due_date.grid(row=3, column=1, padx=10, pady=5)

        self.label_task_priority = tk.Label(self.root, text="Priority (1-5):", bg="#222222", fg="white")
        self.label_task_priority.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_task_priority = tk.Entry(self.root, width=5)
        self.entry_task_priority.grid(row=4, column=1, padx=10, pady=5)

        self.label_task_category = tk.Label(self.root, text="Category:", bg="#222222", fg="white")
        self.label_task_category.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_task_category = tk.Entry(self.root, width=20)
        self.entry_task_category.grid(row=5, column=1, padx=10, pady=5)

        self.button_add_task = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#006400", fg="white")
        self.button_add_task.grid(row=6, column=0, padx=10, pady=10, sticky=tk.EW)

        self.button_list_tasks = tk.Button(self.root, text="List Tasks", command=self.list_tasks, bg="#006400", fg="white")
        self.button_list_tasks.grid(row=6, column=1, padx=10, pady=10, sticky=tk.EW)

        self.label_status = tk.Label(self.root, text="", fg="green", bg="#222222")
        self.label_status.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        # Display current date and time
        self.label_current_datetime = tk.Label(self.root, text=f"Current Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}", bg="#222222", fg="white")
        self.label_current_datetime.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

    def add_task(self):
        title = self.entry_task_input.get().strip()
        description = self.entry_task_description.get().strip()
        due_date_str = self.entry_task_due_date.get().strip()
        priority = int(self.entry_task_priority.get().strip() or 1)
        category = self.entry_task_category.get().strip()

        if not title:
            messagebox.showerror("Error", "Task title cannot be empty.")
            return

        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d %H:%M')
            except ValueError:
                messagebox.showerror("Error", "Invalid due date format. Please use YYYY-MM-DD HH:MM.")
                return
        else:
            due_date = None

        task = Task(title, description, due_date, priority, category)
        self.save_task(task)
        self.label_status.config(text="Task added successfully!", fg="green")

# Initialize the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
