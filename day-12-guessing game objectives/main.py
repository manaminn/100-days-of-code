import random


def low_or_high(user_choice, chosen_number, number_of_attempts):
    if user_choice == chosen_number:
        print( f"Yay! The answer is {chosen_number}")
    elif user_choice > chosen_number:
        print(f"Too high.")
        return number_of_attempts - 1
    elif user_choice < chosen_number:
        print(f"Too low")
        return number_of_attempts - 1

def set_difficulties():
    level = input("Choose a difficulty. Type 'easy' or hard': ")
    if level == "easy":
        return 10
    else:
        return 5

def game():
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100")
    chosen_number = random.randint(1, 100)
    ## player choose the difficulty level (easy - 10 attempts, hard - 5 attempts)
    number_of_attempts = set_difficulties()

    # run the program
    user_choice = 0
    while user_choice != chosen_number:
        user_choice = int(input(f"You have {number_of_attempts} attempts remaining to guess the number. \nMake a guess: "))

        number_of_attempts = low_or_high(user_choice, chosen_number, number_of_attempts)
        if number_of_attempts == 0:
            print("You've ran out of guesses, you lose")
            return

play_or_not = input("Do you want to play the game? Type 'y' for yes or 'n' for no: ")
if play_or_not == "y":
    game()
else:
    print("okay")

















