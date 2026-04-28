# Project

##########################################
#
#    Collaboration Statement: I completed this assignment on my own.
#
##########################################

import random
def get_difficulty():
    # Lets user know options for difficulty.
    print("1-100 Number Guessing Game")
    print("Select Difficulty:")
    print("1. Easy (15 attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard (5 attempts)")
    # Input for choice.
    choice = input("Enter Either 1, 2, or 3: ").strip()
    # If user inputs something that is not a choice, it lets the user know and then to try again.
    while choice not in ("1", "2", "3"):
        print("Invalid Choice. Select 1, 2, or 3.")
        choice = input("Enter Either 1, 2, or 3: ").strip()
    # Returns number of attempts based on selection.
    if choice == "1":
        return 15
    elif choice == "2":
        return 10
    else:
        return 5

def get_valid_guess():
    # Initial conditions.
    valid = False
    guess = None
    # Checks if guess is an integer between 1-100, if not it lets you try again. Returns your guess.
    while not valid:
        try:
            guess = int(input("Your Guess (1-100): ").strip())
            if 1 <= guess <= 100:
                valid = True
            else:
                print("Please Enter a Number Between 1-100.")
        except ValueError:
            print("Invalid Input. Select an Integer 1-100")
    return guess

def play_game():
    # Initial Conditions.
    max_attempts = get_difficulty()
    number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    # Lets you know how many attempts you have.
    print(f"\nGuess a Number Between 1-100. You Have {max_attempts} Attempts.\n")
    # As long as you have attempts remaining and haven't guessed correctly, play on.
    while attempts < max_attempts and not guessed_correctly:
        print(f"Attempts Remaining: {max_attempts - attempts}")
        # Checks guess to see if valid and lets you know if its high, low, correct, or no attempts remaining.
        guess = get_valid_guess()
        attempts += 1
        if guess > number:
            print("Too High, Try a Lower Number.\n")
        elif guess < number:
            print("Too Low, Try a Higher Number.\n")
        else:
            guessed_correctly = True
            print(f"\nCongrats You Guessed the Number {number} Correctly!")
    if not guessed_correctly:
        print(f"\n 0 Attempts Left, the Number was {number}.")
        
def main():
    # Allows you to play again if you would like to.
    play_again = True
    while play_again:
        play_game()
        answer = input("\nPlay Again? (y / n): ").strip()
        play_again = answer in "y"
    print("Thank You for Playing.")

if __name__ == "__main__":
    main()
