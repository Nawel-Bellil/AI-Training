import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Function to check the guess against the target
def guesstarget(target, guess):
    if target == guess:
        return 0 
    elif target < guess:
        return -1 
    else:
        return 1 

# Function to generate a random target number
def gentarget():
    return random.randint(1, 20)

# Function to handle button click
def on_guess():
    global attempts_left
    guess = int(guess_entry.get())
    result = guesstarget(target, guess)
    if result == 0:
        messagebox.showinfo("Congratulations!", "You guessed the number!")
        reset_game()
    elif result == -1:
        messagebox.showinfo("Too high!", "Your guess is too high. Try again.")
        attempts_left -= 1
        update_attempts_label()
    else:
        messagebox.showinfo("Too low!", "Your guess is too low. Try again.")
        attempts_left -= 1
        update_attempts_label()
    if attempts_left == 0:
        messagebox.showinfo("Out of attempts!", f"Sorry, you're out of attempts. The number was {target}.")
        reset_game()

# Function to reset the game
def reset_game():
    global target, attempts_left
    target = gentarget()
    attempts_left = 10
    update_attempts_label()

# Function to update attempts label
def update_attempts_label():
    attempts_label.config(text=f"Attempts left: {attempts_left}")

# Create the main window
root = tk.Tk()
root.title("Guess My Number Game")

# Initialize target and attempts_left
target = gentarget()
attempts_left = 10

# Pastel colors
pastel_colors = ['#FFB6C1', '#87CEEB', '#98FB98', '#FFD700', '#FFA07A']

# Create style for ttk widgets
style = ttk.Style()
style.theme_use('clam')

# Configure style for label
style.configure('TLabel', background=pastel_colors[0], foreground="#333333", font=("Helvetica", 12), padding=10)

# Configure style for entry
style.configure('TEntry', background="white", font=("Helvetica", 12), padding=10)

# Configure style for button
style.configure('TButton', background=pastel_colors[2], foreground="white", font=("Helvetica", 12), padding=10)

# Create widgets using ttk
instruction_label = ttk.Label(root, text="I'm thinking of a number between 1 and 20. You have 10 attempts to guess it.")
guess_label = ttk.Label(root, text="Enter your guess:")
guess_entry = ttk.Entry(root)
attempts_label = ttk.Label(root, text=f"Attempts left: {attempts_left}")
guess_button = ttk.Button(root, text="Guess", command=on_guess)

# Arrange widgets using grid layout
instruction_label.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(10, 5))
guess_label.grid(row=1, column=0, padx=10, pady=5)
guess_entry.grid(row=1, column=1, padx=10, pady=5)
attempts_label.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)
guess_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Set column weights to make the layout responsive
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Run the event loop
root.mainloop()
