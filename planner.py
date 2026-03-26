

tasks=[]
while True:
    print("\n-----Smart Study Planner-----")
    print("1.Add Task")
    print("2.View Task")
    print("3.Mark as Done")
    print("4.Delete Task")
    print("5.Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        task=input("Enter your task:")
        duration=int(input("Enter time required:"))
        task={
            "name":task,
            "duration":duration,
            "done": False
        }
        tasks.append(task)
        print("Task Added!")
    elif choice =='2':
        if len(tasks)==0:
            print("No tasks available.")
        else:             #view tasks+reminder
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                t = tasks[i]
                status = "Done" if t["done"] else "Pending"

                # Reminder logic
                if not t["done"]:
                    reminder = "⚠ Complete this task!"
                else:
                    reminder = ""

                print(f"{i + 1}. {t['name']} | {t['duration']} hrs | {status} {reminder}")
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]['name']}")

            num = int(input("Enter task number: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print("Marked as done!")
            else:
                print("Invalid number!")
    elif choice =='4':
        if len(tasks)==0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num=int(input("Enter your task number to delete:"))
            if  1 <= num <= len(tasks):
                tasks.pop(num -1)
                print("Task deleted!")
            else:
                print("invalid number!")
    elif choice =='5':
        print("Goodbye")
        break
    else:
        print("Invalid choice!")

















