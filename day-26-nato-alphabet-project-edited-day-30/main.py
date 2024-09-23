import pandas



data = pandas.read_csv("nato_phonetic_alphabet.csv")


#
# new_dict = {letter:letter for letter in alphabet_list}
# new_dict2 = {new_key:new_value for (index,row) in new_dit}
new_dic = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [new_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()



