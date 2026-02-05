import os

TASK_FILE = "task.txt"

def load_task():
    tasks = []
    if(os.path.exists(TASK_FILE)): 
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                task, status = line.strip().rsplit('||', 1)
                tasks.append({"task": task, "status": status})
    print(tasks)

def save_task(tasks):
    with open(TASK_FILE, 'w', encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task['status'] == "done" else "not_done"
            f.write(f"{task['task']}||{status}\n") 

def display_task(tasks):
    if not tasks:
        print("No tasks fount")
    else:
        for i, task in (enumerate(tasks, 1)):
            checkbox = "✅" if task["status"] == "done" else " "
            print(f"{i}. [{checkbox}] {task['task']}")
        print()

def task_manager():
    tasks = load_task()

    while True:
        print("\n----- Task Manager -----")
        print("1. Add tasks")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter an option(1-5): ").strip()

        match choice:
            case "1":
                task = input("Enter your task: ").strip()
                if task:
                    tasks.append({"task": task, "status":"not_done"})
                    save_task(tasks)
                    print("Task added")
                else:
                    print("Task can not be empty")
                
            case "2":
                display_task(tasks)

            case "3":
                display_task(tasks)

                try:
                    task_no = int(input("Enter a task no. to mark as done: "))
                    if 1 <= task_no <= len(tasks):
                        tasks[task_no-1]["status"] = "done"
                        save_task(tasks)
                        print("Task marked as done ")
                    else:
                        print("Invalid Task No.")
                except ValueError:
                    print("Please enter a number")
                
            case "4":
                display_task(tasks)

                try:
                    task_no = int(input("Enter a task no. to delete: "))
                    if 1 <= task_no <= len(tasks):
                        deleted = tasks.pop(task_no-1)
                        save_task(tasks)
                        print(f"Deleted the task {deleted}")
                    else:
                        print("Invalid Task No.")
                except ValueError:
                    print("Please enter a number")
                 
            case "5":
                print("Exiting the Task manager")
                break

            case _:
                print("Enter a right option")
                    
task_manager()


