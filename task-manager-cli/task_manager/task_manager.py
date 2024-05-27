import json
import os
import sys

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file):
        json.dump(tasks, file)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['description']} [{status}]")

def complete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f"Completed task: {tasks[task_index]['description']}")
    else:
        print("Invalid task number")

def remove_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Removed task: {removed_task['description']}")
    else:
        print("Invalid task number")

def main():
    if len(sys.argv) < 2:
        print("Usage: task-manager <command> [<args>]")
        return

    command = sys.argv[1]

    if command == "add":
        description = " ".join(sys.argv[2:])
        if description:
            add_task(description)
        else:
            print("Task description cannot be empty.")
    elif command == "list":
        list_tasks()
    elif command == "complete":
        if len(sys.argv) > 2 and sys.argv[2].isdigit():
            complete_task(int(sys.argv[2]) - 1)
        else:
            print("Please provide a valid task number.")
    elif command == "remove":
        if len(sys.argv) > 2 and sys.argv[2].isdigit():
            remove_task(int(sys.argv[2]) - 1)
        else:
            print("Please provide a valid task number.")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
