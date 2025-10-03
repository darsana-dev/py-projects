tasks = []

def show_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def main():
    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

main()