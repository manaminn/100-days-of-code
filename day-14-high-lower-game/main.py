import art
import random
from game_data import data
from replit import clear


def choose_a_person():
    person = random.choice(data)
    return person

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    followers = account['follower_count']
    return f"{name}, a {description}, from {country}... {followers}"

def find_winner(a, b):
    if a['follower_count'] > b['follower_count']:
        return "a"
    elif a['follower_count'] == b['follower_count']:
        return "even"
    else:
        return "b"

def check_answer(user_choice, winner):
    if user_choice == winner:
        return "correct"
    else:
        return "Incorrect"

score = 0
end_game = False

person_a = choose_a_person()
person_b = choose_a_person()

while end_game is False:
    print(art.logo)
    person_a = person_b
    person_b = choose_a_person()
    while person_a == person_b:
        clear()
        person_b = choose_a_person()
    print(f"Compare A: {format_data(person_a)}")
    print(art.vs)
    print(f"Against B: {format_data(person_b)}")

    winner_dictionary = find_winner(person_a, person_b)

    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    check = check_answer(user_choice.lower(), winner_dictionary)

    clear()
    if check == "correct":
        score += 1
        print(f"Correct. Score: {score}")

    else:
        end_game = True
        print(f"You lost. Final Score is: {score} ")











