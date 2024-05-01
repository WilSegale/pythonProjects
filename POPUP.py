import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()

# Set the title of the window
window.title("Hello World Popup")

# Create a label with the text "Hello World"
label = tk.Label(window, text='''HAHAHAH YOU HAVE BEEN HACKED.
                 I AM WATCHING YOU''', font=("Arial", 30))

# Pack the label into the window
label.pack()

# Run the application
window.mainloop()
