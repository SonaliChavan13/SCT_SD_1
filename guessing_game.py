import tkinter as tk
from tkinter import messagebox
import random

def new_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="Guess a number between 1 and 100")
    attempts_label.config(text="Attempts: 0")
    entry.delete(0, tk.END)

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}")

        if guess < number:
            result_label.config(text="📉 Too Low! Try again.")
        elif guess > number:
            result_label.config(text="📈 Too High! Try again.")
        else:
            messagebox.showinfo(
                "Congratulations!",
                f"You guessed the number {number} in {attempts} attempts 🎉"
            )
            new_game()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# Main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x300")
root.resizable(False, False)

# Title
tk.Label(root, text="🎯 Number Guessing Game", font=("Arial", 16, "bold")).pack(pady=10)

# Instructions
result_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 11))
result_label.pack(pady=10)

# Input
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

# Buttons
tk.Button(root, text="Check Guess", command=check_guess,
          bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=8)

tk.Button(root, text="New Game", command=new_game,
          bg="#2196F3", fg="white", font=("Arial", 11)).pack(pady=5)

# Attempts
attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 11))
attempts_label.pack(pady=10)

# Initialize game
number = random.randint(1, 100)
attempts = 0

root.mainloop()
