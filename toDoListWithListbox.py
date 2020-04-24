# h3avren@py
import tkinter as tk

# main window
mainWindow = tk.Tk()
mainWindow.geometry("450x300")
mainWindow.resizable(False,False)
mainWindow.config(bg="White")
mainWindow.title("To-Do List")

# variables
index = 0
completedIndex = 0
mode = "light"

# dark mode functionality
def dark_theme():
    global mode
    mode = "dark"
    mainWindow.config(bg="Black")
    # setting all frames to dark mode
    leftFrame.config(bg="Black",fg="White")
    rightFrame.config(bg="Black",fg="White")
    bottomFrame["bg"] = "Black"
    # setting all listboxes and scrollbars to dark mode
    taskBox.configure(bg="Black",fg="White")
    leftScroll["bg"] = "Black"
    completedTasksBox.configure(bg="Black",fg="White")
    rightScroll["bg"] = "Black"
    # setting all buttons to dark mode
    addButton.configure(bg="Black",fg="White")
    deleteButton.configure(bg="Black",fg="White")
    undoButton.configure(bg="Black",fg="White")
    markAsCompleted.configure(bg="Black",fg="White")
    menuItem.config(bg="Black",fg="White")
    menuItem.entryconfig(1,label="Light Theme",command=light_theme)

# light mode functionality
def light_theme():
    global mode
    mode = "light"
    mainWindow.config(bg="White")
    # setting all frames to dark mode
    leftFrame.config(bg="White",fg="Black")
    rightFrame.config(bg="White",fg="Black")
    bottomFrame["bg"] = "White"
    # setting all listboxes and scrollbars to dark mode
    taskBox.configure(bg="White",fg="Black")
    leftScroll["bg"] = "White"
    completedTasksBox.configure(bg="White",fg="Black")
    rightScroll["bg"] = "White"
    # setting all buttons to dark mode
    addButton.configure(bg="White",fg="Black")
    deleteButton.configure(bg="White",fg="Black")
    undoButton.configure(bg="White",fg="Black")
    markAsCompleted.configure(bg="White",fg="Black")
    menuItem.config(bg="White",fg="Black")
    menuItem.entryconfig(1,label="Dark Theme",command=dark_theme)

# menu for the to do application
menuItem = tk.Menu(fg="Black",bg="White",activebackground="Purple")
menuItem.add_command(label="Dark Theme",command=dark_theme)
mainWindow.config(menu = menuItem)

# bottom frame to hold buttons for adding and deleting tasks
bottomFrame = tk.Frame(mainWindow,bg="White")
bottomFrame.pack(side = tk.BOTTOM)

# left frame to contain incomplete tasks
leftFrame = tk.LabelFrame(mainWindow,text="To Do",fg="Black",bg="White",bd=0)
leftFrame.pack(side=tk.LEFT,anchor=tk.NW,pady=9,padx=15)

# right frame to hold complete tasks
rightFrame = tk.LabelFrame(mainWindow,text="Completed",fg="Black",bg="White",bd=0)
rightFrame.pack(side=tk.RIGHT,anchor=tk.NE,pady=9,padx=15)

# funciton to add Completed tasks to completed task list
def mark():
    global completedIndex
    global index
    if(taskBox.curselection()!=()):
        localIndex = int(str(taskBox.curselection()).replace("(","").replace(")","").replace(",",""))
        taskString = taskBox.get(localIndex)
        taskBox.delete(localIndex)
        completedTasksBox.insert(completedIndex,taskString)
        completedIndex += 1
        index -= 1

# mark as completed button, goes in left frame
markAsCompleted = tk.Button(leftFrame,text="Done",fg="Black",bg="White",command=mark)
markAsCompleted.pack(side=tk.BOTTOM,pady=10)

# listbox to hold incomplete tasks,it goes in the leftFrame
taskBox = tk.Listbox(leftFrame,bg="White",fg="Black")
taskBox.pack(side=tk.LEFT)

# scrollbar for incomplete tasks
leftScroll = tk.Scrollbar(leftFrame)
leftScroll.pack(fill=tk.Y,side=tk.RIGHT)
taskBox.configure(yscrollcommand = leftScroll.set)
leftScroll.configure(command=taskBox.yview)

# function to undo a completed task
def undo():
    global completedIndex
    global index
    if(completedTasksBox.curselection()!=()):
        localIndex = int(str(completedTasksBox.curselection()).replace("(","").replace(")","").replace(",",""))
        taskString = completedTasksBox.get(localIndex)
        taskBox.insert(index,taskString)
        completedTasksBox.delete(localIndex)
        completedIndex -= 1
        index += 1

# undo button,goes in the right frame
undoButton = tk.Button(rightFrame,text="Undo",fg="Black",bg="White",command=undo)
undoButton.pack(side=tk.BOTTOM,padx=30,pady=10)

# listbox to contain completed tasks
completedTasksBox = tk.Listbox(rightFrame,bg="White",fg="Black")
completedTasksBox.pack(side=tk.LEFT)

# scrollbar for complete tasks
rightScroll = tk.Scrollbar(rightFrame)
rightScroll.pack(fill=tk.Y,side=tk.RIGHT)
completedTasksBox.configure(yscrollcommand=rightScroll.set)
rightScroll.configure(command=completedTasksBox.yview)

# funtionality to add tasks
def add_task(window_widgets):
    global index
    # taskEntryBox = 
    # taskWindow = window_widgets[0]
    taskString = window_widgets[1].get("1.0","end-1c")
    if(taskString!=""):
        taskString =  "   " + taskString
        taskBox.insert(index,taskString)
        index +=1
    window_widgets[0].destroy()

# pop up window for add button to enter tasks
def create_task_window():
    taskWindow = tk.Toplevel()
    taskWindow.resizable(False,False)
    taskWindow.geometry("200x88")
    taskEntryBox = tk.Text(taskWindow,width=200,height=3)
    taskEntryBox.pack()
    window_widgets = [taskWindow,taskEntryBox]
    addTaskButton = tk.Button(taskWindow,bg="White",fg="Black",text="Add",command=lambda:add_task(window_widgets))
    addTaskButton.pack(side=tk.LEFT)
    cancelButton = tk.Button(taskWindow,text="Cancel",fg="Black",bg="White",command=taskWindow.destroy)
    cancelButton.pack(side=tk.RIGHT)
    if(mode=="dark"):
        taskWindow.config(bg="Black")
        taskEntryBox.config(bg="Black",fg="White",insertbackground="White")
        addTaskButton.config(bg="Black",fg="White")
        cancelButton.config(bg="Black",fg="White")
    else:
        taskWindow.config(bg="White")
        taskEntryBox.config(bg="White",fg="Black",insertbackground="Black")
        addTaskButton.config(bg="White",fg="Black")
        cancelButton.config(bg="White",fg="Black")
    
# functionality of deleting task
def delete_task():
    if(taskBox.curselection()!=()):
        localIndex = int(str(taskBox.curselection()).replace(",","").replace("(","").replace(")",""))
        taskBox.delete(localIndex)

# Buttons to add and delete tasks
addButton = tk.Button(bottomFrame,text="Add",bg="White",fg="Black",command=create_task_window)
addButton.pack(side=tk.LEFT,padx=20)

deleteButton = tk.Button(bottomFrame,text="Delete",bg="White",fg="Black",command=delete_task)
deleteButton.pack()

mainWindow.mainloop()