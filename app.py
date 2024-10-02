def task():
    tasks = []  # Initialize as a list
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print("Today's tasks are:")
    print(tasks)  # Display tasks after all are added

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop: "))

        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task to '{up}'")
            else:
                print("Task not found.")

        elif operation == 3:
            delete_val = input("Enter the task name you want to delete = ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task '{delete_val}' has been successfully deleted.")
            else:
                print("Task not found.")

        elif operation == 4:
            print("Current tasks:")
            print(tasks)

        elif operation == 5:
            print("Exiting the task manager.")
            break

        else:
            print("Invalid operation. Please try again.")

# Corrected line
if __name__ == "__main__":
    task()
