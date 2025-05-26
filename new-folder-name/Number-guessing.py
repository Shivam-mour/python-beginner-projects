# Import tkinter for GUI components and messagebox for popup alerts
import tkinter as tk
from tkinter import messagebox
import random

# Define a class for the Number Guessing Game
class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")  # Set window title
        self.root.geometry("300x200")  # Set window size

        # Generate a random number between 1 and 100
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0  # Track number of attempts

        # Label prompting user to guess
        self.label = tk.Label(root, text="Guess a number (1–100):")
        self.label.pack(pady=10)

        # Entry box for user input
        self.entry = tk.Entry(root)
        self.entry.pack()

        # Button to submit guess
        self.button = tk.Button(root, text="Submit", command=self.check_guess)
        self.button.pack(pady=10)

        # Label to show result messages
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    # Function to check the user's guess
    def check_guess(self):
        try:
            guess = int(self.entry.get())  # Get guess from entry
            self.attempts += 1  # Increase attempt count

            # Compare guess to the generated number
            if guess < self.number_to_guess:
                self.result_label.config(text="Too low!")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high!")
            else:
                # Show success message
                messagebox.showinfo("Congratulations!",
                                    f"You guessed it in {self.attempts} attempts!")
                self.reset_game()  # Reset game after correct guess
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")  # Handle invalid input

    # Function to reset the game
    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)  # New number
        self.attempts = 0  # Reset attempt counter
        self.entry.delete(0, tk.END)  # Clear input field
        self.result_label.config(text="")  # Clear result label

# Start the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
