#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 'None'
    else:
        Top = my_list[0]
        for j in range(1, len(my_list)):
            if my_list[j] > Top:
                Top = my_list[j]
        return Top
