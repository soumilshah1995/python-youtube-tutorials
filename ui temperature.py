import tkinter as tk
import numpy as np
import random
import time
import datetime
import threading


def tick():

    time2=time.strftime('%H:%M:%S')
    clock.config(text=time2)
    clock.after(200,tick)


def get_data():
    threading.Timer(5, get_data).start()
    x=np.random.randint(0,40,1)
    print(x[0])
    l_display.config(text = x[0])
    return x[0]

mainwindow = tk.Tk()
mainwindow.geometry('640x340')
mainwindow.title("Sensor Data Live Feed ")

clock=tk.Label(mainwindow,font=("Arial",30), bg='green',fg="white")
clock.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

l_m=tk.Label(mainwindow,text="Sensor Data ",font=("Arial",30),fg="Black")
l_m.grid(row=0,column=1, padx=10, pady=10, sticky="nsew")

l_t=tk.Label(mainwindow, text="Temperature C",font=("Arial",25))
l_t.grid(row=1,column=0, padx=10, pady=10, sticky="nsew")

l_display=tk.Label(mainwindow,font=("Arial",25),fg="red")
l_display.grid(row=1,column=1, padx=10, pady=10, sticky="nsew")


tick()
get_data()

mainwindow.mainloop()

