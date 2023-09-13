#!/usr/bin/python3
def best_score(a_dictionary):
    b_key = ""
    if a_dictionary:
        best = 0
        for k, v in a_dictionary.items():
            if v > best:
                best = v
                b_key = k
    else:
        return 'None'
    return b_key
