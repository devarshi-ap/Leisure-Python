import random

# ASK USER FOR LETTER
def promptUser():
    guess = input("Guess a letter: ")
    return guess


# FIND INDICES OF LETTER IN WORD
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


# UPDATE UNKNOWN
def checkLetter(wrd, ukn, ltr):
    indices = find(wrd, ltr)

    for i in indices:
        ukn = ukn[:i] + wrd[i] + ukn[i + 1:]
    return ukn
