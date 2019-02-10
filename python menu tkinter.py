import tkinter as tk


def ooo():
    print("Soumil shah Youtube Channel ")

mainwindow=tk.Tk()
mainwindow.geometry("640x340")
mainwindow.title("sensor data ")

menubar=tk.Menu(mainwindow)
sub_menu=tk.Menu(menubar, tearoff=0)
sub_menu.add_command(label="soumil", command=ooo)
sub_menu.add_separator()
sub_menu.add_command(label="shah")
sub_menu.add_separator()

menubar.add_cascade(label="MY Name ", menu=sub_menu)

mainwindow.config(menu=menubar)
mainwindow.mainloop()
