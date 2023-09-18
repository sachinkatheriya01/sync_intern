import tkinter as tk
from tkinter import messagebox
import time

def set_alarm():
    alarm_time = entry.get()
    try:
        time.strptime(alarm_time, "%H:%M")
        return alarm_time
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid time in HH:MM format.")

def activate_alarm():
    global alarm_active
    alarm_time = set_alarm()
    if alarm_time:
        alarm_active = True
        label.config(text=f"Alarm set for {alarm_time}")
        while alarm_active:
            current_time = time.strftime("%H:%M")
            if current_time == alarm_time:
                messagebox.showinfo("Alarm", "Time to wake up!")
                break
            root.update()
            time.sleep(1)

def stop_alarm():
    global alarm_active
    alarm_active = False
    label.config(text="Alarm stopped")

root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Enter the time for the alarm (HH:MM):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

set_button = tk.Button(root, text="Set Alarm", command=activate_alarm)
set_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Alarm", command=stop_alarm)
stop_button.pack(pady=10)

alarm_active = False

root.mainloop()
