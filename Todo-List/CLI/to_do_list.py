import json
import os

class ToDoList:
    def __init__(self):
        self.filename = "tasks.json"
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

    def view_tasks(self):
        for idx, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx + 1}. {task['task']} - {status}")

    def update_task(self, task_number, completed=True):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = completed
            self.save_tasks()
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
            self.save_tasks()
        else:
            print("Invalid task number.")

def main():
    to_do_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            to_do_list.add_task(task)
        elif choice == '2':
            to_do_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            to_do_list.update_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            to_do_list.delete_task(task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
