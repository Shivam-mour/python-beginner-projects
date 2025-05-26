# Import the random module to generate a random number
import random

# Define the main function for the number guessing game
def number_guessing_game():
    # Generate a random number between 1 and 100 (inclusive)
    number_to_guess = random.randint(1, 100)
    attempts = 0  # Counter to track the number of guesses

    # Welcome message
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop until the user guesses the correct number
    while True:
        try:
            # Take user input and convert it to an integer
            guess = int(input("Take a guess: "))
            attempts += 1  # Increment attempt count

            # Compare guess with the actual number
            if guess < number_to_guess:
                print("Too low!")  # Hint for the user
            elif guess > number_to_guess:
                print("Too high!")  # Hint for the user
            else:
                # Correct guess
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop
        except ValueError:
            # Handle case when user inputs non-integer
            print("Please enter a valid number.")

# Run the game
number_guessing_game()
