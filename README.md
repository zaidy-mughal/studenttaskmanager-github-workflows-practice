# Student Task Manager

Project status: In Progress

A small Python console application to add, display, complete, and delete tasks.

Built for CSC418 DevOps for Cloud Computing — Lab Assignment 4.
Student: Muhammad Zaid Amjad (SP23-BSE-135)

## Features

- Add a task — empty or whitespace-only titles are rejected with a clear error message.
- Display all tasks — each task shows its ID, title, and status (Pending or Done).
- Mark a task as completed — by task ID; already-completed and missing IDs are reported separately.
- Delete a task — by task ID; only an existing, valid ID is deleted.
- Tasks are kept in memory while the app is running. Each task gets a new ID in order (1, 2, 3, ...).

## Setup

Requirements: Python 3.10 or newer. No external packages are needed.

```bash
git clone https://github.com/zaidy-mughal/github-workflows-practice.git
cd github-workflows-practice
python3 main.py
```

On Ubuntu, if `python` is not found, use `python3` in the commands below.
The app is a console program — run it in a terminal.

## Usage

Run the app and choose an option from the menu:

```text
--- Student Task Manager ---
1. Add Task
2. Display Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
```

Example:

1. Choose `1`, enter `Finish Lab 4` — the task is added as `[1] Finish Lab 4 - Pending`.
2. Choose `2` to see all tasks.
3. Choose `3`, enter `1` — the task becomes `[1] Finish Lab 4 - Done`.
4. Choose `4`, enter `1` — the task is deleted.
5. Choose `5` to exit.

If you enter an empty title, the app says `Error: Task title cannot be empty.`
and does not add the task. If you enter an ID that does not exist, the app
says `Task not found. Please enter a valid task ID.`

For a longer step-by-step guide, see [docs/userguide.md](docs/userguide.md).

## Testing

Run the automated tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

On Ubuntu, use `python3 -m unittest discover -s tests -v` if `python` is not found.

There are 5 tests in `tests/test_task_manager.py`, covering adding a task,
rejecting empty titles, marking a task complete, deleting a task, and
displaying an empty list.

Tests also run automatically on GitHub Actions (`.github/workflows/tests.yml`)
on every push to `main` and on every Pull Request to `main`.

## Project structure

```text
main.py                  Console menu (add, display, complete, delete, exit)
task_manager.py          Task and TaskManager: the task list and its operations
tests/test_task_manager.py  Automated unittest tests (5 tests)
.github/workflows/tests.yml  GitHub Actions workflow that runs the tests
docs/userguide.md        Short user guide
README.md                This file
LICENSE                  MIT License
```

## Release

Version 1.0.0 is published as a GitHub Release tagged `v1.0.0`.
See the Releases page on GitHub for the release notes.

## License

MIT License — see [LICENSE](LICENSE).
