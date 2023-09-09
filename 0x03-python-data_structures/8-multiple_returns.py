#!/usr/bin/python3
def multiple_returns(sentence):
    mult_ret = ()
    if len(sentence) == 0:
        mult_ret = 0, 'None'
    else:
        mult_ret = len(sentence), sentence[0]
    return mult_ret
