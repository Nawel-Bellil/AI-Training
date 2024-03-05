import tkinter as tk

# Function to change label text
def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create a label widget
label = tk.Label(root, text="Hello, GUI!", pady=10)
label.pack()

# Create a button widget
button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

# Run the event loop
root.mainloop()
