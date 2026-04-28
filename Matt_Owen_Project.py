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
