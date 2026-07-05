# CODSOFT Internship - Task 1
# To-Do List Application

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        if len(tasks) > 0:
            try:
                task_no = int(input("Enter task number to update: "))
                if 1 <= task_no <= len(tasks):
                    new_task = input("Enter new task: ")
                    tasks[task_no - 1] = new_task
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        show_tasks()
        if len(tasks) > 0:
            try:
                task_no = int(input("Enter task number to delete: "))
                if 1 <= task_no <= len(tasks):
                    deleted = tasks.pop(task_no - 1)
                    print(f"Task '{deleted}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice! Please try again.")