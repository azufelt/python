"""
Ashley Zufelt
To Do List
May 5, 2022
"""

from tkinter import *

# Create item
def add_item(entry: Entry, listbox: Listbox) :
  new_task = entry.get()

  listbox.insert(END, new_task)

  with open('tasks.txt', 'a') as tasks_list_file:
    tasks_list_file.write(f'\n{new_task}')

# Delete Item
def delete_item(listbox: Listbox):
  listbox.delete(ACTIVE)

  with open('tasks.txt', 'r+') as tasks_list_file:
    lines = tasks_list_file.readlines()

    tasks_list_file.truncate()

    for line in lines:
      if listbox.get(ACTIVE) == line[:-2]:
        lines.remove(line)
      tasks_list_file.write(line)

# Initializing the to do list GUI
root = Tk()
root.title('My To Do List')
root.geometry('600x800')
root.resizable(0, 0)
root.config(bg="White")

# Create Heading Label
Label(root, text='My To Do List', bg='white', font=("Helvetica", 15), wraplength=500).place(x=35, y=15)

# Listbox with tasks and scroll bar
tasks = Listbox(root,selectbackground='Gold', bg='lightgray', font=('Helvetica', 12), height=18, width=25)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=260, y=50, height=232)

tasks.config(yscrollcommand=scroller.set)

tasks.place(x=40, y=50)

# Add tasks to the List
with open('tasks.txt', 'r+') as tasks_list:
  for task in tasks_list:
    tasks.insert(END, task)

# Create Entry widget to enter new item
new_item_entry = Entry(root, bg='white', width=37)
new_item_entry.place(x=35, y=400)

# Create Buttons
add_btn = Button(root, text='Add Task', bg='Azure', width=10, font=('Helvetica', 12), command=lambda: add_item(new_item_entry, tasks))
add_btn.place(x=45, y=350)

delete_btn = Button(root, text='Delete Task', bg='Azure', font=('Helvetica',12), command=lambda: delete_item(tasks))
delete_btn.place(x=150, y=350)

# Finalize Window
root.update()
root.mainloop()

