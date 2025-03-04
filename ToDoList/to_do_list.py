import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
TASKS_FILE = "tasks.txt"


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="lightgray")

        # Title Label
        self.label = tk.Label(root, text="To-Do List", font=("Arial", 14, "bold"), bg="lightgray")
        self.label.pack(pady=10)

        # Listbox to display tasks
        self.listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12), selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Entry box for new tasks
        self.task_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.task_entry.pack(pady=5)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="lightgray")
        self.button_frame.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, width=12)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", command=self.remove_task, width=12)
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)

        self.complete_button = tk.Button(self.button_frame, text="Mark Completed", command=self.complete_task, width=12)
        self.complete_button.grid(row=1, column=0, padx=5, pady=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear All", command=self.clear_tasks, width=12)
        self.clear_button.grid(row=1, column=1, padx=5, pady=5)

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to remove!")

    def complete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task_text = self.listbox.get(selected_task_index)

            # If task is already marked completed, unmark it
            if task_text.startswith("✔ "):
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, task_text[2:])
            else:
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, "✔ " + task_text)

            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to mark as completed!")

    def clear_tasks(self):
        self.listbox.delete(0, tk.END)
        self.save_tasks()

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            tasks = self.listbox.get(0, tk.END)
            for task in tasks:
                file.write(task + "\n")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    self.listbox.insert(tk.END, task.strip())


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()