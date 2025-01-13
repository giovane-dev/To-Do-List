import mysql.connector as MySql
from tkinter import *
from tkinter import ttk, messagebox

def connect_to_database():
    conn=MySql.connect(
        host="localhost",
        user="root",
        password="your password",
        database="database name",
        port="port"
    )
    return conn
def setup_database():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
                   id INT PRIMARY KEY AUTO_INCREMENT,
                   task VARCHAR(255),
                   status bool
                   )''')
setup_database()
def center_window(window, width, height):
     screen_width = window.winfo_screenwidth() 
     screen_height = window.winfo_screenheight() 
     x = (screen_width // 2) - (width // 2) 
     y = (screen_height // 2) - (height // 2) 
     window.geometry(f'{width}x{height}+{x}+{y}')

main_window=Tk()
main_window.config(bg='gray')
main_window.title("To Do List")
center_window(main_window, 400, 500)
main_window.iconbitmap("to_do_list.ico")


def add():
    conn = connect_to_database()
    cursor = conn.cursor()
    task = Add_enter.get()
    if task.strip():
        cursor.execute("INSERT INTO tasks (task, status) VALUES (%s,%s)", (task,False))
        conn.commit()
        Add_enter.delete(0, END)
        messagebox.showinfo("Success", "Task added successfully")
    else:
        messagebox.showerror("Error", "Please enter a task")    
def update():
    conn = connect_to_database()
    cursor = conn.cursor()
    def fetch():
        task_id= id_entry.get()
        if task_id:
            conn = connect_to_database()
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM tasks WHERE id ={task_id}")
            rows = cursor.fetchone()
            conn.close()
            if rows:
                task_var.set(rows[1])
                var.set(rows[2])
                if rows[2]:
                    var.set(True)
                else:
                    var.set(False)
            else:
                messagebox.showerror("Error", "Task not found", parent=update_window)
        else:
            messagebox.showerror("Error", "Please enter task id", parent=update_window)
    def update_task():
        task_id=id_entry.get()
        task=task_var.get()
        status=var.get()
        try:
            if task_id:
                conn = connect_to_database()
                cursor = conn.cursor()
                cursor.execute(f"UPDATE tasks SET task = '{task}', status = {status} WHERE id = {task_id}")
                conn.commit()
                conn.close()
                id_entry.delete(0, END)
                task_var.set("")
                var.set(False)
                update_window.destroy()
                messagebox.showinfo("Success", "Task updated successfully")
            else:
                messagebox.showerror("Error", "Please enter task id")
        except Exception as e:
            messagebox.showerror("Error", e)
    

    update_window=Toplevel(master=main_window, bg="#09b7e3")
    update_window.title("Update Task")
    update_window.iconbitmap("to_do_list.ico")
    center_window(update_window, 330, 170)
    update_window.resizable(0,0) 
    button_frame=Frame(update_window, bg="#09b7e3")
    main_frame=Frame(update_window, bg="#09b7e3")
    main_frame.pack(pady=5, padx=5, fill=X)
    button_frame.pack(pady=5, padx=5, anchor=CENTER)
    

    id_label=Label(master=main_frame, text="ID", font=("arial", 10), bg="#09b7e3")
    id_label.grid(column=0, row=0 , pady=20, padx=10)
    id_entry=Entry(master=main_frame, width=5, font=('Arial', 10)) 
    id_entry.grid(column=0, row=1, pady=5, padx=20)
    fetch_button=Button(master=button_frame, text="Fetch",command=fetch, width=10)
    fetch_button.grid(column=0, row=0, pady=17, padx=10)

    task_label=Label(master=main_frame, text='Task', font=('arial', 10), bg="#09b7e3")
    task_label.grid(column=1, row=0, pady=5, padx=10)
    task_var=StringVar()
    update_task_entry=Entry(master=main_frame, textvariable=task_var , width=20, font=('Arial',10))
    update_task_entry.grid(column=1, row=1, pady=5, padx=10)
    status_label=Label(master=main_frame, text='Status', font=('arial', 10), bg="#09b7e3")
    status_label.grid(column=2, row=0, pady=5, padx=10)
    var= IntVar()
    status=Checkbutton(master=main_frame, variable=var, bg="#09b7e3")
    status.grid(column=2, row=1, padx=10, pady=5)
    submit_update=Button(master=button_frame, text="Update", command=update_task, width=10)
    submit_update.grid(column=1, row=0 ,padx=17, pady=5)
   
def delete():
    conn = connect_to_database()
    cursor = conn.cursor()
    delete_window=Toplevel(master=main_window, bg="#09b7e3")
    delete_window.title("Delete Task")
    center_window(delete_window, 230,80)
    delete_window.resizable(0,0)
    delete_window.iconbitmap("to_do_list.ico")
    def confirm_delete():
        id=id_entry.get()
        if id:
            try:
                conn=connect_to_database()
                cursor=conn.cursor()
                cursor.execute(f"SELECT id FROM tasks WHERE id={id}")
                task_exists=cursor.fetchone()
                if not task_exists:
                    messagebox.showerror("Error", "Task does not exist")
                    delete_window.destroy()
                    return
                cursor.execute(f"DELETE FROM tasks WHERE id={id}")
                conn.commit()
                conn.close
                messagebox.showinfo("Success", "Task deleted successfully")
                delete_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter a valid ID")
    main_frame=Frame(delete_window, bg="#09b7e3")
    main_frame.pack(pady=20, padx=15)
    id_label=Label(master=main_frame, text="ID", font=("arial", 10), bg="#09b7e3")
    id_label.grid(column=0, row=0 , pady=5, padx=10)
    id_entry=Entry(master=main_frame, width=5, font=('Arial', 10))
    id_entry.grid(column=1, row=0, pady=5, padx=10)
    delete_button=Button(master=main_frame, text="Delete",command=confirm_delete, width=10)
    delete_button.grid(column=2, row=0, pady=5, padx=10)


def show():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    records=cursor.fetchall()
    conn.close()
    show_window=Toplevel(master=main_window)
    show_window.title("Show Tasks")
    show_window.iconbitmap("to_do_list.ico")
    center_window(show_window, 400, 400)
    
    tree= ttk.Treeview(show_window, columns=("0","1", "2"),show="headings")
    tree.heading("0", text="ID", anchor=CENTER)
    tree.heading("1", text="Task", anchor=CENTER)
    tree.heading("2", text="Status", anchor=CENTER)
    
    tree.column("0", minwidth=50, width=60, anchor=CENTER)
    tree.column("1", minwidth=80, width=100, anchor=CENTER)
    tree.column("2", minwidth=50, width=60, anchor=CENTER)

    for record in records:
        tree.insert("", "end", values=record)
    tree.pack(fill="both", expand=True)    


main_label=Label(master=main_window, text="To do list", font=("Comic Sans MS",20), fg="#000080",bg='gray')
main_label.pack(pady=20)
Add_enter=Entry(master=main_window, width=25, font=('Arial', 13), borderwidth=7)
Add_enter.pack(pady=20)

Add_button=Button(master=main_window, text="Add", font=('Fixedsys', 15), width=20, command=add)
Add_button.pack(pady=20)

Update_button=Button(master=main_window, text="Update", font=('Fixedsys',15), width=20, command=update)
Update_button.pack(pady=20)

Delete_button=Button(master=main_window, text="Delete", font=('Fixedsys',15), width=20, command=delete)
Delete_button.pack(pady=20)

View_button=Button(master=main_window, text="View Tasks", font=('Fixedsys', 15), width=20, command=show)
View_button.pack(pady=20)

main_window.mainloop()