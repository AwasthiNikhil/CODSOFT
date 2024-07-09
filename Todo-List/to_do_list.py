import json
import os
import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def update_task(self, task_index, completed=True):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = completed
            self.save_tasks()

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.to_do_list = ToDoList()

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.pack(pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.to_do_list.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")

    def load_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        for idx, task in enumerate(self.to_do_list.tasks):
            task_text = task["task"]
            if task["completed"]:
                task_text += " (Completed)"
            
            task_label = tk.Label(self.tasks_frame, text=task_text, width=50, anchor='w')
            task_label.grid(row=idx, column=0)

            complete_button = tk.Button(self.tasks_frame, text="Complete", command=lambda idx=idx: self.complete_task(idx))
            complete_button.grid(row=idx, column=1)

            delete_button = tk.Button(self.tasks_frame, text="Delete", command=lambda idx=idx: self.delete_task(idx))
            delete_button.grid(row=idx, column=2)

    def complete_task(self, task_index):
        self.to_do_list.update_task(task_index, completed=True)
        self.load_tasks()

    def delete_task(self, task_index):
        self.to_do_list.delete_task(task_index)
        self.load_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()
