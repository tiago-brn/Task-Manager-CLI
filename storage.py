import json

def load_tasks():
    """
    Load tasks from the storage file.
    """
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """
    Save tasks to the storage file.
    """
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

