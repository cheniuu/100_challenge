# -*- coding: UTF-8 -*-
import random

count = 0
guessesTaken = 0
min = 1
max = 20
x = random.randint(min, max)

"""
# randint vs randrange (?)
# randrange will not consider last item
# randrange has a step option
# randrange is equivalent to choice(range(start, stop, step)),
#     but doesn't actually build a range object
# randint can only be used when you know both interval limits
# randrange can be used when you know only stop
# !!!randitem return self.randrange(a, b+1)
"""

print "I'm thinking of a number between %s and %s!" % (min, max)

def guessing():
    guess = raw_input("Choose the number with decimal place\n")

    """
    # raw_input vs input (?)
    # input() is the same thing as eval(raw_input())
    # (eval() interprets a string as code) >>> x = 1 >>> eval('x + 1') >>> 2
    """

    global guessesTaken, count
    guessesTaken += 1
    print count
    if count > 5:
        print "You cannot play this game because you are retarded"
        raise Exception("Idiot")

    if guess.isdigit() == False:
        count += 1
        guessing()
    else:
        guess = int(guess)

    if guess < x:
        print "Your guess is too low"
        guessing()
    elif guess > x:
        print "Your guess is too high."
        guessing()
    else:
        print "You guessed my number in %s guesses!" % str(guessesTaken)

guessing()
