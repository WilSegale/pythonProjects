import tkinter as tk
import time

root = tk.Tk()
root.title("Clock")

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    label.config(text = current_time)
    label.after(1000, update_time)

label = tk.Label(root, font = ("calibri", 40, "bold"))
label.pack()

update_time()

root.mainloop()
