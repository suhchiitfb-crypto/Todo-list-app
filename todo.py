
class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return {"title": self.title, "done": self.done}

    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"])
        task.done = data["done"]
        return task

    def __str__(self):
        status = "✓" if self.done else " "
        return "[" + status + "] " + self.title
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)    
        return [Task.from_dict(item) for item in data]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump([task.to_dict() for task in tasks], file)
tasks = load_tasks()

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")
    print("5. Clear all tasks")
    print("6. Mark task as done")
    choice = input("Choose an option: ")

    if choice == "1":
        new_task_title = input("Enter the task: ")
        new_task = Task(new_task_title)
        tasks.append(new_task)
        save_tasks(tasks)
        print("Added: " + new_task.title)

    elif choice == "2":
        if len(tasks) == 0:
            print("Your list is empty.")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + str(tasks[i]))

    elif choice == "3":
        if len(tasks) == 0:
            print("Nothing to remove.")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + str(tasks[i]))
            remove_num = input("Enter the number to remove: ")
            if remove_num.isdigit() and 1 <= int(remove_num) <= len(tasks):
                removed = tasks.pop(int(remove_num) - 1)
                save_tasks(tasks)
                print("Removed: " + removed.title)
            else:
                print("Invalid number.")

    elif choice == "5":
        confirm = input("Are you sure you want to clear all tasks? (y/n):")
        if confirm.lower() == "y":
            tasks.clear()
            save_tasks(tasks)
            print("All tasks cleared.")
        else:
            print("clear all tasks canceled.")

    elif choice == "6":
        if len(tasks) == 0:
            print("Nothing to mark as done.")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + str(tasks[i]))
            mark_num = input("Enter the number to mark as done: ")
            if mark_num.isdigit() and 1 <= int(mark_num) <= len(tasks):
                tasks[int(mark_num) - 1].mark_done()
                save_tasks(tasks)
                print("Task marked as done.")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.")
