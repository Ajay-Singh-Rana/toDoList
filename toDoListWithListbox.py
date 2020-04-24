# h3avren@py
import tkinter as tk

# main window
mainWindow = tk.Tk()
mainWindow.geometry("400x300")
mainWindow.resizable(False,False)
mainWindow.config(bg="White")

# variables
index = 0

# bottom frame to hold buttons for adding and deleting tasks
bottomFrame = tk.Frame(mainWindow,bg="White")
bottomFrame.pack(side = tk.BOTTOM)

# listbox to hold tasks,it goes in the leftFrame
taskBox = tk.Listbox(mainWindow,bg="White",fg="Black")
taskBox.pack()

# funtionality to add tasks
def add_task(taskEntryBox):
    global index
    taskString = taskEntryBox.get("1.0","end-1c")
    if(taskString!=""):
        taskString = str(index) + " " + taskString
        taskBox.insert(index,taskString)
        index +=1

# pop up window for add button to enter tasks
def create_task_window():
    taskWindow = tk.Toplevel()
    taskWindow.resizable(False,False)
    taskWindow.geometry("200x88")
    taskEntryBox = tk.Text(taskWindow,width=200,height=3,bg="White",fg="Black",insertbackground="Black")
    taskEntryBox.pack()
    addTaskButton = tk.Button(taskWindow,bg="White",fg="Black",text="Add",command=lambda:add_task(taskEntryBox))
    addTaskButton.pack(side=tk.LEFT)
    cancelButton = tk.Button(taskWindow,text="Cancel",fg="Black",bg="White",command=taskWindow.destroy)
    cancelButton.pack(side=tk.RIGHT)

# functionality of deleting task
def delete_task():
    localIndex = int(str(taskBox.curselection()).replace(",","").replace("(","").replace(")",""))
    taskBox.delete(localIndex)

# Buttons to add and delete tasks
addButton = tk.Button(bottomFrame,text="Add",bg="White",fg="Black",command=create_task_window)
addButton.pack(side=tk.LEFT,padx=70)

deleteButton = tk.Button(bottomFrame,text="Delete",bg="White",fg="Black",command=delete_task)
deleteButton.pack()

mainWindow.mainloop()