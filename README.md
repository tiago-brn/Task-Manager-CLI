# 📝 Task Manager CLI

A task manager playable in the terminal, with your tasks saved automatically in a local JSON file.

## Overview

The program opens an interactive prompt where you manage your to-do list with simple commands. You can add tasks, list them, mark them as completed and delete them. Your tasks are saved after every change, so they are still there the next time you launch the program.

## Commands

- Type a command at the `>` prompt and press Enter.
- `add`: add a new task (you are asked for its description).
- `list`: display all tasks with their number and status (`Done` or `Unaccomplished`).
- `complete`: mark a task as completed (you are asked for its number).
- `delete`: delete a task (you are asked for its number).
- `quit` (or `q`, `exit`): save and leave the program.

Invalid input is handled: unknown commands, invalid task numbers, non-numeric input and empty descriptions will not crash the program.

## Requirements

- [Python 3](https://www.python.org/downloads/)

No external library is needed.

## Installation and launch

```bash
git clone https://github.com/tiago-brn/Task-Manager-CLI.git
cd Task-Manager-CLI
python main.py
```

> On Linux/macOS, use `python3 main.py` if `python` does not work.

## Example session

```
> add
Enter the task description: Revise Docker

> add
Enter the task description: Write the README

> list
1. Revise Docker - Unaccomplished
2. Write the README - Unaccomplished

> complete
1. Revise Docker - Unaccomplished
2. Write the README - Unaccomplished
Enter the task number to mark as completed: 2
Task 2 marked as completed.

> quit
Tasks saved. Goodbye!
```

## Project structure

```
.
├── main.py       # Entry point: main loop and command dispatch
├── tasks.py      # Task logic: add, list, complete, delete
└── storage.py    # Loading and saving tasks in tasks.json
```

## Where your tasks are stored

Tasks are saved in `tasks.json`, created automatically the first time you save. Each task is a dictionary with a description and a completion status:

```json
[
    {
        "task": "Revise Docker",
        "completed": false
    }
]
```

The file is ignored by Git (see `.gitignore`) because it contains your personal data. To start from a clean list, simply delete `tasks.json`.

## Author

Project made by [Tiago](https://github.com/tiago-brn).