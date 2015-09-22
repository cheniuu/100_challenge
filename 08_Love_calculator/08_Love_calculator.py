# -*- coding: UTF-8 -*-
"""
    Simple app which show how compatible 2 people are, by calculating
    a compatibility score. Please look at 08_Love_calculator.readme.
"""

def love_calc():
    pass
    name = raw_input("Please write your name.")
    name_l = raw_input("Please write name of your love one.")
    sum = (name + "loves" + name_l).lower()
    scores = []

    letters = list(sum)
    print letters

    for i in [name, 'loves', name_l]:
        for j in i.lower():
            print j
            if j in letters:
                scores.append(letters.count(j))
                letters[:] = [l for l in letters if l != j]

    print scores



love_calc()
