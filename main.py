from tkinter import *
from PIL import Image, ImageTk

ROOT_WIDTH = 800
ROOT_HEIGHT = 800

WARNING_WIN_HEIGHT = 200
WARNING_WIN_WIDTH = WARNING_WIN_HEIGHT * 2


FONT = "Arial"
TEXT_SIZE = 20
BUTTON_TEXT_SIZE = 15

TO_DO_HEIGHT = 10
DONE_HEIGHT = int(TO_DO_HEIGHT / 2)

TO_DO_WIDTH = 30
DONE_WIDTH = int(TO_DO_WIDTH / 2)


def confirm_task():
    task = entry.get()
    if task != "":
        to_do_list.insert(0, task.capitalize())
        entry.delete(0, END)
    task_num = Label(root, text=to_do_list.size(), font=(FONT, TEXT_SIZE))
    task_num.grid(column=0, row=2)
    

def delete_task():
    task = to_do_list.get("anchor")
    to_do_list.delete("anchor")
    if task != "":
        done_list.insert(0, task)
    task_num = Label(root, text=to_do_list.size(), font=(FONT, TEXT_SIZE))
    task_num.grid(column=0, row=2)
    

def clear(event):
    entry.delete(0, END)
    entry.unbind("<Button-1>", clicked)
    add_button.config(state="normal")


def save_list():
    pass


def open_list():
    pass


def warning_window():
    global warning_win
    warning_win = Toplevel(root)
    warning_win.title("Clear To Do List")
    warning_win.iconbitmap("exclamation_mark.ico")
    warning_win.resizable(False, False)
    warning_win.attributes("-topmost", "true")
    warning_win.geometry(f"{WARNING_WIN_WIDTH}x{WARNING_WIN_HEIGHT}+{int(500 + ROOT_WIDTH / 2 - WARNING_WIN_WIDTH / 2)}+{int(50 + ROOT_HEIGHT / 2 - WARNING_WIN_HEIGHT / 2)}")
    
    root.attributes("-disabled", "true")

    canvas = Canvas(warning_win, width=WARNING_WIN_WIDTH, height=WARNING_WIN_HEIGHT, bg="red")
    canvas.grid(columnspan=2, rowspan=2)
    message = Label(warning_win, text="Are you sure you want to clear your To Do List?")
    message.grid(columnspan=2, column=0, row=0)
    confirm_button = Button(warning_win, text="Confirm", command=confirm_clear)
    confirm_button.grid(column=0, row=1)
    cancel_button = Button(warning_win, text="Storno", command=storno_clear)
    cancel_button.grid(column=1, row=1)


def confirm_clear():
    to_do_list.delete(0, "end")
    warning_win.destroy()
    root.attributes("-disabled", "false")
    task_num = Label(root, text=to_do_list.size(), font=(FONT, TEXT_SIZE))
    task_num.grid(column=0, row=2)


def storno_clear():
    warning_win.destroy()
    root.attributes("-disabled", "false")
    task_num = Label(root, text=to_do_list.size(), font=(FONT, TEXT_SIZE))
    task_num.grid(column=0, row=2)


# Root
root = Tk()
root.title("To Do List")
root.iconbitmap("to_do.ico")
root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}+500+50")
root.resizable(False, False)

canvas = Canvas(root, width=ROOT_WIDTH, height=ROOT_HEIGHT, bg="gray")
canvas.grid(columnspan=3, rowspan=4)


# Logo
logo = ImageTk.PhotoImage(Image.open("logo.jpg"))
logo_label = Label(image=logo)
logo_label.grid(column=1, row=0)


# Text field - write a name of the task
default_text = StringVar()
default_text.set("Enter your task...")
entry = Entry(root, width=TO_DO_WIDTH, font=(FONT, TEXT_SIZE), textvariable=default_text)
entry.grid(column=1, row=1) 

clicked = entry.bind("<Button-1>", clear)


# Button to add - confirms the task and adds it into the to do list
add_button = Button(root, text="Add", command=confirm_task, font=(FONT, BUTTON_TEXT_SIZE), state="disabled")
add_button.grid(column=2, row=1)


# Button to delete - deletes the task from a list
delete_button = Button(root, text="Done", command=delete_task, font=(FONT, BUTTON_TEXT_SIZE))
delete_button.grid(column=2, row=2)


# To do list - inside will be stacked all the tasks
to_do_list = Listbox(root, width=TO_DO_WIDTH, height=TO_DO_HEIGHT, font=(FONT, TEXT_SIZE))
to_do_list.grid(column=1, row=2)

task_num = Label(root, text=0, font=(FONT, TEXT_SIZE))
task_num.grid(column=0, row=2)


# Done tasks - inside are stacked completed tasks
done_list = Listbox(root, width=DONE_WIDTH, height=DONE_HEIGHT, font=(FONT, TEXT_SIZE))
done_list.grid(column=1, row=3)


# Menu
my_menu = Menu(root)
file = Menu(my_menu, tearoff=0)

file.add_command(label="Save", command=save_list)
file.add_command(label="Open", command=open_list)
file.add_separator()
file.add_command(label="Clear", command=warning_window)

my_menu.add_cascade(label="File", menu=file)
root.config(menu=my_menu)

root.mainloop()