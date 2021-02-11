'''
The action of a Caesar cipher is to replace each plaintext letter
with a different one a fixed number of places down the alphabet.

A weak encryption, the Caesar Cipher was actually used by Julius Caesar to message his outposts
'''

import string


def caesarCypher(plain, shift):
    # abcdefghijklmnopqrstuvwxy
    alpha = string.ascii_lowercase

    # first 'shift' number of letters are added to the back of the alphabet
    shifted = alpha[shift:] + alpha[:shift]

    # maketrans() creates a Unicode representation of each character for translation
    table = str.maketrans(alpha, shifted)
    return plain.translate(table)


text = input("Enter lowercase string: ")
phi = int(input("Enter shift value: "))
print(f"Caesar Cipher Encryption of {text}: {caesarCypher(text, phi)}\n\n")
# https://cryptii.com/pipes/caesar-cipher double check here
