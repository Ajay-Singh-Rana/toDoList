# H3avren@py
import tkinter as tk
import time

# calculating current date
localDate = time.localtime()
date = str(localDate.tm_mday) + "/" + str(localDate.tm_mon) + "/" + str(localDate.tm_year)

# creating main window
mainWindow = tk.Tk()
mainWindow.geometry("400x300")
mainWindow.resizable(False,False)

# adding Frame widget to hold a list of to do items
mainFrame = tk.Frame(mainWindow)
mainFrame.pack()

# adding a frame to the right of the main window which will contain add and remove buttons 
rightFrame = tk.Frame(mainWindow)
rightFrame.pack(anchor=tk.NE)

def add_task():
    taskEntryBox =  tk.Toplevel()
    taskEntryBox.geometry("200x50")
    topFrame = tk.Frame(taskEntryBox)
    topFrame.pack(side=tk.TOP)
    bottomFrame = tk.Frame(taskEntryBox)
    bottomFrame.pack(side=tk.BOTTOM)
    entryBox = tk.Entry(topFrame,width=200)
    entryBox.pack(fill=tk.BOTH)
    addTaskButton = tk.Button(bottomFrame,text="Add task")
    addTaskButton.pack(side=tk.RIGHT)
    cancelButton = tk.Button(bottomFrame,text="Cancel")
    cancelButton.pack(anchor=tk.NE)

# add button 
addButton = tk.Button(rightFrame,text="+",fg="White",bg="Black",command=add_task)
addButton.pack(side=tk.TOP)

# remove button
removeButton = tk.Button(rightFrame,text=" - ",fg="White",bg="Black")
removeButton.pack(side=tk.TOP)

mainWindow.mainloop()