import tkinter as tk
import pyttsx3
TELLUSER = "HAHAHAH YOU HAVE BEEN HACKED. I AM WATCHING YOU"
# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150) # Speed of speech
engine.setProperty('volume', 0.9) # Volume (0.0 to 1.0)

# Text you want the computer to say
text_to_say = TELLUSER

# Use the say method
engine.say(text_to_say)

# Run the TTS engine
engine.runAndWait()
# Create a new Tkinter window
window = tk.Tk()

# Set the title of the window
window.title("Popup")

# Create a label with the text "Hello World"
label = tk.Label(window, text=TELLUSER, font=("Arial", 30))

# Pack the label into the window
label.pack()

# Run the application
window.mainloop()
