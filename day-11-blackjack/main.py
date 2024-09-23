import random
from replit import clear
from art import logo

def deal_card():
    '''returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards) ==2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.append(1)
        cards.remove(11)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "you went over"

    if user_score == computer_score:
        return "draw"
    elif user_score == 0:
        return "wins with a blackjack"
    elif computer_score == 0:
        return "computer wins with a blackjack"
    elif user_score > 21:
        return "you went over, you lose"
    elif computer_score > 21:
        return "opponent went over, you win"
    else:
        if computer_score > user_score:
            return "computer wins"
        else:
            return "user wins"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    continue_dealing = True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while continue_dealing:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >21:
            continue_dealing = False
        else:
            user_decide = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_decide == "y":
                user_cards.append(deal_card())
            else:
                continue_dealing = False

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BLackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()




