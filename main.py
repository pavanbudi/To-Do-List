tasks = []

def add_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print("Task added!")
  
def delete_task():
    if len(tasks)==0:
        print("There are no tasks in the list.")
    else:
        i=int(input("Enter index of task to be deleted:"))
        if 1<=i<=len(tasks):
            del tasks[i-1]
        else:
            print("Task doesn't exist")

def view_tasks():
    if not tasks:
        print("There are no tasks in the list.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Close")
    choice = input("Enter your choice:")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Closing..")
        break
    else:
        print("Invalid choice. Please try again.")

