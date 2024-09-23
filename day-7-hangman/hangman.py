
import random
import hangman_words
import hangman_art



#choose random word and convert them in characters, setting
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(chosen_word)
chosen_word_characters = []
end_of_game = False
lives = 6

print(hangman_art.logo)

for letter in chosen_word:
    chosen_word_characters.append(letter)
print(chosen_word_characters)

#display "_"
display = []
word_length = len(chosen_word_characters)
for _ in range(word_length):
    display.append("_")
print(display)

#check if the letter match, and replace it with the value. if all the character matches, the game ends
while not end_of_game:
    #user insert one letter
    guess = str(input("Guess a letter:\n").lower())

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word_characters)):
        letter = chosen_word_characters[position]
        if letter == guess:
            display[position] = letter
    print(display)

    print(hangman_art.stages[lives])

    if guess not in chosen_word_characters:
        print("You chose a wrong letter. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    #if all the letters are guessed - win
    if "_" not in display:
        end_of_game = True
        print("You win")



