import sys
from termcolor import colored, cprint

number_tries = 5
word = "blok"
print_black_on_green = lambda x: cprint(x, "black", "on_green")
print_black_on_red = lambda x: cprint(x, "black", "on_red")

user_word = []
used_letters = []


def find_index(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_state_of_game():
    print()
    print(user_word)
    print(colored("Pozostało prób:", "cyan"), colored(number_tries, "cyan"))
    print("Użyte litery:", used_letters)


for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę: ")
    used_letters.append(letter)

    found_indexes = find_index(word, letter)

    if len(found_indexes) == 0:
        print(colored("Nie ma takiej litery", "yellow"))
        number_tries -= 1

        if number_tries == 0:
            print(colored("---------------------------------------", "red"))
            print_black_on_red("\t" + "      Game over     ")
            print(colored("---------------------------------------", "red"))
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

    if "".join(user_word) == word:
        print()
        print(colored("Super! Odgadłes słowo", "green"))
        print(colored("-----------------------------------------", "green"))
        print_black_on_green(" " + word + " ")
        print(colored("-----------------------------------------", "green"))
        sys.exit(0)

    show_state_of_game()

# https://github.com/termcolor/termcolor
