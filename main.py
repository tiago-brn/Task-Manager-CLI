import tasks as task_manager
from storage import save_tasks


COMMANDS = {
    "add": task_manager.add_task,
    "list": task_manager.list_tasks,
    "complete": task_manager.complete_task,
    "delete": task_manager.delete_task,
}


def main():
    print("------------------------------------------------------------------------------------------------------------------------")
    print("\nWelcome to the Task Manager CLI!")
    print("\nYou can manage your tasks using the following commands")
    print("\nUsable commands: add, list, complete, delete, quit")

    while True:
        command = input("\n> ").strip().lower()

        if command in ("quit", "q", "exit"):
            save_tasks(task_manager.tasks)
            print("Tasks saved. Goodbye!")
            break

        function = COMMANDS.get(command)
        if function is None:
            print("Unknown command. Use: add, list, complete, delete, quit")
            continue

        function()
        if command in ("add", "complete", "delete"):
            save_tasks(task_manager.tasks)


if __name__ == "__main__":
    main()