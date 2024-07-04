import tkinter as tk
from tkinter import messagebox
import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks()
        entry.delete(0, tk.END)
        display_tasks()

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        tasks.pop(task_index)
        save_tasks()
        display_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected")

def mark_task_done():
    try:
        task_index = listbox.curselection()[0]
        tasks[task_index]["done"] = True
        save_tasks()
        display_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected")

def display_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "Done" if task["done"] else "Not Done"
        listbox.insert(tk.END, f"{task['task']} - {status}")

tasks = load_tasks()

app = tk.Tk()
app.title("To-Do List")

frame = tk.Frame(app)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=10)

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

done_button = tk.Button(app, text="Mark as Done", command=mark_task_done)
done_button.pack(side=tk.LEFT)

display_tasks()
app.mainloop()
