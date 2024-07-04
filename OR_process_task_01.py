import json
tsks = []

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tsks, file)

def add_task():
    tsk = input("Enter the task: ")
    tsks.append({"task": tsk, "done": False})
    save_tasks()

def update_task():
    display_tasks()
    tsk_number = int(input("Enter the task number to update: ")) - 1
    if 0 <= tsk_number < len(tsks):
        new_tsk = input("Enter the new task: ")
        tsks[tsk_number]["task"] = new_tsk
        save_tasks()
    else:
        print("Invalid !!")

def delete_task():
    display_tasks()
    tsk_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= tsk_number < len(tsks):
        tsks.pop(tsk_number)
        save_tasks()
    else:
        print("Invalid task number!!")

def display_tasks():
    for i, tsk in enumerate(tsks, start=1):
        status = "Done" if tsk["done"] else "Not Done"
        print(f"{i}. {tsk['task']} - {status}")

def mark_task_done():
    display_tasks()
    tsk_number = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= tsk_number < len(tsks):
        tsks[tsk_number]["done"] = True
        save_tasks()
    else:
        print("Invalid task number.")

def main():
    global tsks
    tsks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Mark Task as Done")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            mark_task_done()
        elif choice == "6":
            break
        else:
            print("Invalid choice ! Please choose again.")

if __name__ == "__main__":
    main()
