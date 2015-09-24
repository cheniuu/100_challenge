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
    # print letters

    for i in [name, 'loves', name_l]:
        for j in i.lower():
            # print j
            if j in letters:
                scores.append(letters.count(j))
                letters[:] = [l for l in letters if l != j]

    # print scores
    state = True
    while state:
        temp = []
        len_score = len(scores)
        int_score = int(''.join(str(a) for a in scores))

        if int_score < 100:
            # state = False
            break

        if len_score % 2 == 0:
            for i in xrange(int(round(len(scores) / 2.0))):
                sum_score = scores[i] + scores[-(i + 1)]
                if len(str(sum_score)) > 1:
                    sum_score = [int(a) for a in str(sum_score)]
                    for j in xrange(len(sum_score)):
                        temp.append(sum_score[j])
                else:
                    temp.append(sum_score)
        else:
            for i in xrange(len(scores) / 2):
                sum_score = scores[i] + scores[-(i + 1)]
                if len(str(sum_score)) > 1:
                    sum_score = [int(a) for a in str(sum_score)]
                    for j in xrange(len(sum_score)):
                        temp.append(sum_score[j])
                else:
                    temp.append(sum_score)
            # temp[:] = [int(x) for x in temp]
            temp.append(scores[int(i) + 1])
        scores = temp

    print "Your love has %s%% chance to survive." % int_score

love_calc()
