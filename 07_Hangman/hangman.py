# -*- coding: UTF-8 -*-
"""
    Simple game where the user tries to guess each letter in a word.
"""
import random, os

guessesTaken = 0
count = 0
remaining = 10  # how many attempts can be taken
words = ["jebac sii", "kalkulator", "skurwysyny"]

i = random.randint(0, len(words) - 1)
word = list(words[i])
word_temp = word * 1
guesses = []
print [w.replace(w, '_') for w in word_temp]

def guessing():

    global guessesTaken, count, remaining
    guessesTaken += 1

    guess = raw_input("Choose the letter.\n")
    remaining -= 1
    print "\n%d chances remaining..." % remaining

    # checking if someone don't know what does it mean 'letter'
    if count > 5:
        print "You cannot play this game because you are retarded."
        raise Exception("Idiot")

    if guess.isalpha() == False:
        count += 1
        guessing()
    else:
        guess = str(guess)

    # check if guess == letter
    if guess in word:
        print "Your guess is good."
        word[:] = [w.replace(guess, '_') for w in word]
        # word[:] = [value for value in word if value != guess]
        guesses.append(guess)
    else:
        print "Your guess is not good."

    # printing you guesses
    temp = []
    for w in word_temp:
        if w not in guesses:
            temp.append('_')
        else:
            temp.append(w)
    print temp

    # checking if win
    temp = [w for w in word if w.isalpha() is True]
    if len(temp) < 1:
        print "You won"
        return

    remaining_lett = len(set(filter(lambda x: x.isalpha(), word)))
    # check if someone have no chance to win
    if remaining_lett > remaining:
        print "You loose. There is no possibility to win this game."
        print "You have at least %d letters to guess and %d chances.\n" % (remaining_lett, remaining)
        return

    guessing()


guessing()
