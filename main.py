from task_manager import TaskManager

def main():
    manager = TaskManager()
    task_id = 1

    while True:
        print("\n--- Student Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            manager.add_task(task_id, task_name)
            task_id += 1

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            tid = int(input("Enter task ID: "))
            manager.complete_task(tid)

        elif choice == "4":
            tid = int(input("Enter task ID: "))
            manager.delete_task(tid)

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
