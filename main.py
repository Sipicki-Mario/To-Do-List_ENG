import os

# File to store the tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from a file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]  # Clean up the tasks
            return tasks
    return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display the menu
def display_menu():
    print("\n==== To-Do List ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    print("=====================")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a new task
def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added to the list!")

# Function to mark a task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] += " [Done]"
            save_tasks(tasks)
            print(f"Task '{tasks[task_num - 1]}' marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid task number!")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid task number!")

# Main function to run the to-do list application
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_done(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please select a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid choice.")

if __name__ == "__main__":
    main()
