my_list={
    1:{"task":"Do Homework", "status":True},
    2:{"task":"Create Database", "status":False}
}

def add_task(id, task):
    if id in my_list:
        print("Task already exist")
    else:    
        my_list[id] = {"task": task, "status": False}
        print()
        print(f"Task added successfuly")

def checking_status(id):
    if id in my_list:
        if my_list[id]['status'] == False:
            print(f"Task {my_list[id]['task']} is not completed")
        else:
            print(f"Task {my_list[id]['task']} is completed")
    else:
        print("Task not found")        

def update_task(id, task=None, status=None):
    if id in my_list:
        if task is not None:
            my_list[id]['task']= task
            print("task updated successfuly")
        if status is not None:
            my_list[id]['status']= not my_list[id]['status']
            print("Task updated successfuly")
    else:
        print("Task not found")

def single_task(id):
    print()
    task=my_list.get(id)
    if task:
        status="Completed" if task['status'] else 'Pending'
        print(f"ID {id} : {task['task']} - {status}")
    else:
        print("Task not found")

def show_list():
    # task=my_list.get(id)
    if not my_list:
        print("No tasks")
    else:
        print()
        for id, task in my_list.items():
            status="Completed" if task['status'] else "Pending"
            print(f"ID {id} : {task['task']} - {status}") 
            print() 

def delete_task(id):
    if id in my_list:
        del my_list[id]
        print(f"Task {id} deleted")
    else:
        print("Task not found")

def delete_list():
    my_list.clear()
    print("All tasks deleted")
    
 


while True:
    print("""
  -----------------------------------------
  |  For adding new task press 1          |
  |  For checking status press 2          |
  |  For Updating task press 3            |
  |  For showing a single task press 4    |
  |  For showing the list press 5         |
  |  For deleting a single task press 6   |
  |  For deleting the whole list press 7  |
  |  For exiting press 0                  |
  -----------------------------------------
          """)
    try:      
        opt=int(input("Please enter your option here :"))


        if opt == 0:
            break

        elif opt == 1:
            add_new_id=int(input("Enter task ID : "))
            add_new_task=input("Enter task : ")
            add_task(add_new_id,add_new_task)

        elif opt == 2:
            id=int(input("Enter task ID : "))
            checking_status(id)

        elif opt == 3:
            opt2=int(input("Please enter task id here here :"))
            print("""
    ------------------------------------
    |  For Update Description press D  |
    |  For Update Status press S       |
    |  For Update Both press B         |
    ------------------------------------
            """)
    
            update=input("Enter your optiont here : ").lower()
            
            if update == 'd':
                new_task=input("Enter the new task here : ")
                update_task(opt2,task=new_task)
            elif update == 's':
                update_task(opt2,status= True)
            elif update == 'b':
                new_task=input("Enter the new task here : ")
                update_task(opt2,task=new_task,status=True)
            else:
                print("Invalid option")

        elif opt == 4:
            id=int(input("Enter task ID : "))
            single_task(id)

        elif opt == 5:
            show_list()

        elif opt == 6:
            id=int(input("Enter task id : "))
            delete_task(id)

        elif opt == 7:
            delete_list()    
    except ValueError:
        print("Invalid input")        