import random
import time

# Global variable to track high score
high_score = float('inf')  # Initialize with infinity to ensure any number of attempts will be better

def print_welcome_message():
    """
    Print a welcome message and game instructions.
    """
    print("🎉 Welcome to Guess the Number! 🎉")
    print("You will choose a difficulty level and try to guess a number.")
    print("The number of attempts will vary based on the difficulty.")
    print("Good luck!")

def print_ascii_art():
    """
    Print ASCII art for the game.
    """
    print("""
     ____                 
    / ___| ___   ___   ___ 
   | |  _ / _ \ / _ \ / _ \\
   | |_| | (_) | (_) | (_) |
    \____/ \___/ \___/ \___/ 
    """)

def setup_difficulty(difficulty):
    """
    Set up the game difficulty based on user input.
    
    Parameters:
    difficulty (str): The chosen difficulty level (easy, medium, hard).
    
    Returns:
    tuple: The number to guess and the maximum number of attempts.
    """
    if difficulty == 'easy':
        return random.randint(1, 10), 5
    elif difficulty == 'medium':
        return random.randint(1, 50), 7
    else:
        return random.randint(1, 100), 10

def guess_the_number():
    """
    Main function to run the Guess the Number game.
    """
    global high_score
    print_ascii_art()
    print_welcome_message()
    
    difficulty = input("Choose difficulty (Easy, Medium, Hard): ").lower()
    number_to_guess, max_attempts = setup_difficulty(difficulty)
    
    attempts = 0
    guessed = False
    start_time = time.time()

    while not guessed and attempts < max_attempts:
        try:
            player_guess = int(input("Guess the number: "))
            attempts += 1
            
            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Congratulations! You've guessed the number in {attempts} attempts and {elapsed_time:.2f} seconds.")
                guessed = True
                
                if attempts < high_score:
                    high_score = attempts
                    print(f"New high score: {high_score} attempts!")
        except ValueError:
            print("Please enter a valid number.")
    
    if not guessed:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number()

# Start the game
guess_the_number()
