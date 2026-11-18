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

    def get_task_by_id(self, task_id):
        """Return the task with this id, or None if there is no such task."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        """Mark the task with this id as completed.

        Returns True only when a pending task is newly completed.
        Returns False when the id does not exist, or the task
        is already completed (feature/completetask).
        """
        task = self.get_task_by_id(task_id)
        if task is None or task.completed:
            return False
        task.completed = True
        return True

    def delete_task(self, task_id):
        """Delete the task with this id. Returns True/False."""
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False
