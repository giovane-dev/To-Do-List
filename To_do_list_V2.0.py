import mysql.connector as MySql

def connect_to_database():
    conn=MySql.connect(
        host='localhost',
        user='root',
        database='to_do_list',
        password='your password',
        port=4000)
        
    return conn
connect_to_database()

def setup_database():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
                   id INT PRIMARY KEY AUTO_INCREMENT,
                   task VARCHAR(255),
                   status bool
                   )''')
setup_database()

def insert(task):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, status) VALUES (%s, %s)", (task, False))
    conn.commit()
    print("================================")
    print("task added successfully")
    print("================================")
#insert('task_two')    

# def dynamic_update(id, task=None, status=None):
#     conn = connect_to_database()
#     cursor = conn.cursor()
#     if task:
#         cursor.execute(f"UPDATE tasks SET task = '{task}' WHERE id = {id}")
#     if status is not None:
#         new_status= 1 if status== 0 else 0
#         cursor.execute("UPDATE tasks SET status = %s WHERE id= %s", (new_status, id))

#     conn.commit()
#     print(f"task {id} updated successfully")

def dynamic_update(id, task=None, status=False):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        if task is not None:
            cursor.execute("UPDATE tasks SET task = %s WHERE id = %s", (task, id))
        if status:
            cursor.execute("UPDATE tasks SET status = NOT status WHERE id = %s", (id, ))
        conn.commit()
        print("================================")
        print(f"Task {id} updated successfully.")
        print("================================")
    except Exception as e:
        print("================================")
        print(f"An error occurred: {e}")
        print("================================")
    finally:
        conn.close()
# dynamic_update(id=1, status=False)
def update(id, task, status):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET task = %s, status = %s WHERE id = %s", (task, status, id))
    conn.commit()
    print("================================")
    print("task updated successfully")
    print("================================")
#update(id=1, task="task 1", status=False)
def show_task(id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
    task = cursor.fetchone()
    if task:
        # Assuming status is the second column, adjust index if needed
        status = "completed" if task[2] == 1 else "pending"  # Change index if necessary
        print("=======================================================")
        print(f"Task ID: {task[0]}\nTask: {task[1]}\nStatus: {status}")
        print("=======================================================")
    else:
        print("================================")
        print(f"No task found with ID {id}")
        print("================================")
    conn.close()
#show_task(id=1)
     
def show_tasks():
    conn= connect_to_database()
    cursor =conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        status = "completed" if task[2] == 1 else "pending"
        print("===========================================================")
        print(f"Task ID: {task[0]}, Task: {task[1]}, Status: {status}\n")
        print("===========================================================")

#show_tasks()     

def delete_task(id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    conn.commit()
    print("================================")
    print(f"Task {id} deleted successfully")
    print("================================")

def delete_tasks():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks")
    conn.commit()
    print("================================")
    print("All tasks deleted successfully")
    print("================================")
  

while True:
    print("1. Add task")
    print("2. Update task")
    print("3. Show task")
    print("4. Delete task")
    print("5. Show all tasks")
    print("6. Delete all tasks")
    print("0. Exit")
    try:
        opt=int(input("Enter your option : "))

        if opt==1:
            task=input("Enter Task here : ")
            insert(task)
        elif opt==2:
            print("""
            1. Change task
            2. Update status
            3. Update both
            """)
            opt2=int(input("Enter your option : "))
            if opt2==1:
                id=int(input("Enter task id : "))
                new_task=input("Enter new task here : ")
                dynamic_update(id=id,task=new_task)
            elif opt2==2:
                id=int(input("Enter task id : "))
                dynamic_update(id=id, status=True)
            elif opt2==3:
                id=int(input("Enter task id : "))
                new_task=input("Enter new task here : ")
                dynamic_update(id=id,task=new_task, status=True)
            else:
                print("================================")
                print("Invalid option")
                print("================================")

        elif opt==3:
            id=int(input("Enter task id : "))
            show_task(id)
        elif opt==4:
            id=int(input("Enter task id : "))
            delete_task(id)
            print("================================")
            print(f"task {id} deleted successfully")
            print("================================")
        elif opt==5:
            show_tasks()
        elif opt==6:
            delete_tasks()
        elif opt==0:
            print("================================")
            print("Exiting...")
            print("Thanks for using the To_do_list")
            print("================================")
            break
        
        else:
            print("Invalid option")
    except:
        print("================================")
        print("Invalid input")
        print("================================")




   

            

    # if status:
    #     if status== 0:
    #         cursor.execute(f"UPDATE tasks SET status = {True} WHERE id ={id}")
    #     else:
    #         cursor.execute(f"UPDATE tasks SET status = {False} WHERE id = {id}")


#     def dynamic_update(id, task=None, status=None):
#     conn = connect_to_database()
#     cursor = conn.cursor()
#     if task:
#         cursor.execute(f"UPDATE tasks SET task = '{task}' WHERE id = {id}")
#     if status is not None:
#         new_status= 1 if status== 0 else 0
#         cursor.execute("UPDATE tasks SET status = %s WHERE id= %s", (new_status, id))

#     conn.commit()
#     print(f"task {id} updated successfully")

# dynamic_update(id=1, status=True)  