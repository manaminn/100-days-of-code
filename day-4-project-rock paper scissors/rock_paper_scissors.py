import random

user_choice =int(input("WHat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)
print(f"Computer choice: {computer_choice}")

if computer_choice == 0 and user_choice == 1:
    print("User wins")

elif computer_choice == 1 and user_choice == 2:
    print("User wins")

elif computer_choice == 2 and user_choice == 0:
    print("User wins")

elif user_choice == computer_choice:
    print("draw")

else:
    print("Computer wins")
