# Student Task Manager - v1.1 Part E - 2026-11-18
"""Automated tests for the Student Task Manager (Part E).

Run from the repository root with:
    python -m unittest discover -s tests -v

Also works as a plain script:
    python tests/test_task_manager.py
"""

import os
import sys
import unittest

# Make `task_manager` importable when tests are run from the tests folder
# or by unittest discover, which adds the start directory to sys.path.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """Tests for adding, completing and deleting tasks."""

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        """Adding a task stores it with the given title, pending."""
        task = self.manager.add_task("Finish Lab 4")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Finish Lab 4")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.get_tasks()), 1)
        self.assertIn("Finish Lab 4", self.manager.display_tasks())

    def test_add_empty_task_is_rejected(self):
        """Empty and whitespace-only titles are rejected."""
        with self.assertRaises(ValueError):
            self.manager.add_task("")
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")
        self.assertEqual(len(self.manager.get_tasks()), 0)

    def test_complete_task(self):
        """Marking a task complete sets it to Done, once only."""
        self.manager.add_task("Revise CSC418 notes")
        self.assertTrue(self.manager.complete_task(1))
        self.assertTrue(self.manager.get_tasks()[0].completed)
        self.assertIn("Done", self.manager.display_tasks())
        # Completing again, or completing a missing task, returns False.
        self.assertFalse(self.manager.complete_task(1))
        self.assertFalse(self.manager.complete_task(99))

    def test_delete_task(self):
        """Deleting a task removes it, only for a valid task id."""
        self.manager.add_task("Task A")
        self.manager.add_task("Task B")
        self.assertTrue(self.manager.delete_task(2))
        self.assertEqual(len(self.manager.get_tasks()), 1)
        self.assertEqual(self.manager.get_tasks()[0].title, "Task A")
        # Deleting again, or deleting a missing task, returns False.
        self.assertFalse(self.manager.delete_task(2))
        self.assertFalse(self.manager.delete_task(99))

    def test_display_tasks_when_empty(self):
        """Displaying an empty list says there are no tasks yet."""
        self.assertEqual(self.manager.display_tasks(), "No tasks yet.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
