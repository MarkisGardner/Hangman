import os

def print_title():
    print(20*" ","Markis's Hangman!")

def print_gallows(gallow):
    print(gallow)
def print_screen(gallow):
    #os.system('cls')
    print_title()
    print_gallows(gallow)

