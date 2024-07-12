import print_screen
import gallows
import ReadDataFromCSV
import random


# here I set every character in sub as _ except for non-letters.
def setup_sub(animal, sub):
    for a in range(0, len(animal)):
        if 'a' <= animal[a] <= 'z' or 'A' <= animal[a] <= 'Z':
            sub.append('_')
        else:
            sub.append(animal[a])
    return sub


# This just prints all the letters in sub
def print_characters(sub):
    for a in sub:
        print(a, end='')
    print("")


# Here I check to see if the letter I guessed is in the animal's name
# Also, if letter found I return whether you won or not.  You won if there are no more _ in sub.
def check_guess(guess, animal, sub):
    found = 0
    still = -1
    for a in range(0, len(animal)):
        if guess.lower() == animal[a] or guess.upper() == animal[a]:
            sub[a] = animal[a]
            found = 1
        elif sub[a] == '_':
            still = 1
    if found == 1:
        print("Correct!!!!")
        # print("still is " + str(still))
        return still, sub
    else:
        print("Wrong!")
        # print("still is " + str(still))
        return False, sub


# Here is the meat of the program.
def playgame(animals):
    # print_screen.print_screen(gallows.gallow[0])
    wrong_tries = 0
    won_game = False
    random.seed()
    choice = random.randint(0, len(animals)-1)
    sub = []
    tried_guesses = []
    sub = setup_sub(animals[choice][0], sub)
    while not won_game and wrong_tries < len(gallows.gallow) - 1:
        print_screen.print_screen(gallows.gallow[wrong_tries])
        print("Tried Guesses:", end='')
        for letter in tried_guesses:
            print(letter, end='')
        print("")
        # print("Animal is:", animals[choice][0])
        print("Animal is: ", end='')
        print_characters(sub)
        print("It is under the category of", animals[choice][1])
        print("It is listed as", animals[choice][2])
        # print_characters(sub)
        wrong_guess = True
        while wrong_guess:
            guess = input("Guess a letter: ")
            if guess.lower() in tried_guesses or guess.upper() in tried_guesses:
                print("You already guessed that letter.  Try again!")
            else:
                wrong_guess = False
        result, sub = check_guess(guess, animals[choice][0], sub)
        if not result:
            wrong_tries += 1
        elif result == -1:
            print("You win!")
            print("The word was", animals[choice][0])
            won_game = True
        tried_guesses.append(guess)
    if wrong_tries == len(gallows.gallow) - 1:
        print_screen.print_screen(gallows.gallow[wrong_tries])
        print("You lost!")
        print("The animal was", animals[choice][0])


# print("Welcome to Hangman!")
animals = ReadDataFromCSV.load_data()
playgame(animals)
