#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list
