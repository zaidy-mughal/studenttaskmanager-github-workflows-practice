"""Console menu for the Student Task Manager.

Run:  python3 main.py
"""

from task_manager import TaskManager


def show_menu():
    print("\n--- Student Task Manager ---")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            try:
                task = manager.add_task(title)
            except ValueError:
                print("Error: Task title cannot be empty.")
                continue
            print(f"Task added: {task}")

        elif choice == "2":
            print("\nYour tasks:")
            print(manager.display_tasks())

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if manager.complete_task(task_id):
                print("Task marked as completed.")
            else:
                print("Task not found.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if manager.delete_task(task_id):
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
