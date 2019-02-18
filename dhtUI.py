import tkinter as tk
import numpy as np
import random
import time
import datetime
import threading
import Adafruit_DHT

pin = 4
sensor = Adafruit_DHT.DHT22

def tick():

    time2=time.strftime('%H:%M:%S')
    clock.config(text=time2)
    clock.after(200,tick)


def get_data():

    threading.Timer(5, get_data).start()

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        l_display.config(text = temperature)
    else:
        print('Failed to get reading. Try again!')


    return temperature



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

