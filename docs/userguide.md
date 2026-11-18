# Student Task Manager — User Guide

A short guide to using the Student Task Manager. It is a console app:
you type a number from a menu, and the app does that job.

## Starting the app

You need Python 3.10 or newer, and nothing else to install.

```bash
git clone https://github.com/zaidy-mughal/github-workflows-practice.git
cd github-workflows-practice
python3 main.py
```

On Ubuntu, if `python` is not found, use `python3` as above.
You should see this menu:

```text
--- Student Task Manager ---
1. Add Task
2. Display Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
```

## A worked example

1. **Add a task.** Choose `1`, then type a title, for example `Finish Lab 4`.
   The app replies: `Task added: [1] Finish Lab 4 - Pending`
   The number in brackets is the task ID. Use it for the next steps.
2. **See your tasks.** Choose `2`. You will see:
   `[1] Finish Lab 4 - Pending`
3. **Complete the task.** Choose `3`, then type `1`.
   The app replies: `Task marked as completed.`
   Choose `2` again and you will see: `[1] Finish Lab 4 - Done`
4. **Delete the task.** Choose `4`, then type `1`.
   The app replies: `Task deleted.`
5. **Leave the app.** Choose `5`. The app says `Goodbye!` and exits.

Tasks are kept in memory while the app is running. When you exit,
the list is not saved — start the app again with an empty list.

## If something does not work as expected

- **Empty title:** if you press Enter without a title, the app says
  `Error: Task title cannot be empty.` and does not add a task.
  Type a real title and try again.
- **Wrong ID:** if you enter an ID that does not exist, for example `99`,
  the app says `Task not found. Please enter a valid task ID.`
  Choose `2` first to see the real IDs, then try again.
- **Already completed:** completing a task that is already Done says
  `Task is already completed.` — the task stays Done.
- **Not a number:** if you type letters where an ID is asked for, the app
  says `Please enter a valid number.` and asks again.

## Running the tests

From the repository root, run:

```bash
python -m unittest discover -s tests -v
```

Use `python3` instead of `python` on Ubuntu if needed. All 5 tests
should pass with `OK` at the end.
