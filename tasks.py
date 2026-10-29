from storage import load_tasks

tasks = load_tasks()

def add_task():
    """
    Add a new task to the task list.
    """
    new_task = input("Enter the task description: ")
    if new_task:
        tasks.append({"task": new_task, "completed": False})


def list_tasks():
    """
    List all tasks with their status.
    """
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Unaccomplished"
        print(f"{index}. {task['task']} - {status}")

def complete_task():
    """
    Mark a task as completed.
    """
    list_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    """
    Delete a task from the task list.
    """
    list_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            print(f"Task {task_number} deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
                print("Please enter a valid number.")