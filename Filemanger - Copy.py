import os
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("File Manager")

def open_file():
    filepath = filedialog.askopenfilename()
    os.startfile(filepath)

def open_folder():
    folder_path = filedialog.askdirectory()
    os.startfile(folder_path)

open_file_button = Button(root, text="Open File", command=open_file)
open_file_button.pack()

open_folder_button = Button(root, text="Open Folder", command=open_folder)
open_folder_button.pack()

root.mainloop()
