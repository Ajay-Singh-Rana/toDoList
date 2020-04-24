# H3avren@py
import tkinter as tk
import time

# calculating current date
localDate = time.localtime()
date = str(localDate.tm_mday) + "/" + str(localDate.tm_mon) + "/" + str(localDate.tm_year)

# creating main window
mainWindow = tk.Tk()
mainWindow.config(bg="White")
mainWindow.geometry("400x300")
mainWindow.resizable(False,False)

# variables
mode = "light"
taskString = ""
taskButton = ""
taskButtonsList = []
toRemoveList =[]

# loading icons
addButtonIcon = tk.PhotoImage(file="icons/button.png")
addButtonDark = tk.PhotoImage(file="icons/dark_theme/button_dark.png")
removeButtonIcon = tk.PhotoImage(file="icons/removeButtonIcon.png")
removeButtonDark = tk.PhotoImage(file="icons/dark_theme/removeButtonDark.png")

# adding a frame to the right of the main window which will contain add and remove buttons 
rightFrame = tk.Frame(mainWindow,bg="White")
rightFrame.pack(anchor=tk.NE)

# adding a frame to hold tasks
leftFrame = tk.Frame(mainWindow,bg="White")
leftFrame.pack(side=tk.LEFT,anchor=tk.NE,pady=10,padx=20)

def dark_theme():
    global mode
    mode="dark"
    mainWindow.configure(bg="Black")
    addButton.configure(image=addButtonDark,bg="Black",activebackground="Black")
    rightFrame.configure(bg="Black")
    removeButton.configure(activebackground="Black",bg="Black",image=removeButtonDark)
    menuItem.entryconfig("Dark Theme",label="Light Theme",command=light_theme)
    menuItem.config(fg="White",bg="Black")
    leftFrame["bg"] = "Black"
    if(taskButton!=""):
        for _ in taskButtonsList:
            _.configure(bg="Black",fg="White")

def light_theme():
    global mode
    mode="light"
    mainWindow.configure(bg="White")
    addButton.configure(image=addButtonIcon,bg="White",activebackground="White")
    removeButton.configure(image=removeButtonIcon,bg="White",activebackground="White")
    rightFrame.configure(bg="White")
    menuItem.entryconfigure("Light Theme",label="Dark Theme",command=dark_theme)
    menuItem.config(fg="Black",bg="White")
    leftFrame["bg"]="White"
    if(taskButton!=""):
        for _ in taskButtonsList:
            _.configure(bg="White",fg="Black")

menuItem = tk.Menu(fg="Black",bg="White",activebackground="Purple",font=("Times",10,"italic"),border=0)
mainWindow.config(menu = menuItem)
menuItem.add_command(label="Dark Theme",command=dark_theme)

def on_check(taskButton):
    taskButton.configure(command=lambda:on_decheck(taskButton),font=("Helvetica",8,"overstrike"))
    toRemoveList.append(taskButton)

def on_decheck(taskButton):
    taskButton.configure(command=lambda:on_check(taskButton),font=("Helvetica",8,"bold"))
    toRemoveList.remove(taskButton)

def add_It(taskEntryBox):
    global taskString
    global taskButton
    taskString = entryBox.get("1.0","end-1c")
    if(taskString!=""):
        taskButton = tk.Checkbutton(leftFrame,text=taskString,font=("Helvetica",8,"bold"),command=lambda:on_check(taskButton))
        if(mode=="dark"):
            taskButton.configure(fg="White",bg="Black")
        else:
            taskButton.configure(fg="Black",bg="White")
        taskButton.pack()
        taskButtonsList.append(taskButton)
        taskEntryBox.destroy()

def add_task():
    global entryBox
    global mode
    taskEntryBox =  tk.Toplevel()
    taskEntryBox.geometry("200x88")
    taskEntryBox.resizable(False,False)
    topFrame = tk.Frame(taskEntryBox)
    topFrame.pack(side=tk.TOP)
    bottomFrame = tk.Frame(taskEntryBox)
    bottomFrame.pack(side=tk.BOTTOM)
    entryBox = tk.Text(topFrame,height=3,width=200)
    entryBox.pack(fill=tk.BOTH)
    addTaskButton = tk.Button(bottomFrame,activebackground="Purple",text="Add",command=lambda:add_It(taskEntryBox))
    addTaskButton.pack(side=tk.LEFT,padx=10)
    cancelButton = tk.Button(bottomFrame,activebackground="Purple",text="Cancel",command=taskEntryBox.destroy)
    cancelButton.pack(padx=2)
    if(mode=="dark"):
        taskEntryBox.configure(bg="Black")
        entryBox.configure(bg="Black",fg="White",insertbackground="White")
        bottomFrame.configure(bg="Black")
        addTaskButton.configure(bg="Black",fg="White")
        cancelButton.configure(bg="Black",fg="White")
    else:
        taskEntryBox.configure(bg="White")
        entryBox.configure(bg="White",insertbackground="Black",fg="Black")
        bottomFrame.configure(bg="White")
        addTaskButton.configure(bg="White",fg="Black")
        cancelButton.configure(bg="White",fg="Black")

def remove_it():
    if(toRemoveList!=[]):
        for _ in toRemoveList:
            _.destroy()

# add button 
addButton = tk.Button(rightFrame,image=addButtonIcon,bg="White",activebackground="White",border=0,command=add_task)
addButton.pack(side=tk.TOP)

# remove button
removeButton = tk.Button(rightFrame,image=removeButtonIcon,activebackground="White",bg="White",command=remove_it)
removeButton.pack(side=tk.TOP)

mainWindow.mainloop()