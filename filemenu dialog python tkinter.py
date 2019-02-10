import tkinter as tk
from tkinter import filedialog

def open_handler():
    name = tk.filedialog.askopenfilename(filetypes=(("file","*.jpg"),("All Files","*.*") ))
    print(name)

mainwindow=tk.Tk()
mainwindow.geometry("640x340")
mainwindow.title("sensor data ")

menubar=tk.Menu(mainwindow)
sub_menu=tk.Menu(menubar, tearoff=0)
sub_menu.add_command(label="Open File ", command=open_handler)
sub_menu.add_separator()

menubar.add_cascade(label="File", menu=sub_menu)

mainwindow.config(menu=menubar)
mainwindow.mainloop()