import main as mm

words = ['charizard', 'blastoise', 'venasaur', 'mewtwo', 'blaziken', 'pokemon']
guessed = []
lives = 3

# select random word from list and make the sequence of dashes to represent the unknown word
word = mm.random.choice(words)
unknown = "-" * len(word)
print("{}\n{}".format(word, unknown))


# while player still has lives, repeat body code
while lives != 0:
    letter = mm.promptUser().lower()

    # check if already guessed
    if letter in guessed:
        print("You already guess this word")
        continue

    # update dash-sequence if letter is in the word and add letter to 'guessed' list
    if letter in word:
        unknown = mm.checkLetter(word, unknown, letter)
        guessed.append(letter)
        print(unknown)

    # if letter's not in the word, one life is lost and add letter to 'guessed' list
    else:
        lives -= 1
        guessed.append(letter)
        print("{} isn't in the word!\nlives: {}".format(letter, lives))

    # if the player has guessed all the letters, break out of while loop
    if "-" not in unknown:
        break


print("\n\nYou guessed the following letters: {}".format(guessed))


# give user an appropriate ending message (win/lose)
if lives == 0:
    print("you lost all your lives.......GAME OVER!")
else:
    print("CONGRATULATIONS")
