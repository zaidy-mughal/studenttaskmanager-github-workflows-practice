# Student Task Manager - v1.0 Part A - 2026-11-18
"""Core logic for the Student Task Manager.

Part A: a simple, working version with add, display, complete and delete.
Part B branches will harden each feature in turn:
  - feature/addtask: reject empty titles
  - feature/completetask: validate the task id before completing
  - feature/deletetask: validate the task id before deleting
"""


class Task:
    """One student task."""

    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.id}] {self.title} - {status}"


class TaskManager:
    """Keeps the task list in memory and offers the four operations."""

    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        """Add a task and return it."""
        task = Task(self._next_id, title)
        self._next_id += 1
        self.tasks.append(task)
        return task

    def get_tasks(self):
        """Return all tasks."""
        return self.tasks

    def display_tasks(self):
        """Return a printable list of tasks, or a message when empty."""
        if not self.tasks:
            return "No tasks yet."
        return "\n".join(str(task) for task in self.tasks)

    def complete_task(self, task_id):
        """Mark the task with this id as completed. Returns True/False."""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False

    def delete_task(self, task_id):
        """Delete the task with this id.

        Only a valid, existing task id is deleted
        (feature/deletetask). Returns True when a task was
        deleted, and False when the id does not exist.
        """
        if not isinstance(task_id, int) or isinstance(task_id, bool):
            return False
        for task in list(self.tasks):
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False
