# -*- coding: UTF-8 -*-
"""
    xxx
"""
import random

guessesTaken = 0
count = 0
words = ["jebac siia", "kalkulator", "skurwysynya"]

i = random.randint(0, len(words) - 1)
word = list(words[i])

def guessing():
    guess = raw_input("Choose the letter\n")

    global guessesTaken, count
    guessesTaken += 1

    if count > 5:
        print "You cannot play this game because you are retarded"
        raise Exception("Idiot")
    print guess
    if guess.isalpha() == False:
        count += 1
        guessing()
    else:
        guess = str(guess)
        print guess
    if guess in word:
        print "Your guess is good."
        word[:] = [value for value in word if value != guess]
        print word
    """
        guessing()
    elif guess > x:
        print "Your guess is wrong."
        guessing()
    else:
        print "You guessed my number in %s guesses!" % str(guessesTaken)
    """
guessing()
