#for GUI 
import tkinter
#for using the messagebox
import tkinter.messagebox
import pickle


#declare a variable named window 
# for the tkinter with the Tk() func declare
window = tkinter.Tk()


#title for the window
window.title("To Do List")

#for frame

list_frame = tkinter.Frame(window)
#implement the tkinter process
list_frame.pack()


#list box = design the lisst box in frame

todo_box = tkinter.Listbox(list_frame,height=20,width=50)
# apply the methods and set the box appear in left
todo_box.pack(side=tkinter.LEFT)

#scroll bar

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)

# box for adding the task
todo_box.config(yscrollcommand=scroller.set)
# scroller.config(command=list_frame.yview)

#function for the store the task using entry
task_add =tkinter.Entry(window,width=70)
task_add.pack()


#functions to perform the task for the buttons

# adding task
def task_adding():
    todo = task_add.get()
    
    if todo != "": #condition for adding the values and delete the empty 
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else: #condition for warning for the value cannot be empty
        tkinter.messagebox.showwarning(title="ATTENTION : ",message="Task cannot be empty.Enter some Task")
        
# removing task
def task_removing():
    try:
        #function to start when deleting the list
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
        
    except IndexError: #message 
        tkinter.messagebox.showwarning(title="ATTENTION",message="Select a task to delete")
       
# loading task
def task_loading():
    try:       
        todo_list=pickle.load(open("task.dat","rb"))
        todo_box.delete(0,tkinter.END)
        for todo in todo_list:
            todo_box.inset(tkinter.END,todo)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="ATTENTION!!",message="Cannot find the task.dat")

# saving task
def task_saving():
    todo_list = todo_box.get(0,tkinter.END)
    pickle.dump(todo_list,open("tasks.dat","wb"))


#adding the buttons
#add button
add_task_button = tkinter.Button(window,text="Add Task",font=("Monospace",20),background="white",width=20,command=task_adding)
add_task_button.pack()

#remove button
remove_task_button = tkinter.Button(window,text="Delete Task",font=("Monospace",20),background="white",width=20,command=task_removing)
remove_task_button.pack()

#load button
load_task_button =tkinter.Button(window,text="Load",font=("Monospace",20),background="white",width=20,command=task_loading)
load_task_button.pack()

#save button
save_task_button = tkinter.Button(window,text="Save",font=("Monospace",20),background="white",width=20,command=task_saving)
save_task_button.pack()



window.mainloop()